# Learn-MCP: AI Engineering Knowledge Base

## Overview
AI Engineering Learning Reference MCP Server with 801 searchable references for 2026.
Running on Docker at http://127.0.0.1:8001/mcp

## MCP Server Details
- **Name**: learn-mcp
- **Type**: FastMCP Streamable HTTP Server
- **Port**: 8001
- **Transport**: Streamable HTTP
- **Vector DB**: Qdrant (http://127.0.0.1:6333)
- **Collection**: learn_refs
- **Location**: /home/francis-v/ai-stack/learn-mcp/

## Topics Available (801 Total References)

1. **mcp** (73 refs) - Model Context Protocol — servers, clients, deployment
2. **rag** (60 refs) - Retrieval-Augmented Generation — vector DBs, chunking, reranking
3. **agents** (79 refs) - Agentic AI — LangGraph, CrewAI, AutoGen, tool use
4. **fine-tuning** (59 refs) - LLM Fine-Tuning — LoRA, QLoRA, PEFT, deployment
5. **mlops** (62 refs) - MLOps & LLMOps — CI/CD, Docker, K8s, MLflow
6. **prompt-engineering** (56 refs) - Advanced Prompting — CoT, ReAct, ToT
7. **inference** (86 refs) - LLM Inference — vLLM, Ollama, SGLang, quantization
8. **claude-code** (58 refs) - Claude Code — context engineering, hooks, skills
9. **vector-db** (61 refs) - Vector Databases — Qdrant, Pinecone, Weaviate
10. **gpu-compute** (64 refs) - GPU & CUDA — PyTorch, kernels, mixed precision
11. **autonomous-agents** (64 refs) - Autonomous Systems — self-correcting loops
12. **seo** (79 refs) - SEO & Web Promotion — landing pages, Core Web Vitals

## MCP Tools

### 1. list_topics
List all available topics with descriptions.

### 2. search_references(query, topic?, limit?)
Keyword search across all references.
- **query**: Search terms
- **topic**: Optional filter by topic
- **limit**: Max results (default: 10)

### 3. get_topic_references(topic)
Get all references for a specific topic.

### 4. get_workflow(topic, workflow_name?)
Get step-by-step workflows for implementing patterns.

### 5. get_examples(topic)
Get code examples and configuration snippets.

### 6. reference_stats()
Statistics about the reference database.

### 7. index_to_qdrant()
Index all references into Qdrant for semantic search.

### 8. semantic_search(query, topic?, limit?)
Vector similarity search via Qdrant.

## How to Use

### Direct MCP Connection
The server uses Streamable HTTP transport on port 8001:
```
http://127.0.0.1:8001/mcp
```

### Example Queries
- "Show me MCP server examples"
- "How to build a RAG pipeline?"
- "LangGraph agent patterns"
- "Fine-tuning with LoRA"
- "Claude Code best practices"

## Architecture
```
learn-mcp/
  server.py          # FastMCP server
  references.json    # 801 merged references
  merge_refs.py      # Merge + validate script
  data/              # Per-topic reference files
  Dockerfile         # Python 3.14 container
```

## Reference Schema
Each reference includes:
- topic
- type (course/tutorial/pattern/tool/example)
- title
- description
- url
- tags
- difficulty (beginner/intermediate/advanced)
- workflow (optional step-by-step)
- code (optional code snippets)

## Docker Status
Container: ai-learn (running, healthy)
Image: ai-stack-learn:latest
Uptime: 5+ hours
