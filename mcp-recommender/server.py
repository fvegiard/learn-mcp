"""AI-Powered MCP Recommendation Server.

Analyzes natural language requests and recommends the best MCP server(s)
for the task. Uses NVIDIA NIM (free) as primary LLM with Ollama fallback.
"""

from __future__ import annotations

import functools
import hashlib
import json
import os
import httpx
from mcp.server.fastmcp import FastMCP

# Must bind 0.0.0.0 inside container for docker-proxy + cross-container access.
# Host exposure limited by the compose `127.0.0.1:8002:8002` port prefix.
mcp = FastMCP("mcp-recommender", host="0.0.0.0", port=8002)

NVIDIA_API_KEY = os.environ.get("NVIDIA_API_KEY", "")
NVIDIA_BASE_URL = "https://integrate.api.nvidia.com/v1"
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://127.0.0.1:11434")
LEARN_URL = os.environ.get("LEARN_URL", "http://127.0.0.1:8001")
DEFAULT_MODEL = "meta/llama-3.1-8b-instruct"

# ── Built-in MCP knowledge base ──────────────────────────────────────────

MCP_SERVERS = [
    {
        "name": "playwright",
        "category": "browser",
        "description": "Browser automation — navigate, click, type, screenshot, extract content from web pages",
        "install": "npx @anthropic-ai/mcp-playwright",
        "stars": 12000,
        "tags": ["browser", "automation", "testing", "scraping"],
    },
    {
        "name": "filesystem",
        "category": "storage",
        "description": "Read, write, and search files on the local filesystem with configurable access controls",
        "install": "npx @anthropic-ai/mcp-filesystem",
        "stars": 8000,
        "tags": ["files", "storage", "local"],
    },
    {
        "name": "memory",
        "category": "knowledge",
        "description": "Persistent knowledge graph for storing and retrieving entities, relations, and observations across sessions",
        "install": "npx @anthropic-ai/mcp-memory",
        "stars": 3000,
        "tags": ["memory", "knowledge-graph", "persistence"],
    },
    {
        "name": "sequential-thinking",
        "category": "reasoning",
        "description": "Dynamic problem-solving through structured step-by-step thinking with revision and branching",
        "install": "npx @anthropic-ai/mcp-sequential-thinking",
        "stars": 2500,
        "tags": ["reasoning", "thinking", "planning"],
    },
    {
        "name": "fetch",
        "category": "web",
        "description": "Fetch and extract content from web URLs with optional HTML-to-markdown conversion",
        "install": "npx @anthropic-ai/mcp-fetch",
        "stars": 5000,
        "tags": ["web", "fetch", "scraping", "http"],
    },
    {
        "name": "time",
        "category": "utility",
        "description": "Get current time and convert between timezones",
        "install": "npx @anthropic-ai/mcp-time",
        "stars": 800,
        "tags": ["time", "timezone", "utility"],
    },
    {
        "name": "sqlite",
        "category": "database",
        "description": "SQLite database operations — create tables, run queries, append insights",
        "install": "npx @anthropic-ai/mcp-sqlite",
        "stars": 1500,
        "tags": ["database", "sqlite", "sql"],
    },
    {
        "name": "github",
        "category": "devops",
        "description": "GitHub API integration — issues, PRs, repos, code search, actions",
        "install": "npx @anthropic-ai/mcp-github",
        "stars": 6000,
        "tags": ["github", "git", "devops", "ci"],
    },
    {
        "name": "qdrant",
        "category": "database",
        "description": "Qdrant vector database — semantic search, point management, collection operations",
        "install": "pip install mcp-qdrant",
        "stars": 800,
        "tags": ["vector", "search", "database", "embeddings"],
    },
    {
        "name": "host-router",
        "category": "compute",
        "description": "Route tasks to different compute backends — Claude Code, Gemini, OpenRouter, ComfyUI, Ollama",
        "install": "custom",
        "stars": 100,
        "tags": ["routing", "compute", "multi-model", "orchestration"],
    },
    {
        "name": "comfyui",
        "category": "image",
        "description": "Image generation via ComfyUI — txt2img, img2img, upscale, inpaint, ControlNet, IP-Adapter workflows",
        "install": "custom",
        "stars": 200,
        "tags": ["image", "generation", "comfyui", "stable-diffusion", "flux"],
    },
    {
        "name": "ollama",
        "category": "llm",
        "description": "Run local LLMs via Ollama — list models, generate completions, chat, embeddings",
        "install": "custom",
        "stars": 500,
        "tags": ["llm", "local", "ollama", "generation"],
    },
    {
        "name": "nacos-mcp-router",
        "category": "orchestration",
        "description": "MCP gateway and registry — discover, install, and proxy other MCP servers with Nacos service discovery",
        "install": "pip install nacos-mcp-router",
        "stars": 174,
        "tags": ["gateway", "registry", "proxy", "discovery"],
    },
    {
        "name": "mcp-research-router",
        "category": "orchestration",
        "description": "Aggregate multiple MCP servers with LLM-powered tool recommendation and parallel execution",
        "install": "npx mcp-research-router",
        "stars": 22,
        "tags": ["aggregation", "recommendation", "parallel", "routing"],
    },
    {
        "name": "learn",
        "category": "education",
        "description": "AI/ML learning reference MCP — 801 references across 12 topics with semantic search",
        "install": "custom",
        "stars": 50,
        "tags": ["learning", "education", "references", "search"],
    },
]


# ── LLM client ────────────────────────────────────────────────────────────


@functools.lru_cache(maxsize=128)
def _cached_llm(cache_key: str, prompt: str, system: str, max_tokens: int) -> str:
    """Wrapper around _call_llm that caches by content hash. Identical inputs
    return identical outputs without burning a paid API round-trip."""
    return _call_llm_uncached(prompt, system, max_tokens)


def _call_llm(prompt: str, system: str = "", max_tokens: int = 2048) -> str:
    """Public LLM call — hashes inputs and routes through the LRU cache."""
    cache_key = hashlib.sha256(f"{system}\0{prompt}\0{max_tokens}".encode()).hexdigest()
    return _cached_llm(cache_key, prompt, system, max_tokens)


def _call_llm_uncached(prompt: str, system: str = "", max_tokens: int = 2048) -> str:
    """Call NVIDIA NIM API, falling back to Ollama if unavailable."""
    if NVIDIA_API_KEY:
        try:
            resp = httpx.post(
                f"{NVIDIA_BASE_URL}/chat/completions",
                headers={
                    "Authorization": f"Bearer {NVIDIA_API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": DEFAULT_MODEL,
                    "messages": [
                        {"role": "system", "content": system},
                        {"role": "user", "content": prompt},
                    ],
                    "max_tokens": max_tokens,
                    "temperature": 0.3,
                },
                timeout=30.0,
            )
            resp.raise_for_status()
            return resp.json()["choices"][0]["message"]["content"]
        except Exception:
            pass  # Fall through to Ollama

    # Fallback to Ollama
    try:
        resp = httpx.post(
            f"{OLLAMA_URL}/api/chat",
            json={
                "model": os.environ.get("OLLAMA_MODEL", "llama3.1:8b"),
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": prompt},
                ],
                "stream": False,
            },
            timeout=60.0,
        )
        resp.raise_for_status()
        return resp.json()["message"]["content"]
    except Exception as e:
        return (
            f"Error: No LLM backend available. NVIDIA API error and Ollama error: {e}"
        )


def _call_nim_models() -> list[dict]:
    """List available NIM models (public endpoint, no auth required)."""
    try:
        resp = httpx.get(f"{NVIDIA_BASE_URL}/models", timeout=10.0)
        if resp.status_code == 200:
            return resp.json().get("data", [])
    except Exception:
        pass
    return []


# ── Tools ─────────────────────────────────────────────────────────────────


@mcp.tool()
def recommend_mcp(task_description: str, max_results: int = 5) -> str:
    """Analyze a task description and recommend the best MCP server(s) for it.

    Uses AI to deeply understand the request and match it to the most suitable
    MCP servers, explaining why each is recommended and how to install it.

    Args:
        task_description: Natural language description of what you want to accomplish
        max_results: Maximum number of recommendations (default 5, max 10)
    """
    max_results = min(max_results, 10)

    server_list = "\n".join(
        f"- {s['name']} [{s['category']}]: {s['description']} (tags: {', '.join(s['tags'])})"
        for s in MCP_SERVERS
    )

    system = """You are an expert MCP (Model Context Protocol) server recommender.
Analyze the user's task and recommend the most suitable MCP servers from the available list.
For each recommendation, explain: WHY it fits, HOW to use it, and the INSTALL command.
Format your response as JSON with this structure:
{"recommendations": [{"name": "...", "why": "...", "how_to_use": "...", "install": "...", "alternatives": ["..."]}]}"""

    prompt = f"""Task: {task_description}

Available MCP Servers:
{server_list}

Recommend the top {max_results} most suitable MCP servers for this task."""

    response = _call_llm(prompt, system)

    # Try to extract JSON from response, fallback to raw text
    try:
        # Find JSON block in response
        start = response.find("{")
        end = response.rfind("}") + 1
        if start >= 0 and end > start:
            return response[start:end]
    except Exception:
        pass

    return response


@mcp.tool()
def scan_mcp_registry(query: str, category: str | None = None, limit: int = 10) -> str:
    """Search for MCP servers by keyword or category. Includes both local
    knowledge base and public NIM model discovery.

    Args:
        query: Search keywords (e.g., "browser automation", "vector database")
        category: Optional category filter (browser, storage, knowledge, reasoning, web, utility, database, devops, compute, image, llm, orchestration, education)
        limit: Maximum results (default 10, max 20)
    """
    limit = min(limit, 20)
    query_lower = query.lower()

    results = []
    for s in MCP_SERVERS:
        if category and s["category"] != category:
            continue
        score = 0
        # Match against name, description, tags, category
        if query_lower in s["name"].lower():
            score += 10
        if query_lower in s["description"].lower():
            score += 5
        if query_lower in s["category"].lower():
            score += 3
        for tag in s["tags"]:
            if query_lower in tag.lower():
                score += 2
        # Also check individual query terms
        for term in query_lower.split():
            if term in s["description"].lower():
                score += 1
            for tag in s["tags"]:
                if term in tag.lower():
                    score += 1
        if score > 0:
            results.append({"score": score, **s})

    results.sort(key=lambda x: x["score"], reverse=True)
    results = results[:limit]

    # Also discover NIM models if relevant
    nim_models = []
    if any(
        kw in query_lower
        for kw in ["nvidia", "nim", "inference", "llm", "model", "gpu"]
    ):
        nim_models = _call_nim_models()[:5]

    output = {
        "query": query,
        "category": category,
        "results": results,
        "nim_models_discovered": len(nim_models),
    }

    return json.dumps(output, indent=2)


@mcp.tool()
def explain_mcp(server_name: str) -> str:
    """Get a detailed AI-generated explanation of an MCP server — what it does,
    when to use it, how it compares to alternatives, and installation instructions.

    Args:
        server_name: Name of the MCP server to explain (e.g., "playwright", "qdrant", "memory")
    """
    # Find server in knowledge base
    server = next(
        (s for s in MCP_SERVERS if s["name"].lower() == server_name.lower()), None
    )

    if not server:
        # Try partial match
        matches = [s for s in MCP_SERVERS if server_name.lower() in s["name"].lower()]
        if matches:
            server = matches[0]
        else:
            return json.dumps(
                {
                    "error": f"Server '{server_name}' not found. Use scan_mcp_registry to search.",
                    "available_servers": [s["name"] for s in MCP_SERVERS],
                },
                indent=2,
            )

    # Find alternatives in same category
    alternatives = [
        s["name"]
        for s in MCP_SERVERS
        if s["category"] == server["category"] and s["name"] != server["name"]
    ]

    system = """You are an expert MCP (Model Context Protocol) consultant. Provide detailed, practical
explanations of MCP servers. Cover: what it does, when to use it, comparison with alternatives,
installation steps, and common use cases. Be specific and actionable."""

    prompt = f"""Explain the MCP server "{server["name"]}" in detail.

Known info:
- Category: {server["category"]}
- Description: {server["description"]}
- Install: {server["install"]}
- Tags: {", ".join(server["tags"])}
- Alternatives in same category: {", ".join(alternatives) if alternatives else "none"}

Provide a comprehensive explanation including:
1. What it does (detailed)
2. When to use it (decision criteria)
3. How it compares to alternatives
4. Installation and setup steps
5. Common use cases and examples"""

    response = _call_llm(prompt, system, max_tokens=3000)
    return json.dumps(
        {
            "server": server["name"],
            "category": server["category"],
            "description": server["description"],
            "install": server["install"],
            "alternatives": alternatives,
            "ai_explanation": response,
        },
        indent=2,
    )


if __name__ == "__main__":
    # 2026: Streamable HTTP replaces SSE per MCP spec 2025-06-18.
    mcp.run(transport="streamable-http")
