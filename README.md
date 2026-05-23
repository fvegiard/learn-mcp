# learn-mcp

AI Engineering Learning Reference MCP Server — 550+ searchable references for 2026.

## Topics

| Topic | Description | Refs |
|-------|-------------|------|
| `mcp` | Model Context Protocol — servers, clients, deployment | 50+ |
| `rag` | Retrieval-Augmented Generation — vector DBs, chunking, reranking | 50+ |
| `agents` | Agentic AI — LangGraph, CrewAI, AutoGen, tool use | 50+ |
| `fine-tuning` | LLM Fine-Tuning — LoRA, QLoRA, PEFT, deployment | 50+ |
| `mlops` | MLOps & LLMOps — CI/CD, Docker, K8s, MLflow | 50+ |
| `prompt-engineering` | Advanced Prompting — CoT, ReAct, ToT, structured output | 50+ |
| `inference` | LLM Inference — vLLM, Ollama, SGLang, quantization | 50+ |
| `claude-code` | Claude Code — context engineering, hooks, skills, worktrees | 50+ |
| `vector-db` | Vector Databases — Qdrant, Pinecone, Weaviate, Milvus | 50+ |
| `gpu-compute` | GPU & CUDA — PyTorch, kernels, mixed precision | 50+ |
| `autonomous-agents` | Autonomous Systems — self-correcting loops, memory, planning | 50+ |

## Tools

- `list_topics` — List all available topics
- `search_references(query, topic?, limit?)` — Keyword search across references
- `get_topic_references(topic)` — Get all references for a topic
- `get_workflow(topic, workflow_name?)` — Get step-by-step workflows
- `get_examples(topic)` — Get code examples and config snippets
- `reference_stats()` — Statistics about the reference database
- `index_to_qdrant()` — Index all references into Qdrant for semantic search
- `semantic_search(query, topic?, limit?)` — Vector similarity search via Qdrant

## Quick Start

### Docker (recommended)

```bash
docker compose up -d learn
```

### Local Development

```bash
cd ai-stack/learn-mcp
pip install "mcp[cli]>=1.6.0" qdrant-client sentence-transformers
python server.py
```

### Build References

```bash
python merge_refs.py  # Merges data/*.json into references.json
```

## Architecture

```
learn-mcp/
  server.py          # FastMCP server (SSE on port 8001)
  references.json     # Merged reference database (generated)
  merge_refs.py       # Merge + validate script
  data/               # Per-topic reference files
    mcp.json
    rag.json
    agents.json
    ...
  Dockerfile          # Python 3.14 + deps
```

## Adding References

1. Create or edit `data/<topic>.json` with new references
2. Run `python merge_refs.py` to merge and validate
3. Restart the server to pick up changes

Each reference follows this schema:

```json
{
  "topic": "mcp",
  "type": "course",
  "title": "DeepLearning.AI MCP Course",
  "description": "Build rich-context AI apps with Anthropic's MCP protocol...",
  "url": "https://deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic/",
  "tags": ["mcp", "fastmcp", "sse", "deployment"],
  "difficulty": "intermediate",
  "workflow": ["Step 1: ...", "Step 2: ..."],
  "code": "from mcp.server.fastmcp import FastMCP\n..."
}
```

## License

MIT