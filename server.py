"""AI Engineering Learning Reference MCP Server.

Serves a searchable knowledge base of 2026 AI/ML engineering courses,
patterns, workflows, and code examples. Backed by Qdrant vector DB
for semantic search across all references.
"""

from __future__ import annotations

import json
import os
import re
import threading
from mcp.server.fastmcp import FastMCP

# Must bind 0.0.0.0 inside the container for docker-proxy + cross-container
# (ai-recommender) access. Host exposure is limited by the compose
# `127.0.0.1:8001:8001` port prefix.
mcp = FastMCP("learn", host="0.0.0.0", port=8001)

QDRANT_URL = os.environ.get("QDRANT_URL", "http://127.0.0.1:6333")
COLLECTION = "learn_refs"

# ── Topics and their reference databases ──────────────────────────────────

TOPICS = {
    "mcp": "Model Context Protocol — building, deploying, and orchestrating MCP servers and clients",
    "rag": "Retrieval-Augmented Generation — vector DBs, chunking, embeddings, reranking, evaluation",
    "agents": "Agentic AI — LangGraph, CrewAI, AutoGen, multi-agent systems, tool use, planning",
    "fine-tuning": "LLM Fine-Tuning — LoRA, QLoRA, PEFT, dataset prep, evaluation, deployment",
    "mlops": "MLOps & LLMOps — CI/CD, Docker, K8s, MLflow, monitoring, deployment pipelines",
    "prompt-engineering": "Advanced Prompt Engineering — CoT, ReAct, ToT, structured output, meta-prompting",
    "inference": "LLM Inference Serving — vLLM, Ollama, TGI, SGLang, quantization, production",
    "claude-code": "Claude Code Workflows — context engineering, CLAUDE.md, subagents, hooks, skills",
    "vector-db": "Vector Databases — Qdrant, Pinecone, Weaviate, Milvus, ChromaDB, HNSW, hybrid search",
    "gpu-compute": "GPU & CUDA Programming — PyTorch, CUDA kernels, mixed precision, memory optimization",
    "autonomous-agents": "Autonomous & Agentic Systems — self-correcting loops, tool use, memory, planning",
    "seo": "SEO & Web Promotion — landing pages, design psychology, Core Web Vitals, open-source marketing, analytics",
}

# ── Reference data ───────────────────────────────────────────────────────

REFERENCES: list[dict] = []


def _load_references():
    """Load references from merged JSON or individual topic files."""
    global REFERENCES
    base = os.path.dirname(os.path.abspath(__file__))
    merged = os.path.join(base, "references.json")
    if os.path.exists(merged):
        try:
            with open(merged) as f:
                REFERENCES = json.load(f)
            return
        except (json.JSONDecodeError, OSError) as e:
            print(f"Warning: Failed to load {merged}: {e}")
    # Fallback: load individual topic files from data/
    data_dir = os.path.join(base, "data")
    if not os.path.isdir(data_dir):
        print(f"Warning: No data directory at {data_dir}")
        return
    for fname in sorted(os.listdir(data_dir)):
        if fname.endswith(".json"):
            try:
                with open(os.path.join(data_dir, fname)) as f:
                    REFERENCES.extend(json.load(f))
            except (json.JSONDecodeError, OSError) as e:
                print(f"Warning: Failed to load {fname}: {e}")


_load_references()

# ── Lazy-loaded SentenceTransformer model ────────────────────────────────

_MODEL = None


_MODEL_LOCK = threading.Lock()


def _get_model():
    """Lazy-load and cache the SentenceTransformer model (thread-safe)."""
    global _MODEL
    if _MODEL is None:
        with _MODEL_LOCK:
            if _MODEL is None:
                from sentence_transformers import SentenceTransformer

                _MODEL = SentenceTransformer("all-MiniLM-L6-v2")
    return _MODEL


# Background pre-warm: load the embedding model at startup so the first
# semantic_search / index_to_qdrant call doesn't pay a 3-5s cold-start.
threading.Thread(target=_get_model, daemon=True, name="model-prewarm").start()


# ── Tools ─────────────────────────────────────────────────────────────────


@mcp.tool()
def list_topics() -> str:
    """List all available learning topics with descriptions."""
    return json.dumps({k: v for k, v in TOPICS.items()}, indent=2)


@mcp.tool()
def search_references(query: str, topic: str | None = None, limit: int = 10) -> str:
    """Search learning references by keyword or semantic similarity.

    Args:
        query: Natural language search query
        topic: Optional topic filter (mcp, rag, agents, fine-tuning, mlops,
               prompt-engineering, inference, claude-code, vector-db,
               gpu-compute, autonomous-agents, seo)
        limit: Maximum results to return (default 10, max 50)
    """
    if topic and topic not in TOPICS:
        return json.dumps(
            {"error": f"Unknown topic '{topic}'. Use list_topics to see valid topics."},
            indent=2,
        )

    limit = min(limit, 50)
    results = []
    # Compile patterns once per query (not once per ref) — saves ~720 regex
    # compilations on every search call.
    patterns = [
        re.compile(r"\b" + re.escape(term) + r"\b") for term in query.lower().split()
    ]

    for ref in REFERENCES:
        if topic and ref.get("topic") != topic:
            continue
        searchable = " ".join(
            v if isinstance(v, str) else " ".join(v) if isinstance(v, list) else ""
            for v in ref.values()
        ).lower()
        if all(p.search(searchable) for p in patterns):
            results.append(ref)
            if len(results) >= limit:
                break

    if not results:
        return json.dumps(
            {"message": f"No references found for '{query}'", "total": 0}, indent=2
        )

    return json.dumps({"total": len(results), "results": results}, indent=2)


@mcp.tool()
def get_topic_references(topic: str) -> str:
    """Get all references for a specific topic.

    Args:
        topic: Topic name (mcp, rag, agents, fine-tuning, mlops,
               prompt-engineering, inference, claude-code, vector-db,
               gpu-compute, autonomous-agents, seo)
    """
    if topic not in TOPICS:
        return json.dumps(
            {"error": f"Unknown topic '{topic}'. Use list_topics to see valid topics."},
            indent=2,
        )

    refs = [r for r in REFERENCES if r.get("topic") == topic]
    return json.dumps(
        {"topic": topic, "total": len(refs), "references": refs}, indent=2
    )


@mcp.tool()
def get_workflow(topic: str, workflow_name: str | None = None) -> str:
    """Get step-by-step workflows and procedures for a topic.

    Args:
        topic: Topic name (mcp, rag, agents, fine-tuning, mlops,
               prompt-engineering, inference, claude-code, vector-db,
               gpu-compute, autonomous-agents, seo)
        workflow_name: Optional specific workflow name to retrieve
    """
    if topic not in TOPICS:
        return json.dumps(
            {"error": f"Unknown topic '{topic}'. Use list_topics to see valid topics."},
            indent=2,
        )

    workflows = [
        r for r in REFERENCES if r.get("topic") == topic and r.get("type") == "workflow"
    ]

    if workflow_name:
        workflows = [
            w for w in workflows if workflow_name.lower() in w.get("title", "").lower()
        ]
        if not workflows:
            return json.dumps(
                {"error": f"No workflow '{workflow_name}' found in topic '{topic}'"},
                indent=2,
            )

    return json.dumps({"topic": topic, "workflows": workflows}, indent=2)


@mcp.tool()
def get_examples(topic: str) -> str:
    """Get code examples and configuration snippets for a topic.

    Args:
        topic: Topic name (mcp, rag, agents, fine-tuning, mlops,
               prompt-engineering, inference, claude-code, vector-db,
               gpu-compute, autonomous-agents, seo)
    """
    if topic not in TOPICS:
        return json.dumps(
            {"error": f"Unknown topic '{topic}'. Use list_topics to see valid topics."},
            indent=2,
        )

    examples = [
        r for r in REFERENCES if r.get("topic") == topic and r.get("type") == "example"
    ]
    return json.dumps({"topic": topic, "examples": examples}, indent=2)


@mcp.tool()
def reference_stats() -> str:
    """Get statistics about the reference database."""
    by_topic = {}
    by_type = {}
    for ref in REFERENCES:
        t = ref.get("topic", "unknown")
        ty = ref.get("type", "unknown")
        by_topic[t] = by_topic.get(t, 0) + 1
        by_type[ty] = by_type.get(ty, 0) + 1

    return json.dumps(
        {
            "total_references": len(REFERENCES),
            "by_topic": by_topic,
            "by_type": by_type,
        },
        indent=2,
    )


# ── Qdrant integration ───────────────────────────────────────────────────


@mcp.tool()
def index_to_qdrant() -> str:
    """Index all references into Qdrant vector database for semantic search.
    Requires Qdrant running at QDRANT_URL (default: http://127.0.0.1:6333).
    Idempotent: recreates the collection on each call.
    """
    try:
        from qdrant_client import QdrantClient
        from qdrant_client.models import Distance, VectorParams, PointStruct
    except ImportError:
        return json.dumps(
            {"error": "qdrant-client not installed. Run: pip install qdrant-client"},
            indent=2,
        )

    client = QdrantClient(url=QDRANT_URL)

    # Recreate collection for clean indexing (idempotent)
    collections = [c.name for c in client.get_collections().collections]
    if COLLECTION in collections:
        client.delete_collection(collection_name=COLLECTION)
    client.create_collection(
        collection_name=COLLECTION,
        vectors_config=VectorParams(size=384, distance=Distance.COSINE),
    )

    model = _get_model()

    points = []
    for i, ref in enumerate(REFERENCES):
        text = f"{ref.get('title', '')} {ref.get('description', '')} {' '.join(ref.get('tags', []))}"
        vector = model.encode(text).tolist()
        points.append(PointStruct(id=i, vector=vector, payload=ref))

    client.upsert(collection_name=COLLECTION, points=points)
    return json.dumps({"indexed": len(points), "collection": COLLECTION}, indent=2)


@mcp.tool()
def semantic_search(query: str, topic: str | None = None, limit: int = 10) -> str:
    """Semantic search across references using Qdrant vector similarity.

    Args:
        query: Natural language search query
        topic: Optional topic to filter results
        limit: Maximum results (default 10, max 50)
    """
    if topic and topic not in TOPICS:
        return json.dumps(
            {"error": f"Unknown topic '{topic}'. Use list_topics to see valid topics."},
            indent=2,
        )

    try:
        from qdrant_client import QdrantClient
        from qdrant_client.models import FieldCondition, Filter, MatchValue
    except ImportError:
        return json.dumps(
            {
                "error": "Install dependencies: pip install qdrant-client sentence-transformers"
            },
            indent=2,
        )

    client = QdrantClient(url=QDRANT_URL)
    model = _get_model()
    vector = model.encode(query).tolist()

    filter_obj = None
    if topic:
        filter_obj = Filter(
            must=[FieldCondition(key="topic", match=MatchValue(value=topic))]
        )

    results = client.query_points(
        collection_name=COLLECTION,
        query=vector,
        query_filter=filter_obj,
        limit=min(limit, 50),
    ).points

    hits = [{"score": hit.score, **hit.payload} for hit in results]
    return json.dumps({"query": query, "total": len(hits), "results": hits}, indent=2)


def _auto_reindex():
    """Reindex Qdrant if the collection is empty (e.g. after a container restart)."""
    try:
        from qdrant_client import QdrantClient

        client = QdrantClient(url=QDRANT_URL)
        if (
            not client.collection_exists(COLLECTION)
            or client.count(COLLECTION).count == 0
        ):
            index_to_qdrant()
    except Exception:
        pass


threading.Thread(target=_auto_reindex, daemon=True, name="qdrant-auto-reindex").start()


def main():
    import sys

    transport = "streamable-http"
    if "--transport" in sys.argv:
        idx = sys.argv.index("--transport")
        if idx + 1 < len(sys.argv):
            transport = sys.argv[idx + 1]
    elif len(sys.argv) > 1 and sys.argv[1] in ("stdio", "streamable-http"):
        transport = sys.argv[1]
    if transport == "stdio":
        mcp.run(transport="stdio")
    else:
        mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()
