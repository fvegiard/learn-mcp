"""Generate INDEX.md — a single Copilot-friendly markdown index of all references.

Reads data/*.json (the source of truth), dedups by (url, title),
and writes a topic-grouped markdown file at INDEX.md.

Run: python3 build_index.py
"""

from __future__ import annotations
import json
import pathlib
import sys
from collections import OrderedDict

ROOT = pathlib.Path(__file__).parent
DATA = ROOT / "data"
OUT = ROOT / "INDEX.md"

TOPIC_ORDER = [
    "mcp",
    "rag",
    "agents",
    "fine-tuning",
    "mlops",
    "prompt-engineering",
    "inference",
    "claude-code",
    "vector-db",
    "gpu-compute",
    "autonomous-agents",
    "seo",
]
TOPIC_DESCRIPTIONS = {
    "mcp": "Model Context Protocol — servers, clients, deployment patterns",
    "rag": "Retrieval-Augmented Generation — vector DBs, chunking, embeddings, reranking",
    "agents": "Agentic AI — LangGraph, CrewAI, AutoGen, multi-agent systems, tool use",
    "fine-tuning": "LLM Fine-Tuning — LoRA, QLoRA, PEFT, dataset prep, evaluation",
    "mlops": "MLOps & LLMOps — CI/CD, Docker, K8s, MLflow, model serving",
    "prompt-engineering": "Advanced prompting — CoT, ReAct, ToT, system prompts, constitutional AI",
    "inference": "LLM inference — vLLM, Ollama, SGLang, llama.cpp, quantization, batching",
    "claude-code": "Claude Code — context engineering, hooks, skills, MCP servers, agents",
    "vector-db": "Vector databases — Qdrant, Pinecone, Weaviate, Milvus, pgvector",
    "gpu-compute": "GPU & CUDA — PyTorch, CUDA kernels, mixed precision, FlashAttention",
    "autonomous-agents": "Autonomous systems — self-correcting loops, planning, long-horizon tasks",
    "seo": "SEO & web promotion — landing pages, Core Web Vitals, structured data, sitemaps",
}


def main() -> int:
    if not DATA.is_dir():
        print(f"ERROR: {DATA} not found", file=sys.stderr)
        return 1

    by_topic: OrderedDict[str, list[dict]] = OrderedDict()
    seen: set[tuple[str, str]] = set()
    total = 0

    for topic in TOPIC_ORDER:
        f = DATA / f"{topic}.json"
        if not f.exists():
            print(f"  ! missing {f}, skipping", file=sys.stderr)
            continue
        refs = json.loads(f.read_text())
        unique = []
        for ref in refs:
            key = (ref.get("url", ""), ref.get("title", ""))
            if key in seen:
                continue
            seen.add(key)
            unique.append(ref)
            total += 1
        by_topic[topic] = unique
        print(f"  {topic:24s} {len(unique):4d} refs")

    lines: list[str] = []
    lines.append("# learn-mcp Knowledge Index")
    lines.append("")
    lines.append(
        f"**{total} curated references** across **{len(by_topic)} topics** "
        "for AI/ML engineering in 2026. Source of truth: `data/<topic>.json` files."
    )
    lines.append("")
    lines.append(
        "This index is auto-generated from the per-topic JSON files by "
        "`build_index.py`. Re-run after editing `data/` to refresh."
    )
    lines.append("")
    lines.append("## Topics")
    lines.append("")
    for topic, refs in by_topic.items():
        anchor = topic.lower()
        lines.append(
            f"- [`{topic}`](#{anchor}) — {TOPIC_DESCRIPTIONS.get(topic, '')} "
            f"({len(refs)} refs)"
        )
    lines.append("")
    lines.append("---")
    lines.append("")

    for topic, refs in by_topic.items():
        lines.append(f"## {topic}")
        lines.append("")
        if topic in TOPIC_DESCRIPTIONS:
            lines.append(f"*{TOPIC_DESCRIPTIONS[topic]}*")
            lines.append("")
        lines.append(f"**{len(refs)} references**")
        lines.append("")
        lines.append("| # | Title | Type | URL |")
        lines.append("|---|-------|------|-----|")
        for i, ref in enumerate(refs, 1):
            title = (ref.get("title") or "").replace("|", "\\|").strip()
            url = (ref.get("url") or "").strip()
            kind = (ref.get("type") or ref.get("category") or "—").strip()
            lines.append(f"| {i} | {title[:120]} | {kind} | {url} |")
        lines.append("")

    OUT.write_text("\n".join(lines))
    print(f"\nWrote {OUT} ({OUT.stat().st_size:,} bytes, {total} unique refs)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
