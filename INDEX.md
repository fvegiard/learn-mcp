# learn-mcp Knowledge Index

**801 curated references** across **12 topics** for AI/ML engineering in 2026. Source of truth: `data/<topic>.json` files.

This index is auto-generated from the per-topic JSON files by `build_index.py`. Re-run after editing `data/` to refresh.

## Topics

- [`mcp`](#mcp) — Model Context Protocol — servers, clients, deployment patterns (73 refs)
- [`rag`](#rag) — Retrieval-Augmented Generation — vector DBs, chunking, embeddings, reranking (60 refs)
- [`agents`](#agents) — Agentic AI — LangGraph, CrewAI, AutoGen, multi-agent systems, tool use (79 refs)
- [`fine-tuning`](#fine-tuning) — LLM Fine-Tuning — LoRA, QLoRA, PEFT, dataset prep, evaluation (59 refs)
- [`mlops`](#mlops) — MLOps & LLMOps — CI/CD, Docker, K8s, MLflow, model serving (63 refs)
- [`prompt-engineering`](#prompt-engineering) — Advanced prompting — CoT, ReAct, ToT, system prompts, constitutional AI (56 refs)
- [`inference`](#inference) — LLM inference — vLLM, Ollama, SGLang, llama.cpp, quantization, batching (86 refs)
- [`claude-code`](#claude-code) — Claude Code — context engineering, hooks, skills, MCP servers, agents (58 refs)
- [`vector-db`](#vector-db) — Vector databases — Qdrant, Pinecone, Weaviate, Milvus, pgvector (61 refs)
- [`gpu-compute`](#gpu-compute) — GPU & CUDA — PyTorch, CUDA kernels, mixed precision, FlashAttention (63 refs)
- [`autonomous-agents`](#autonomous-agents) — Autonomous systems — self-correcting loops, planning, long-horizon tasks (64 refs)
- [`seo`](#seo) — SEO & web promotion — landing pages, Core Web Vitals, structured data, sitemaps (79 refs)

---

## mcp

*Model Context Protocol — servers, clients, deployment patterns*

**73 references**

| # | Title | Type | URL |
|---|-------|------|-----|
| 1 | MCP Specification (2025-11-25) — Protocol Fundamentals | course | https://modelcontextprotocol.io/specification/2025-11-25 |
| 2 | MCP Architecture Overview — Hosts, Clients, and Servers | course | https://modelcontextprotocol.io/docs/learn |
| 3 | MCP Transport Mechanisms — stdio and Streamable HTTP | course | https://modelcontextprotocol.io/specification/2025-06-18/basic/transports |
| 4 | MCP Authorization — OAuth 2.1 Security Framework | course | https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization |
| 5 | MCP Server Quickstart — Build a Weather Server (Official) | tutorial | https://github.com/modelcontextprotocol/docs/blob/main/quickstart/server.mdx |
| 6 | MCP Client Quickstart — Connect to Servers (Official) | tutorial | https://github.com/modelcontextprotocol/docs/blob/main/quickstart/client.mdx |
| 7 | Microsoft MCP for Beginners — Multi-Language Course | tutorial | https://github.com/microsoft/mcp-for-beginners |
| 8 | MCP Inspector — Official Debugging and Testing Tool | tool | https://github.com/modelcontextprotocol/inspector |
| 9 | MCP Python SDK — Building Servers (Official Documentation) | course | https://modelcontextprotocol.github.io/python-sdk/server/ |
| 10 | MCP TypeScript SDK — Server Quickstart and API Reference | course | https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/server-quickstart.md |
| 11 | Build a Secure MCP Server in TypeScript from Scratch | tutorial | https://rebeccamdeprey.com/blog/secure-mcp-server |
| 12 | FastMCP Python Server — Minimal Tool, Resource, and Prompt | example | https://modelcontextprotocol.github.io/python-sdk/server/ |
| 13 | TypeScript MCP Server with Streamable HTTP Transport | example | https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/server-quickstart.md |
| 14 | Python MCP Client — Connecting to a Server and Calling Tools | example | https://github.com/modelcontextprotocol/python-sdk |
| 15 | Python MCP Client — Streamable HTTP Transport with OAuth | example | https://github.com/modelcontextprotocol/python-sdk |
| 16 | TypeScript MCP Client — Connecting to Remote and Local Servers | example | https://github.com/modelcontextprotocol/typescript-sdk/blob/HEAD/docs/client.md |
| 17 | MCP TypeScript SDK — Client Development Guide | course | https://github.com/modelcontextprotocol/typescript-sdk/blob/HEAD/docs/client.md |
| 18 | Building a Python MCP Client — Real Python Deep Dive | tutorial | https://realpython.com/python-mcp-client/ |
| 19 | VS Code MCP Integration — Server Configuration and Copilot | course | https://github.com/microsoft/vscode-docs/blob/main/docs/copilot/customization/mcp-servers.md |
| 20 | GitHub MCP Server — Official GitHub Integration | tool | https://github.com/github/github-mcp-server |
| 21 | Deploy MCP Servers to Production with Docker and Streamable HTTP | tutorial | https://systemprompt.io/guides/mcp-servers-production-deployment |
| 22 | MCP Streamable HTTP Transport — SSE Migration to Production | pattern | https://apigene.ai/blog/mcp-streamable-http |
| 23 | Deploy an MCP Server to Google Cloud Run | workflow | https://cloud.google.com/run/docs/host-mcp-servers |
| 24 | Claude Code Plugins — Skills, Hooks, MCP, and Worktrees | course | https://code.claude.com/docs/en/plugins-reference |
| 25 | Claude Code Full Stack — MCP, Skills, Subagents, and Hooks Explained | pattern | https://alexop.dev/posts/understanding-claude-code-full-stack/ |
| 26 | Claude Code Hooks Reference — Lifecycle Events and Handler Types | course | https://code.claude.com/docs/en/hooks.md |
| 27 | MCP Tools vs Resources vs Prompts — Decision Framework | pattern | https://engineersofai.com/docs/agentic-ai/model-context-protocol/MCP-Tools-Resources-Prompts |
| 28 | MCP Tool Design Patterns — Building Agent-Friendly, Composable Tools | pattern | https://chatforest.com/guides/mcp-tool-design-patterns/ |
| 29 | Awesome MCP Best Practices — Curated Production Guidelines | pattern | https://github.com/lirantal/awesome-mcp-best-practices |
| 30 | MCP Server Design Checklist — AgentPatterns.ai | pattern | https://agentpatterns.ai/tool-engineering/mcp-server-design/ |
| 31 | Composable Tools for Enterprise MCP — Nine Design Patterns | pattern | https://dev.to/zaynelt/designing-composable-tools-for-enterprise-mcp-from-theory-to-practice-3df |
| 32 | Build and Deploy a FastMCP Server with Docker | workflow | https://www.firecrawl.dev/blog/fastmcp-tutorial-building-mcp-servers-python |
| 33 | Build a Custom MCP Client in Python with LLM Integration | workflow | https://github.com/modelcontextprotocol/docs/blob/main/quickstart/client.mdx |
| 34 | Configure MCP Servers for VS Code Copilot | workflow | https://github.com/microsoft/vscode-docs/blob/main/docs/copilot/reference/mcp-configuration.md |
| 35 | Set Up Claude Code Hooks with MCP Tool Integration | workflow | https://code.claude.com/docs/en/hooks.md |
| 36 | Debug an MCP Server with MCP Inspector | workflow | https://github.com/modelcontextprotocol/inspector |
| 37 | mcp-agent SDK — Composable Workflow Patterns for Multi-Agent Systems | course | https://github.com/lastmile-ai/mcp-agent |
| 38 | MCP Agent Orchestration — Chaining, Handoffs, and Multi-Agent Patterns | pattern | https://www.getknit.dev/blog/advanced-mcp-agent-orchestration-chaining-and-handoffs |
| 39 | Microsoft Agent Framework — MCP-Driven Multi-Agent Patterns | pattern | https://techcommunity.microsoft.com/blog/azuredevcommunityblog/orchestrating-multi-agent-intelligence-mcp-driven-patterns-in-agent-framework/4462150 |
| 40 | mcp-orchestrator — TypeScript Composition Library | tool | https://github.com/mrorigo/mcp-orchestrator |
| 41 | Advanced MCP Server Patterns — Circuit Breakers, Caching, and Error Handling | pattern | https://www.mcpstack.org/learn/advanced-mcp-patterns |
| 42 | MCP Tool Creation Patterns and Best Practices | pattern | https://www.grizzlypeaksoftware.com/library/mcp-tool-creation-patterns-and-best-practices-sgph5f29 |
| 43 | MCP Gateway and Registry — Enterprise Production Platform | tool | https://github.com/agentic-community/mcp-gateway-registry |
| 44 | Centralized MCP Registry Architecture — Multi-Tenancy and Dynamic Discovery | pattern | https://www.truefoundry.com/de/blog/centralized-mcp-registry-architecture |
| 45 | FastMCP 3.0 — Provider Architecture and Transform System | course | https://gofastmcp.com/servers/providers/overview |
| 46 | Building MCP Servers with Python — freeCodeCamp Guide | tutorial | https://www.freecodecamp.org/news/how-to-build-your-own-mcp-server-with-python/ |
| 47 | Smithery — MCP Server Discovery and Registry Platform | tool | https://smithery.ai/docs |
| 48 | MCP 2026-07-28 Specification Release Candidate — Stateless Protocol Core | course | https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/ |
| 49 | Claude Code Skills — Unified Commands and Auto-Activation | course | https://code.claude.com/docs/en/plugins |
| 50 | FastMCP 3.0 Provider Composition — Mounting and Proxying Servers | example | https://gofastmcp.com/servers/providers/overview |
| 51 | SudoAll.com MCP Protocol Course (55 Lessons) | course | https://sudoall.com/mcp-protocol-course-intro/ |
| 52 | Apify MCP Server Handbook 2026 | tutorial | https://use-apify.com/blog/mcp-server-handbook-2026 |
| 53 | env.dev: How to Build an MCP Server | tutorial | https://env.dev/guides/how-to-build-an-mcp-server |
| 54 | LogRocket: How to Build an MCP Server with Node.js | tutorial | https://blog.logrocket.com/how-to-build-mcp-server-nodejs/ |
| 55 | MCP: Model Context Protocol Book (cloudstreet-dev, CC0) | book | https://github.com/cloudstreet-dev/MCP-Model-Context-Protocol |
| 56 | awesome-mcp-servers (punkpeye) | tool | https://github.com/punkpeye/awesome-mcp-servers |
| 57 | FastMCP | tool | https://github.com/PrefectHQ/fastmcp |
| 58 | MCP Toolbox for Databases (Google) | tool | https://github.com/googleapis/mcp-toolbox |
| 59 | Figma Context MCP | tool | https://github.com/GLips/Figma-Context-MCP |
| 60 | MCP Chrome | tool | https://github.com/hangwin/mcp-chrome |
| 61 | PAL MCP Server | tool | https://github.com/BeehiveInnovations/pal-mcp-server |
| 62 | mcp-use | tool | https://github.com/mcp-use/mcp-use |
| 63 | MCP Registry | tool | https://github.com/modelcontextprotocol/registry |
| 64 | GhidraMCP | tool | https://github.com/LaurieWired/GhidraMCP |
| 65 | GitMCP | tool | https://github.com/idosal/git-mcp |
| 66 | Kreuzberg - Polyglot Document Intelligence | tool | https://github.com/kreuzberg-dev/kreuzberg |
| 67 | Firecrawl MCP Server | tool | https://github.com/firecrawl/firecrawl-mcp-server |
| 68 | Desktop Commander MCP | tool | https://github.com/wonderwhy-er/DesktopCommanderMCP |
| 69 | XcodeBuildMCP | tool | https://github.com/getsentry/XcodeBuildMCP |
| 70 | MCP Atlassian | tool | https://github.com/sooperset/mcp-atlassian |
| 71 | HexStrike AI MCP Agents | tool | https://github.com/0x4m4/hexstrike-ai |
| 72 | Browser MCP | tool | https://github.com/BrowserMCP/mcp |
| 73 | awesome-mcp-servers (appcypher) | pattern | https://github.com/appcypher/awesome-mcp-servers |

## rag

*Retrieval-Augmented Generation — vector DBs, chunking, embeddings, reranking*

**60 references**

| # | Title | Type | URL |
|---|-------|------|-----|
| 1 | DeepLearning.AI Retrieval Augmented Generation (RAG) Course | course | https://www.deeplearning.ai/courses/retrieval-augmented-generation |
| 2 | Boot.dev Learn Retrieval Augmented Generation | course | https://www.boot.dev/courses/learn-retrieval-augmented-generation |
| 3 | Coursera Generative AI Applications with RAG and LangChain | course | https://www.coursera.org/learn/project-generative-ai-applications-with-rag-and-langchain |
| 4 | Educative.io Fundamentals of RAG with LangChain | course | https://www.educative.io/courses/rag-llm |
| 5 | LangChain Official RAG Agent Tutorial | tutorial | https://docs.langchain.com/oss/python/langchain/rag |
| 6 | Qdrant Vector Database | tool | https://qdrant.tech/documentation/ |
| 7 | Weaviate Vector Database | tool | https://weaviate.io/developers/weaviate |
| 8 | ChromaDB Embedded Vector Database | tool | https://www.trychroma.com/docs |
| 9 | Vector Database Selection Decision Framework | pattern | https://genai.qa/blog/pinecone-vs-weaviate-vs-qdrant-vs-chroma-vs-milvus/ |
| 10 | Build a Basic RAG Pipeline End-to-End | workflow | https://docs.langchain.com/oss/python/langchain/rag |
| 11 | Set Up Qdrant Hybrid Search with Dense and Sparse Vectors | workflow | https://qdrant.tech/documentation/tutorials-develop/hybrid-search-fastembed/ |
| 12 | Evaluate RAG Quality with RAGAS Metrics | workflow | https://docs.ragas.io/en/stable/tutorials/rag/ |
| 13 | Build a GraphRAG Pipeline with Microsoft GraphRAG | workflow | https://microsoft-graphrag.mintlify.app/quickstart |
| 14 | Deploy Production RAG Monitoring with OpenTelemetry and Langfuse | workflow | https://langfuse.com/blog/2025-10-28-rag-observability-and-evals |
| 15 | LangChain RAG Agent with Tool-Based Retrieval | example | https://docs.langchain.com/oss/python/langchain/rag |
| 16 | Qdrant Hybrid Search with RRF Fusion | example | https://qdrant.tech/documentation/tutorials-develop/hybrid-search-fastembed/ |
| 17 | RAGAS RAG Evaluation Pipeline | example | https://docs.ragas.io/en/stable/tutorials/rag/ |
| 18 | SPLADE Sparse Retrieval with Sentence Transformers | example | https://sbert.net/examples/sparse_encoder/training/retrievers/README.html |
| 19 | LlamaIndex Semantic Chunking Pipeline | example | https://developers.llamaindex.ai/python/examples/node_parsers/semantic_chunking/ |
| 20 | Advanced Retrieval: Hybrid Search with RRF and DBSF Fusion | pattern | https://qdrant.tech/articles/hybrid-search/ |
| 21 | Cascading Retrieval-Reranking Pipeline (SPLADE to Cross-Encoder to LLM) | pattern | https://arxiv.org/abs/2403.10407 |
| 22 | ColBERT Late Interaction Reranking Pattern | pattern | https://github.com/stanford-futuredata/ColBERT |
| 23 | Recursive Semantic Chunking (RSC) Pattern | pattern | https://aclanthology.org/2025.icnlsp-1.15.pdf |
| 24 | Pseudo-Instruction Chunking (PIC) Pattern | pattern | https://aclanthology.org/2025.findings-acl.422.pdf |
| 25 | Multi-Granularity Chunking with Parent-Child Retrieval | pattern | https://arxiv.org/abs/2501.09940 |
| 26 | Fixed-Size vs Recursive vs Semantic Chunking Decision Guide | pattern | https://www.onsomble.ai/blog/chunking-strategies-compared |
| 27 | OpenAI Embeddings (text-embedding-3-small/large) | tool | https://platform.openai.com/docs/guides/embeddings |
| 28 | BGE-M3 Multilingual Embedding Model | tool | https://huggingface.co/BAAI/bge-m3 |
| 29 | Embedding Model Selection Decision Framework | pattern | https://app.ailog.fr/en/blog/guides/choosing-embedding-models |
| 30 | RAGAS Evaluation Framework | tool | https://docs.ragas.io/en/stable/ |
| 31 | DeepEval RAG Evaluation and CI/CD | tool | https://docs.confident-ai.com/ |
| 32 | Separate Retrieval and Generation Scoring | pattern | https://atlan.com/know/llm-evaluation-frameworks-compared/ |
| 33 | Langfuse Open-Source RAG Observability | tool | https://langfuse.com/docs |
| 34 | Production RAG Cost Optimization Playbook | pattern | https://brlikhon.engineer/blog/production-rag-architecture-that-scales-vector-databases-chunking-strategies-and-cost-optimization-for-2025 |
| 35 | Production RAG Monitoring: Per-Stage Latency Breakdown and SLOs | pattern | https://markaicode.com/architecture/prometheus-rag-architecture/ |
| 36 | RAG Data Versioning and Regression Testing | pattern | https://pub.towardsai.net/rag-in-practice-exploring-versioning-observability-and-evaluation-in-production-systems-85dc28e1d9a8 |
| 37 | Microsoft GraphRAG | tool | https://github.com/microsoft/GraphRAG |
| 38 | Neo4j GraphRAG Python Library | tool | https://github.com/neo4j/neo4j-graphrag-python |
| 39 | GraphRAG vs Vector RAG Decision Framework | pattern | https://microsoft-graphrag.mintlify.app/quickstart |
| 40 | Microsoft GraphRAG Python API: Index, Query, and Search | example | https://microsoft-graphrag.mintlify.app/guides/python-api |
| 41 | RAG in Production with Haystack | book | https://www.oreilly.com/library/view/retrieval-augmented-generation-in/9781098165161/ |
| 42 | Mastering Retrieval-Augmented Generation | book | https://www.oreilly.com/library/view/mastering-retrieval-augmented-generation/9798868818080/ |
| 43 | Hands-On RAG for Production | book | https://www.oreilly.com/library/view/hands-on-rag-for/9798341621701/ |
| 44 | RAG-Critic: Automated Error Identification and Correction in RAG | tutorial | https://aclanthology.org/2025.acl-long.179.pdf |
| 45 | R3-RAG: Reinforcement Learning for Step-by-Step Retrieval | pattern | https://aclanthology.org/2025.findings-emnlp.554.pdf |
| 46 | CoRAG: Chain-of-Retrieval Augmented Generation | pattern | https://arxiv.org/abs/2505.02811 |
| 47 | SIM-RAG: Self-Practicing When to Stop Retrieving | pattern | https://arxiv.org/abs/2501.14342 |
| 48 | UniversalRAG: Modality-Aware Routing for Multimodal Retrieval | pattern | https://arxiv.org/abs/2504.20734 |
| 49 | mRAG Design Space for Multimodal Retrieval-Augmented Generation | pattern | https://arxiv.org/abs/2505.24073 |
| 50 | Multimodal RAG Survey: Scaling Beyond Context for Document Understanding | tutorial | https://arxiv.org/abs/2510.15253 |
| 51 | Udacity: Large Language Models (LLMs) and RAG | course | https://www.udacity.com/course/large-language-models-llms-and-rag--cd13318 |
| 52 | Activeloop Gen AI 360: RAG Course (Free) | course | https://learn.activeloop.ai/courses/rag |
| 53 | Cognita (TrueFoundry) | tool | https://github.com/truefoundry/cognita |
| 54 | RAG Web UI | tool | https://github.com/rag-web-ui/rag-web-ui |
| 55 | RAGHub | pattern | https://github.com/Andrew-Jang/RAGHub |
| 56 | Simple Local RAG (mrdbourke) | pattern | https://github.com/mrdbourke/simple-local-rag |
| 57 | MODULAR-RAG-MCP-SERVER | tool | https://github.com/jerry-ai-dev/MODULAR-RAG-MCP-SERVER |
| 58 | Cloudflare RAG | pattern | https://github.com/RafalWilinski/cloudflare-rag |
| 59 | raggo | tool | https://github.com/teilomillet/raggo |
| 60 | Azure RAG Design and Evaluation | pattern | https://github.com/Azure-Samples/Design-and-evaluation-of-RAG-solutions |

## agents

*Agentic AI — LangGraph, CrewAI, AutoGen, multi-agent systems, tool use*

**79 references**

| # | Title | Type | URL |
|---|-------|------|-----|
| 1 | Anthropic: Building Effective Agents | tutorial | https://www.anthropic.com/engineering/building-effective-agents |
| 2 | ReAct Pattern - Reasoning and Acting in Language Models | tutorial | https://tutorialq.com/ai/dl-applications/react-pattern |
| 3 | Four Single-Agent Patterns: ReAct, Plan-and-Execute, ReWOO, Reflexion | pattern | https://theaiengineer.substack.com/p/the-4-single-agent-patterns |
| 4 | LangGraph Official: Human-in-the-Loop Quickstart | tutorial | https://langchain-ai.github.io/langgraph/tutorials/get-started/4-human-in-the-loop/ |
| 5 | LangGraph Human-in-the-Loop: Interrupt Patterns in Python | tutorial | https://turion.ai/blog/langgraph-human-in-the-loop-interrupt-tutorial/ |
| 6 | LangGraph ReAct Agent: Build from Scratch | example | https://machinelearningplus.com/gen-ai/langgraph-react-agent-from-scratch/ |
| 7 | LangGraph: Build a ReAct Agent with Human-in-the-Loop Approval | workflow | https://machinelearningmastery.com/building-a-human-in-the-loop-approval-gate-for-autonomous-agents/ |
| 8 | CrewAI Official Documentation | tutorial | https://docs.crewai.com/ |
| 9 | CrewAI: Build Your First Crew | tutorial | https://blog.crewai.com/getting-started-with-crewai-build-your-first-crew/ |
| 10 | CrewAI: Build a Game-Building Agent System | example | https://workos.com/blog/how-to-build-a-game-building-agent-system-with-crewai |
| 11 | CrewAI: Build Your First Flow (Event-Driven Orchestration) | tutorial | https://docs.crewai.com/en/guides/flows/first-flow |
| 12 | CrewAI Examples: Write a Book with Flows | tutorial | https://github.com/crewAIInc/crewAI-examples/tree/main/flows/write_a_book_with_flows |
| 13 | AG2 (AutoGen) Official Quickstart Guide | tutorial | https://docs.ag2.ai/latest/docs/home/quickstart/ |
| 14 | AG2: GroupChat Advanced Concepts | tutorial | https://docs.ag2.ai/latest/docs/user-guide/advanced-concepts/groupchat/groupchat/ |
| 15 | AG2: Perform Research with Multi-Agent Group Chat | tutorial | https://docs.ag2.ai/latest/docs/use-cases/notebooks/notebooks/agentchat_groupchat_research/ |
| 16 | OpenAI Agents SDK: Official Documentation | tutorial | https://openai.github.io/openai-agents-python/ |
| 17 | OpenAI Agents SDK: Quickstart | tutorial | https://openai.github.io/openai-agents-python/quickstart/ |
| 18 | OpenAI Agents SDK: Handoffs and Guardrails Example | example | https://openai.github.io/openai-agents-python/handoffs/ |
| 19 | OpenAI Agents SDK: Orchestration and Handoffs Guide | tutorial | https://developers.openai.com/api/docs/guides/agents/orchestration |
| 20 | Building Agents with the Claude Agent SDK | tutorial | https://anthropic.com/engineering/building-agents-with-the-claude-agent-sdk |
| 21 | Claude Code: Create Custom Sub-Agents | tutorial | https://code.claude.com/docs/en/sub-agents.md |
| 22 | Claude Code Sub-Agents and the Orchestrator Pattern | pattern | https://www.channel.tel/blog/claude-code-subagents-orchestrator-pattern |
| 23 | Building Specialized AI Sub-Agents in Claude Code: Multi-Agent Orchestration | pattern | https://techarion.com/blog/building-specialized-ai-sub-agents-claude-code-multi-agent-orchestration |
| 24 | Agentic Memory: A-Mem Paper (Zettelkasten-Inspired Agent Memory) | tutorial | https://arxiv.org/abs/2502.12110 |
| 25 | MIRIX: Multi-Agent Memory System for LLM-Based Agents | tutorial | https://arxiv.org/html/2507.07957v1 |
| 26 | LangMem: Memory Management for LangGraph Agents | tool | https://github.com/langchain-ai/langmem |
| 27 | Mem0: Production-Ready Long-Term Memory for AI Agents | tool | https://github.com/mem0ai/mem0 |
| 28 | LangChain Long-Term Memory Documentation | tutorial | https://docs.langchain.com/oss/python/langchain/long-term-memory |
| 29 | Multi-Agent Orchestration Patterns: Supervisor, Swarm, Hierarchical, Router, Pipeline, Consensus | pattern | https://lushbinary.com/blog/multi-agent-orchestration-patterns-supervisor-swarm-pipeline-router-guide/ |
| 30 | Pipeline Pattern: Sequential Agent Stages for Content Generation | workflow | https://fast.io/resources/multi-agent-orchestration-patterns/ |
| 31 | Evaluator-Optimizer Pattern: Iterative Refinement with Dual Agents | workflow | https://www.anthropic.com/engineering/building-effective-agents |
| 32 | Plan-and-Execute Pattern: Upfront Planning with Step-by-Step Execution | workflow | https://dev.to/gabrielanhaia/react-plan-and-execute-or-reflection-the-three-agent-patterns-every-engineer-needs-in-2026-355p |
| 33 | Router Pattern: Classification-Based Agent Dispatch | workflow | https://www.anthropic.com/engineering/building-effective-agents |
| 34 | Function Calling Deep Dive: Building LLM-Powered Tools and Agents | tutorial | https://dataa.dev/2025/04/15/function-calling-deep-dive-building-llm-powered-tools-and-agents/ |
| 35 | From Basic Tool Calling to Advanced ReAct Agents: A Complete Implementation Guide | tutorial | https://thedataguy.pro/blog/2025/08/llm-tool-calling-to-react-agent/ |
| 36 | Microsoft AI Agents for Beginners: Tool Use Lesson | tutorial | https://github.com/microsoft/ai-agents-for-beginners/blob/main/04-tool-use/README.md |
| 37 | Tool Use: How AI Agents Interact with the Real World | pattern | https://hopx.ai/blog/ai-agents/tool-use-pattern-ai-agents/ |
| 38 | ReAct Agent from Scratch with Gemini 2.5 and LangGraph | example | https://www.philschmid.de/langgraph-gemini-2-5-react-agent |
| 39 | SWE-bench: Evaluating Agents on Real-World GitHub Issues | tutorial | https://github.com/SWE-bench/SWE-bench/ |
| 40 | Anthropic Agent Design Patterns: Tool Surface, Programmatic Tool Calling, and Caching | pattern | https://github.com/anthropics/skills/blob/main/skills/claude-api/shared/agent-design.md |
| 41 | Swarm Pattern: Decentralized Agent Orchestration with Emergent Coordination | workflow | https://blog.premai.io/multi-agent-ai-systems-architecture-communication-and-coordination/ |
| 42 | AG2 Group Chat with Research Team: Planner, Scientist, Critic, and Executor | example | https://github.com/ag2ai/ag2/blob/main/notebook/agentchat_groupchat.ipynb |
| 43 | Hierarchical Pattern: Multi-Level Supervision for Enterprise Scale | workflow | https://fast.io/resources/multi-agent-orchestration-patterns/ |
| 44 | DeepLearning.AI: AI Agents in LangGraph (Andrew Ng) | course | https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/ |
| 45 | Parallelization Pattern: Sectioning and Voting for Speed and Reliability | pattern | https://www.anthropic.com/engineering/building-effective-agents |
| 46 | Building Governed AI Agents: Handoffs, Guardrails, and Centralized Policy Enforcement | example | https://developers.openai.com/cookbook/examples/partners/agentic_governance_guide/agentic_governance_cookbook |
| 47 | Agentic RAG: Agent-Controlled Retrieval Augmented Generation | pattern | https://www.genaipatterns.dev/patterns/rag/agentic-rag |
| 48 | Google Agent Development Kit (ADK) | tool | https://github.com/google/adk-docs |
| 49 | Model Context Protocol (MCP): Connecting Agents to External Tools and Data | tutorial | https://modelcontextprotocol.io/introduction |
| 50 | Anthropic Computer Use: Building Desktop Automation Agents with Claude | tutorial | https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool |
| 51 | Agentic AI with LangGraph, CrewAI, AutoGen and BeeAI (IBM/Coursera) | course | https://www.coursera.org/learn/agentic-ai-with-langgraph-crewai-autogen-and-beeai |
| 52 | Google Codelab: Scale Agents with CrewAI, LangGraph, A2A, and ADK | tutorial | https://codelabs.developers.google.com/next26/scale-agents |
| 53 | LangChain Academy: Introduction to LangGraph (Free) | course | https://academy.langchain.com/courses/intro-to-langgraph |
| 54 | AI Agent Frameworks Compared: CrewAI vs LangGraph vs AutoGen vs Claude Code | tutorial | https://www.developersdigest.tech/guides/ai-agent-frameworks-compared |
| 55 | Building Production AI Agents with LangGraph: Beyond the Toy Examples | tutorial | https://dev.to/young_gao/building-production-ai-agents-with-langgraph-beyond-the-toy-examples-2idm |
| 56 | Deploy LangGraph to Production: Step-by-Step Postgres Tutorial | tutorial | https://rapidclaw.dev/blog/deploy-langgraph-production-tutorial-2026 |
| 57 | Build an AI Agent from Scratch: LangGraph Tutorial with Tools, Memory, and Human-in-the-Loop | tutorial | https://appscale.blog/ar/blog/build-ai-agent-langgraph-tools-memory-step-by-step-tutorial-2026 |
| 58 | LangGraph AI Assistant Tutorial: 7-Module Structured Course | pattern | https://github.com/girijesh-ai/langgraph-ai-assistant-tutorial |
| 59 | Stateful AI Agent with FastAPI, LangGraph, and PostgreSQL | tutorial | https://dev.to/shahzaib_dev/how-to-build-a-stateful-ai-agent-with-fastapi-langgraph-and-postgresql-5b45 |
| 60 | CrewAI Production Architecture: Flows, State Management, and Gradual Autonomy | tool | https://docs.crewai.com/en/concepts/production-architecture |
| 61 | CrewAI Flows: Production Multi-Agent Guide 2026 | tutorial | https://www.jahanzaib.ai/blog/crewai-flows-production-multi-agent-guide |
| 62 | Agent Service Toolkit: Full Stack LangGraph Agent with FastAPI and Streaming | tool | https://github.com/JoshuaC215/agent-service-toolkit |
| 63 | All Agentic Architectures: 17+ Implementations with LangGraph and CrewAI | pattern | https://github.com/FareedKhan-dev/all-agentic-architectures |
| 64 | Agentic RAG for Dummies: Modular LangGraph Implementation | pattern | https://github.com/GiovanniPasq/agentic-rag-for-dummies |
| 65 | Building Multi-Agent AI Applications with AutoGen: Complete Tutorial 2026 | tutorial | https://medium.com/@vishwajeetv2003/building-multi-agent-ai-applications-with-autogen-complete-tutorial-2026-2fbd9af73a9c |
| 66 | AutoGen Tutorial: Async Programming, Multi-Agent Teams, and Human-in-the-Loop | pattern | https://github.com/alfredang/autogen_tutorial |
| 67 | Top 10 Agentic AI Frameworks Compared: LangGraph vs CrewAI vs AutoGen (Benchmarks) | pattern | https://dev.to/dextralabs/top-10-agentic-ai-frameworks-compared-langgraph-vs-crewai-vs-autogen-vs-benchmarks-inside-1d6g |
| 68 | Complete Guide to AI Agent Frameworks 2026 | pattern | https://turion.ai/blog/complete-guide-ai-agent-frameworks-2026/ |
| 69 | AI Agent Framework Showdown: Claude Agent SDK vs Strands vs LangGraph vs OpenAI Agents SDK | pattern | https://qubittool.com/blog/ai-agent-framework-comparison-2026 |
| 70 | Best AI Agent Frameworks 2026: LangGraph vs CrewAI Tested on 30 Repos | pattern | https://theeditorial.news/ai-agents/langgraph-vs-crewai-vs-autogen-vs-openai-swarm-vs-llamaindex-agents-which-agent-framework-ships-mpcl9yrq |
| 71 | Framework Analysis: 44 Agent Frameworks Through a Context Engineering Lens | pattern | https://github.com/larsderidder/framework-analysis |
| 72 | A2A Protocol v1.0 Specification: Agent-to-Agent Interoperability Standard | pattern | https://a2a-protocol.org/v1.0.0/specification/ |
| 73 | A2A Protocol v1.0 Production Patterns for Agent-to-Agent Work | pattern | https://replyant.com/lab/a2a-protocol-v1-production/ |
| 74 | DeepAgents: The Batteries-Included Agent Harness by LangChain | tool | https://github.com/langchain-ai/deepagents |
| 75 | Google Gemini Fullstack LangGraph Quickstart | pattern | https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart |
| 76 | Python A2A: Library for Google's Agent-to-Agent Protocol | tool | https://github.com/themanojdesai/python-a2a |
| 77 | AgentOps: AI Agent Monitoring, LLM Cost Tracking, and Benchmarking SDK | tool | https://github.com/AgentOps-AI/agentops |
| 78 | CrewAI Studio: GUI for Managing and Running CrewAI Agents | pattern | https://github.com/strnad/CrewAI-Studio |
| 79 | Full-Stack AI Agent Template: FastAPI + Next.js with CrewAI Agents and RAG | pattern | https://github.com/vstorm-co/full-stack-ai-agent-template |

## fine-tuning

*LLM Fine-Tuning — LoRA, QLoRA, PEFT, dataset prep, evaluation*

**59 references**

| # | Title | Type | URL |
|---|-------|------|-----|
| 1 | LoRA/QLoRA Fine-Tuning Pipeline with PEFT | workflow | https://huggingface.co/docs/peft/main/quicktour |
| 2 | QLoRA Fine-Tuning with PEFT and BitsAndBytes | example | https://huggingface.co/docs/trl/sft_trainer |
| 3 | Fine-Tuning LLMs with LoRA and QLoRA: A Practical Deep-Dive | tutorial | https://www.abstractalgorithms.dev/fine-tuning-llms-with-lora-and-qlora |
| 4 | LoRA and QLoRA Fine-Tuning Guide 2026 (AI Workflow Lab) | tutorial | https://aiworkflowlab.dev/article/how-to-fine-tune-llms-with-lora-and-qlora-production-python-guide |
| 5 | LoRA Adapter Merging and Export to GGUF | example | https://github.com/ggml-org/llama.cpp/blob/master/tools/quantize/README.md |
| 6 | Unsloth: 2-5x Faster LLM Fine-Tuning | tool | https://github.com/unslothai/unsloth |
| 7 | Axolotl: Configurable LLM Fine-Tuning Framework | tool | https://docs.axolotl.ai/index.html |
| 8 | torchtune: PyTorch Native LLM Fine-Tuning | tool | https://github.com/meta-pytorch/torchtune |
| 9 | How to Create Data for Fine-Tuning LLMs (DigitalOcean) | tutorial | https://www.digitalocean.com/community/tutorials/how-to-create-llm-finetuning-dataset |
| 10 | LLM Fine-Tuning Dataset Preparation: End-to-End Guide | tutorial | https://asoasis.tech/articles/2026-04-22-0853-llm-fine-tuning-dataset-preparation-guide/ |
| 11 | Dataset Preparation and Formatting for SFT | example | https://machinelearningplus.com/machine-learning/custom-instruction-dataset-fine-tuning/ |
| 12 | FSDP Multi-GPU Fine-Tuning Workflow | workflow | https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.md |
| 13 | HuggingFace TRL SFTTrainer Documentation | tutorial | https://huggingface.co/docs/trl/sft_trainer |
| 14 | DPO Alignment Fine-Tuning Workflow | workflow | https://www.philschmid.de/rl-with-llms-in-2025-dpo |
| 15 | TRL DPOTrainer Documentation | tutorial | https://github.com/huggingface/trl/blob/main/docs/source/dpo_trainer.md |
| 16 | Guide to RL Post-Training Algorithms: PPO, DPO, GRPO, and Beyond | tutorial | https://huggingface.co/blog/karina-zadorozhny/guide-to-llm-post-training-algorithms |
| 17 | EleutherAI LM Evaluation Harness | tool | https://github.com/eleutherAI/lm-evaluation-harness |
| 18 | Evaluating Fine-Tuned Models with LM Evaluation Harness | workflow | https://github.com/eleutherAI/lm-evaluation-harness |
| 19 | LoRA Adapter Merging and GGUF Export for Local Deployment | workflow | https://www.mintlify.com/ggml-org/llama.cpp/models/quantizing-models |
| 20 | vLLM: High-Throughput LLM Serving with Multi-LoRA Support | tool | https://docs.vllm.ai/en/latest/serving/online_serving/ |
| 21 | Ollama Custom Model Import and Modelfile Reference | tutorial | https://docs.ollama.com/import |
| 22 | Deploy Fine-Tuned Model to vLLM Production Stack | workflow | https://github.com/vllm-project/production-stack |
| 23 | The Ultimate LLM Fine-Tuning Guide (PromptInjection) | book | https://www.promptinjection.net/p/the-ultimate-llm-ai-fine-tuning-guide-tutorial |
| 24 | On-Policy Preference Data Generation for DPO | pattern | https://www.philschmid.de/rl-with-llms-in-2025-dpo |
| 25 | Chat Template Consistency Between Training and Inference | pattern | https://aiworkflowlab.dev/article/how-to-fine-tune-llms-with-lora-and-qlora-production-python-guide |
| 26 | Avoiding Catastrophic Forgetting in Domain Fine-Tuning | pattern | https://www.abstractalgorithms.dev/fine-tuning-llms-with-lora-and-qlora |
| 27 | Quality Over Quantity in Fine-Tuning Datasets | pattern | https://labelsets.ai/blog-llm-fine-tuning-dataset |
| 28 | PoliLegalLM: Domain-Specific LLM for Legal Reasoning | tutorial | https://arxiv.org/abs/2604.17543 |
| 29 | Multi-Stage Training Pipeline for Domain Adaptation | pattern | https://arxiv.org/abs/2604.17543 |
| 30 | Continuous Fine-Tuning with Catastrophic Forgetting Mitigation | pattern | https://aclanthology.org/2025.findings-naacl.303.pdf |
| 31 | A/B Testing Fine-Tuned Models in Production | pattern | https://arxiv.org/pdf/2507.21983 |
| 32 | HuggingFace PEFT: Parameter-Efficient Fine-Tuning Library | tool | https://github.com/huggingface/peft |
| 33 | Deploying a Fine-Tuned Model with Ollama | example | https://docs.ollama.com/import |
| 34 | Full Fine-Tuning to Production Deployment Pipeline | workflow | https://www.promptinjection.net/p/the-ultimate-llm-ai-fine-tuning-guide-tutorial |
| 35 | Target All Linear Projections for LoRA (Not Just Q and V) | pattern | https://www.youngju.dev/blog/llm/2026-03-02-llm-finetuning-lora-qlora-peft.en |
| 36 | Docker-Based Fine-Tuning Environment Setup | workflow | https://curlscape.com/blog/fine-tuning-open-models-in-the-real-world-unsloth-axolotl-and-the-case-for-docker |
| 37 | ORPO Alignment Fine-Tuning Workflow | workflow | https://huggingface.co/docs/trl/orpo_trainer |
| 38 | DeepSpeed: Distributed Training with ZeRO Offloading | tool | https://github.com/deepspeedai/DeepSpeed |
| 39 | DeepSpeed ZeRO-3 QLoRA Fine-Tuning Configuration | example | https://github.com/deepspeedai/DeepSpeed/tree/master/examples |
| 40 | mergekit: Model Merging for Fine-Tuned LLMs | tool | https://github.com/arcee-ai/mergekit |
| 41 | Model Merging with mergekit: TIES and SLERP | example | https://github.com/arcee-ai/mergekit |
| 42 | GRPO Fine-Tuning Workflow (DeepSeek-R1 Style) | workflow | https://huggingface.co/docs/trl/grpo_trainer |
| 43 | MT-Bench and LLM-as-Judge for Fine-Tuned Model Evaluation | tutorial | https://github.com/lm-sys/FastChat/blob/main/fastchat/llm_judge/README.md |
| 44 | LoRA+ and QA-LoRA: Improved Fine-Tuning Methods | pattern | https://arxiv.org/abs/2402.12354 |
| 45 | Multi-Task Fine-Tuning with Task-Specific Adapters | workflow | https://huggingface.co/docs/peft/main/quicktour |
| 46 | Flash Attention 2 for Memory-Efficient Fine-Tuning | tutorial | https://github.com/Dao-AILab/flash-attention |
| 47 | Reward Model Training for RLHF Pipeline | workflow | https://huggingface.co/docs/trl/reward_trainer |
| 48 | Knowledge Distillation as Fine-Tuning Pretraining | pattern |  |
| 49 | HuggingFace AutoTrain: No-Code LLM Fine-Tuning | tool | https://github.com/huggingface/autotrain-advanced |
| 50 | Iterative DPO for Continuous Model Improvement | pattern | https://huggingface.co/blog/karina-zadorozhny/guide-to-llm-post-training-algorithms |
| 51 | Fine-Tuning LLMs with LoRA (tutorialQ) | tutorial | https://tutorialq.com/ai/ml/fine-tuning-llms-lora |
| 52 | LLM Fine-Tuning Complete Guide 2026 (youngju.dev) | tutorial | https://www.youngju.dev/blog/llm/2026-03-17-llm-finetuning-complete-guide.en |
| 53 | NVIDIA NeMo Framework 2.0: End-to-End LLM Training and Fine-Tuning | tool | https://docs.nvidia.com/nemo-framework/user-guide/25.04/index.html |
| 54 | NVIDIA NeMo Curator: GPU-Accelerated Data Preparation | tool | https://docs.nvidia.com/nemo-framework/user-guide/25.04/nemotoolkit/starthere/fundamentals.html |
| 55 | NVIDIA NeMo Guardrails: Safety and Alignment for LLMs | tool | https://developer.nvidia.com/nemo-guardrails |
| 56 | DeepSpeed SuperOffload: Efficient Large-Scale LLM Training on Superchips | tool | https://deepspeed.readthedocs.io/en/stable/index.html |
| 57 | NVIDIA Megatron-FSDP: Distributed Training with FSDP and Megatron Core | tool | https://docs.nvidia.com/megatron-core/developer-guide/0.17.0/discussions/megatron-fsdp-user-guide/megatron-fsdp-user-guide.html |
| 58 | NVIDIA NeMo Framework: Qwen3 Pretraining and Fine-Tuning Recipes | tutorial | https://docs.nvidia.com/nemo-framework/user-guide/25.09/llms/qwen3.html |
| 59 | NVIDIA TensorRT Model Optimizer: Quantization and Compression | tool | https://developer.nvidia.com/TensorRT |

## mlops

*MLOps & LLMOps — CI/CD, Docker, K8s, MLflow, model serving*

**63 references**

| # | Title | Type | URL |
|---|-------|------|-----|
| 1 | MLOps Specialization (Coursera/Board Infinity) | course | https://www.coursera.org/specializations/machine-learning-operations-mlops |
| 2 | LLMOps Specialization (Duke University/Coursera) | course | https://www.coursera.org/specializations/large-language-model-operations |
| 3 | LLMOps Short Course (DeepLearning.AI) | course | https://www.deeplearning.ai/courses/llmops |
| 4 | Machine Learning in Production (DeepLearning.AI) | course | https://www.deeplearning.ai/courses/machine-learning-in-production |
| 5 | MLOps and LLMOps BootCamp (AgileFever) | course | https://agilefever.com/bootcamps/mlops-bootcamp/ |
| 6 | LLMOps Masterclass 2026 (Udemy) | course | https://www.udemy.com/course/llmops-masterclass-generative-ai-mlops-aiops/ |
| 7 | LLMOps: Building Production-Ready LLM Systems (Educative) | course | https://www.educative.io/courses/llmops |
| 8 | MLOps Engineering on AWS (EnterOne) | course | https://www.enterone.com/platforms/amazon-web-services/courses/aws-mlpops |
| 9 | CI/CD Pipeline for ML Models | workflow |  |
| 10 | Docker + Kubernetes ML Deployment | workflow |  |
| 11 | Model Monitoring and Alerting Setup | workflow |  |
| 12 | Feature Store Setup with Feast | workflow |  |
| 13 | ML Model Testing Pipeline | workflow |  |
| 14 | Canary Deployment with KServe and Prometheus | workflow |  |
| 15 | MLflow 3 Experiment Tracking and GenAI Evaluation | example |  |
| 16 | FastAPI Model Serving with Health Checks and Metrics | example |  |
| 17 | Docker Compose for ML Stack with MLflow, Redis, Prometheus, and Grafana | example |  |
| 18 | GitHub Actions CI/CD for ML Models | example |  |
| 19 | Data Drift Detection with Evidently | example |  |
| 20 | A/B Testing with Consistent Hash-Based Routing | example |  |
| 21 | GPU Scheduling with Kubernetes DRA | example |  |
| 22 | MLflow | tool | https://mlflow.org/ |
| 23 | Kubeflow | tool | https://www.kubeflow.org/ |
| 24 | Weights & Biases (W&B) | tool | https://wandb.ai/ |
| 25 | Evidently | tool | https://www.evidentlyai.com/ |
| 26 | Feast | tool | https://feast.dev/ |
| 27 | BentoML | tool | https://bentoml.com/ |
| 28 | DVC (Data Version Control) | tool | https://dvc.org/ |
| 29 | KitOps | tool | https://kitops.ml/ |
| 30 | KServe | tool | https://kserve.github.io/ |
| 31 | Shadow Deployment Pattern | pattern |  |
| 32 | Feature Store Pattern | pattern |  |
| 33 | Canary Deployment Pattern | pattern |  |
| 34 | Model Registry Pattern | pattern |  |
| 35 | Data Pipeline Pattern (Medallion Architecture) | pattern |  |
| 36 | Infrastructure as Code for ML Platforms | pattern |  |
| 37 | GPU Cost Optimization Pattern | pattern |  |
| 38 | MLflow GenAI Tutorial Series | tutorial | https://github.com/dmatrix/mlflow-genai-tutorials |
| 39 | MLflow Official Quickstart | tutorial | https://mlflow.org/docs/latest/quickstart.html |
| 40 | Kubeflow Pipelines V2 on Kubernetes | tutorial | https://oneuptime.com/blog/post/2026-02-09-kubeflow-pipelines-v2-kubernetes/view |
| 41 | DVC Getting Started Guide | tutorial | https://dvc.org/doc/start |
| 42 | Canary Model Rollouts with KServe and Prometheus | tutorial | https://oneuptime.com/blog/post/2026-02-09-canary-model-rollouts-kserve/view |
| 43 | ML Model Serving with BentoML and Kubernetes | tutorial | https://www.youngju.dev/blog/ai-platform/2026-03-03-bentoml-model-serving-guide.en |
| 44 | IaC Patterns for ML Platforms (Terraform) | tutorial | https://engineersofai.com/docs/mlops/infrastructure-as-code/IaC-Patterns-for-ML-Platforms |
| 45 | Machine Learning in Production (Christian Kastner) | book | https://mlip-cmu.github.io/book/ |
| 46 | Machine Learning Platform Engineering (Manning) | book | https://www.manning.com/books/machine-learning-platform-engineering |
| 47 | Machine Learning Engineering on AWS (2nd Edition) | book | https://www.packtpub.com/en-us/product/machine-learning-engineering-on-aws-9781835881095 |
| 48 | Designing Machine Learning Systems (Chip Huyen) | book | https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/ |
| 49 | AI Engineering (Chip Huyen) | book | https://huyenchip.com/books/ |
| 50 | Machine Learning Engineering in Action (Ben Wilson) | book | https://www.manning.com/books/machine-learning-engineering-in-action |
| 51 | MLOpsLab.org LLMOps Crash Course: Beginners Guide to LLM Operations | course | https://mlopslab.org/llmops-tutorial-a-beginners-guide-to-llm-operations-lifecycle-workflow/ |
| 52 | MLOps and LLMOps: Deploying and Scaling AI in Production (Coursera/Board Infinity) | course | https://www.coursera.org/learn/mlops-and-llmops-deploying-and-scaling-ai-in-production |
| 53 | PromptTools | tool | https://github.com/hegelai/prompttools |
| 54 | Vector Admin | tool | https://github.com/Mintplex-Labs/vector-admin |
| 55 | Awesome MLOps Contents | pattern | https://github.com/MLOpsKR/Awesome-MLOps-Contents |
| 56 | Rocketride Server | tool | https://github.com/rocketride-org/rocketride-server |
| 57 | NVIDIA NIM Operator Observability: Prometheus and OpenTelemetry | tutorial | https://docs.nvidia.com/nim/large-language-models/2.0.0/reference/logging-and-observability.html |
| 58 | NVIDIA NIM Operator Installation and Configuration (Kubernetes) | tutorial | https://docs.nvidia.com/nim-operator/latest/install.html |
| 59 | NVIDIA NeMo Guardrails: Content Safety Integration with NIM | tutorial | https://docs.nvidia.com/nemo/microservices/latest/guardrails/tutorials/integrate-nemoguard-nims.html |
| 60 | NVIDIA NIM Air-Gapped Enterprise Deployment (Kubernetes Operator) | tutorial | https://docs.nvidia.com/nim-operator/latest/air-gap.html |
| 61 | NVIDIA Dynamo: Disaggregated Serving for AI Factories | tool | https://www.nvidia.com/en-us/ai/dynamo/ |
| 62 | nim-audit: Security Auditing for NIM Containers | tool | https://github.com/ashzak/nim-audit |
| 63 | Hyena-PAM-Proxy: Unified API Gateway for NVIDIA NIM Models | tool | https://github.com/CosmonautCode/Hyena-PAM-Proxy |

## prompt-engineering

*Advanced prompting — CoT, ReAct, ToT, system prompts, constitutional AI*

**56 references**

| # | Title | Type | URL |
|---|-------|------|-----|
| 1 | Prompting for Effective LLM Reasoning and Planning (Udacity + Microsoft) | course | https://www.udacity.com/course/prompting-for-effective-llm-reasoning-and-planning-with-microsoft-foundry--cd14704 |
| 2 | Advanced Prompt Engineering: CoT, COSTAR and XML (FindSkill) | course | https://findskill.ai/courses/advanced-prompts/ |
| 3 | Mastering Prompt Engineering with CoT, ReAct, and ToT (Cognixia) | course | https://www.cognixia.com/course/mastering-prompt-engineering-with-cot-react-and-tot/ |
| 4 | Prompt Engineering 2026: Demystifying Advanced AI Techniques (Sikho) | course | https://sikho.ai/course/prompt-engineering-2026-demystifying |
| 5 | Advanced Prompt Engineering (Educative) | course | https://www.educative.io/courses/prompt-engineering-guide/advanced-prompt-engineering |
| 6 | Anthropic Prompt Engineering Interactive Tutorial | course | https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview |
| 7 | OpenAI Prompt Engineering Guide | course | https://platform.openai.com/docs/guides/prompt-engineering |
| 8 | Google Prompt Engineering for Developers (DeepLearning.AI) | course | https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/ |
| 9 | Chain-of-Thought Prompting Workflow | workflow |  |
| 10 | System Prompt Design Pattern | workflow |  |
| 11 | ReAct (Reason+Act) Prompting Pattern | workflow |  |
| 12 | Few-Shot Prompt Engineering Process | workflow |  |
| 13 | Structured Output with JSON Schema | workflow |  |
| 14 | Chain-of-Thought with Self-Verification | example |  |
| 15 | ReAct Agent Prompt Template | example |  |
| 16 | Structured JSON Output Prompt | example |  |
| 17 | Meta-Prompt for Automatic Prompt Optimization | example |  |
| 18 | Multi-Turn Conversation with Context Management | example |  |
| 19 | Promptfoo | tool | https://github.com/promptfoo/promptfoo |
| 20 | DSPy | tool | https://dspy.ai/ |
| 21 | LangSmith Prompt Playground | tool | https://smith.langchain.com/ |
| 22 | Anthropic Workbench | tool | https://console.anthropic.com/workbench |
| 23 | OpenAI Playground | tool | https://platform.openai.com/playground |
| 24 | Least-to-Most Prompting | pattern |  |
| 25 | Self-Consistency Decoding | pattern |  |
| 26 | Directional Stimulus Prompting | pattern |  |
| 27 | Prompt Chaining Pattern | pattern |  |
| 28 | Emotional Prompting | pattern |  |
| 29 | Anthropic Prompt Engineering Guide | tutorial | https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview |
| 30 | Learn Prompting (Open-Source Course) | tutorial | https://learnprompting.org/ |
| 31 | Prompt Engineering Guide (DAIR.AI) | tutorial | https://www.promptingguide.ai/ |
| 32 | Microsoft Prompt Engineering Guide | tutorial | https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering |
| 33 | The Art of Prompt Engineering (OpenAI Guide) | book | https://platform.openai.com/docs/guides/prompt-engineering |
| 34 | Prompt Engineering for Generative AI (O'Reilly) | book | https://www.oreilly.com/library/view/prompt-engineering-for/9781098154621/ |
| 35 | Prompt Engineering for LLMs (Cohere) | course | https://docs.cohere.com/docs/prompt-engineering |
| 36 | IBM Prompt Engineering for Generative AI | course | https://www.coursera.org/professional-certificates/ibm-generative-ai-engineering |
| 37 | Automatic Prompt Optimization with DSPy | workflow |  |
| 38 | Production Prompt Testing Pipeline | workflow |  |
| 39 | XML-Structured Prompt for Data Extraction | example |  |
| 40 | Role-Based Prompt for Code Review | example |  |
| 41 | Iterative Refinement Prompt Pattern | example |  |
| 42 | PromptLayer | tool | https://promptlayer.com/ |
| 43 | Guardrails AI | tool | https://www.guardrailsai.com/ |
| 44 | Outlines | tool | https://github.com/dottxt-ai/outlines |
| 45 | Program-Aided Language (PAL) Pattern | pattern |  |
| 46 | Tree-of-Thought Prompting | pattern |  |
| 47 | Self-Ask Prompting Pattern | pattern |  |
| 48 | Instruction Following Hierarchy Pattern | pattern |  |
| 49 | Anthropic Prompt Engineering Cookbook | tutorial | https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/be-clear-and-direct |
| 50 | LangChain Prompt Templates Guide | tutorial | https://python.langchain.com/docs/concepts/prompt_templates/ |
| 51 | ChatGPT Prompt Engineering for Developers (DeepLearning.AI) | book | https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/ |
| 52 | Prompt Engineering Complete Guide: CoT, DSPy, Structured Output (youngju.dev) | tutorial | https://www.youngju.dev/blog/ai/2026-03-17-prompt-engineering-complete-guide.en |
| 53 | Advanced LLM Prompt Engineering: CoT, ReAct, and Tree of Thoughts (youngju.dev) | tutorial | https://www.youngju.dev/blog/llm/2026-03-10-llm-prompt-engineering-cot-react-advanced.en |
| 54 | Every Prompt Engineering Technique Explained: The Research-Backed Guide (SurePrompts) | tutorial | https://sureprompts.com/blog/advanced-prompt-engineering-techniques |
| 55 | Prompt Engineering 2026: The Frameworks That Actually Work (Pasquale Pillitteri) | tutorial | https://pasqualepillitteri.it/en/news/1090/prompt-engineering-2026-frameworks-complete-guide |
| 56 | Promptify | tool | https://github.com/promptslab/Promptify |

## inference

*LLM inference — vLLM, Ollama, SGLang, llama.cpp, quantization, batching*

**86 references**

| # | Title | Type | URL |
|---|-------|------|-----|
| 1 | vLLM Official Documentation and Tutorials | course | https://docs.vllm.ai/ |
| 2 | vLLM vs Ollama vs TGI Comparison (ToolHalla 2026) | course | https://toolhalla.ai/blog/vllm-vs-ollama-vs-tgi-2026 |
| 3 | SGLang: Efficient Serving for LLMs | course | https://github.com/sgl-project/sglang |
| 4 | Ollama Official Documentation | course | https://ollama.com/ |
| 5 | Complete Guide to vLLM and Ollama (YoungJu Dev) | course | https://www.youngju.dev/blog/llm/vllm_ollama_serving_complete_guide.en |
| 6 | Run LLM Inference on Talos Linux (OneUptime) | course | https://oneuptime.com/blog/post/2026-03-03-run-llm-inference-workloads-on-talos-linux/view |
| 7 | Self-Hosting LLMs: vLLM vs TGI vs Ollama (BirJob) | course | https://www.birjob.com/blog/vllm-tgi-ollama-self-hosting-llms |
| 8 | Quantization Deep Dive: GGUF, AWQ, GPTQ, FP8 | course | https://huggingface.co/docs/transformers/main/en/quantization |
| 9 | Deploy vLLM in Production with Docker | workflow |  |
| 10 | Set Up Ollama for Local Development | workflow |  |
| 11 | Multi-LoRA Serving with vLLM | workflow |  |
| 12 | Model Quantization and GGUF Export Pipeline | workflow |  |
| 13 | SGLang RadixAttention Setup for Multi-Turn | workflow |  |
| 14 | vLLM Docker Compose Production Setup | example |  |
| 15 | Ollama Modelfile for Custom Model | example |  |
| 16 | SGLang Server Launch Configuration | example |  |
| 17 | OpenAI-Compatible API Client for vLLM/Ollama | example |  |
| 18 | vLLM | tool | https://github.com/vllm-project/vllm |
| 19 | Ollama | tool | https://ollama.com/ |
| 20 | SGLang | tool | https://github.com/sgl-project/sglang |
| 21 | llama.cpp | tool | https://github.com/ggerganov/llama.cpp |
| 22 | HuggingFace Text Generation Inference (TGI) | tool | https://github.com/huggingface/text-generation-inference |
| 23 | Production vs Development Serving Pattern | pattern |  |
| 24 | Speculative Decoding Pattern | pattern |  |
| 25 | Quantization Selection Guide | pattern |  |
| 26 | KV Cache Optimization Pattern | pattern |  |
| 27 | GPU Hardware Recommendation Pattern | pattern |  |
| 28 | vLLM Getting Started Guide | tutorial | https://docs.vllm.ai/en/latest/getting_started/quickstart.html |
| 29 | Ollama Modelfile Documentation | tutorial | https://ollama.com/Modelfile |
| 30 | llama.cpp Quantization Guide | tutorial | https://github.com/ggerganov/llama.cpp/blob/master/examples/quantize/README.md |
| 31 | vLLM Production Deployment on Kubernetes | tutorial | https://docs.vllm.ai/en/latest/serving/deploying_on_k8s.html |
| 32 | LLM Inference at Scale (Online Resource) | book | https://www.anyscale.com/blog/llm-inference-at-scale |
| 33 | Building LLM Apps (O'Reilly) | book | https://www.oreilly.com/library/view/building-llm-apps/9781098167969/ |
| 34 | Fast Inference for LLMs (DeepLearning.AI) | course | https://www.deeplearning.ai/short-courses/efficient-inference-for-llms/ |
| 35 | Deploying LLMs at Scale (Anyscale) | course | https://www.anyscale.com/courses/deploying-llms |
| 36 | HuggingFace Inference Endpoints Guide | course | https://huggingface.co/docs/inference-endpoints/index |
| 37 | Kubernetes for AI/ML Workloads (KodeKloud) | course | https://kodekloud.com/courses/kubernetes-for-ai-ml-workloads |
| 38 | Deploy LLM with GPU Sharing on Kubernetes | workflow |  |
| 39 | Model Quantization Pipeline for Production | workflow |  |
| 40 | Speculative Decoding Setup with vLLM | workflow |  |
| 41 | vLLM Multi-LoRA Serving Configuration | example |  |
| 42 | Ollama Python Client for Local Development | example |  |
| 43 | AutoGPTQ | tool | https://github.com/AutoGPTQ/AutoGPTQ |
| 44 | AutoAWQ | tool | https://github.com/casper-hansen/AutoAWQ |
| 45 | NVIDIA TensorRT-LLM | tool | https://github.com/NVIDIA/TensorRT-LLM |
| 46 | Ray Serve | tool | https://docs.ray.io/en/latest/serve/ |
| 47 | Continuous Batching Pattern | pattern |  |
| 48 | Model Merging Pattern | pattern |  |
| 49 | Prefix Caching Pattern | pattern |  |
| 50 | HuggingFace Transformers Inference Guide | tutorial | https://huggingface.co/docs/transformers/main/en/inference |
| 51 | vLLM Quantization Deployment Guide | tutorial | https://docs.vllm.ai/en/latest/features/quantization/ |
| 52 | vLLM vs SGLang vs TensorRT-LLM vs Ollama: Choosing an Inference Engine in 2026 (LeetLLM) | tutorial | https://leetllm.com/blog/llm-inference-engine-comparison-2026 |
| 53 | vLLM vs Ollama vs SGLang vs TensorRT-LLM Serving 2026 (The AI Engineer) | tutorial | https://theaiengineer.substack.com/p/vllm-vs-ollama-vs-sglang-vs-tensorrt |
| 54 | vLLM vs SGLang: Inference Engine Comparison 2026 (TURION.AI) | tutorial | https://turion.ai/blog/vllm-vs-sglang-inference-comparison-2026/ |
| 55 | Concurrent LLM Serving: Benchmarking vLLM vs SGLang vs Ollama (DEV Community) | tutorial | https://dev.to/zkaria_gamal_3cddbbff21c8/concurrent-llm-serving-benchmarking-vllm-vs-sglang-vs-ollama-1cpn |
| 56 | SGLang vs vLLM: Latency Cuts 40% Under Dynamic Batching (Markaicode) | tutorial | https://markaicode.com/vs/sglang-vs-vllm/ |
| 57 | NVIDIA Dynamo: Distributed LLM Inference Framework | tool | https://github.com/ai-dynamo/dynamo/ |
| 58 | NVIDIA Dynamo Architecture: Disaggregated Prefill/Decode Serving | tutorial | https://docs.dynamo.nvidia.com/dynamo/design-docs/overall-architecture |
| 59 | Full-Stack Optimizations for Agentic Inference with NVIDIA Dynamo | tutorial | https://developer.nvidia.com/blog/full-stack-optimizations-for-agentic-inference-with-nvidia-dynamo/ |
| 60 | NVIDIA NIM: Containerized Inference Microservices | tool | https://docs.nvidia.com/nim/large-language-models/latest/deployment-guide.html |
| 61 | NVIDIA Triton Inference Server (Dynamo-Triton) | tool | https://github.com/triton-inference-server/server/releases/tag/v2.68.0 |
| 62 | Triton Inference Server: Autoscaling TensorRT-LLM on Kubernetes | tutorial | https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2670/user-guide/docs/tutorials/Deployment/Kubernetes/TensorRT-LLM_Autoscaling_and_Load_Balancing/README.html |
| 63 | NVIDIA TensorRT 10.x: Inference Optimization SDK | tool | https://docs.nvidia.com/deeplearning/tensorrt/latest/index.html |
| 64 | Eliminating Pipeline Friction in AI Model Serving with TensorRT | tutorial | https://developer.nvidia.com/blog/how-to-eliminate-pipeline-friction-in-ai-model-serving/ |
| 65 | NVIDIA NIM API: 189 Hosted Models on build.nvidia.com | tool | https://docs.nvidia.com/nim/large-language-models/latest/api-reference.html |
| 66 | NVIDIA NeMo Guardrails: Programmable Safety for LLM Applications | tool | https://docs.nvidia.com/nemo/guardrails/latest/about/overview.html |
| 67 | NVIDIA NIM for LLMs: Quickstart Guide | tutorial | https://docs.nvidia.com/nim/large-language-models/latest/get-started/quickstart.html |
| 68 | NVIDIA NIM LoRA/PEFT Adapter Serving Guide | tutorial | https://docs.nvidia.com/nim/large-language-models/latest/peft.html |
| 69 | NVIDIA NIM Structured Output and Guided Decoding | tutorial | https://docs.nvidia.com/nim/large-language-models/latest/structured-generation.html |
| 70 | NVIDIA NIM Function/Tool Calling Guide | tutorial | https://docs.nvidia.com/nim/large-language-models/latest/function-calling.html |
| 71 | NVIDIA NIM Operator Quick Start (Kubernetes) | tutorial | https://docs.nvidia.com/nim-operator/latest/quickstart.html |
| 72 | NVIDIA NIM Cloud Deployment: AWS EKS | tutorial | https://docs.nvidia.com/nim/large-language-models/2.0.2/deployment/csp-deployment/aws.html |
| 73 | NVIDIA NIM Cloud Deployment: Azure AKS | tutorial | https://docs.nvidia.com/nim/large-language-models/2.0.1/deployment/csp-deployment/azure.html |
| 74 | NVIDIA NIM on Google Kubernetes Engine (GKE) | tutorial | https://docs.nvidia.com/nim/cloud/gke/latest/overview.html |
| 75 | NVIDIA NIM Multi-Node Deployment Guide | tutorial | https://docs.nvidia.com/nim/large-language-models/latest/deployment/multi-node-deployment.html |
| 76 | NVIDIA NIM Air-Gapped Deployment Guide | tutorial | https://docs.nvidia.com/nim/large-language-models/latest/deploy-air-gap.html |
| 77 | NVIDIA NIM LLM Benchmarks: Latency and Throughput | tutorial | https://docs.nvidia.com/nim/benchmarking/llm/latest/performance.html |
| 78 | NVIDIA Build API Catalog Quickstart | tutorial | https://docs.api.nvidia.com/nim/docs/api-quickstart |
| 79 | Finding Free Hosted Models on NVIDIA Builder (Steve Scargall) | tutorial | https://stevescargall.com/blog/2026/04/using-the-api-to-find-free-hosted-models-on-nvidia-builder/ |
| 80 | NVIDIA nim-deploy: Reference Deployments for Kubernetes | tool | https://github.com/NVIDIA/nim-deploy |
| 81 | NVIDIA NIM Free API: 100+ Models at Zero Cost (aiHola) | tool | https://aihola.com/article/nvidia-nim-free-api-models |
| 82 | NeMo Microservices Python SDK (nemo-microservices) | tool | https://pypi.org/project/nemo-microservices/ |
| 83 | NVIDIA NIM OpenAI-Compatible Client Setup | example | https://developer.nvidia.com/blog/a-simple-guide-to-deploying-generative-ai-with-nvidia-nim/ |
| 84 | NVIDIA NIM Docker Deployment with LoRA Adapters | example | https://docs.nvidia.com/nim/large-language-models/2.0.5/advanced-use-cases/finetune-lora.html |
| 85 | NVIDIA NIM Three-Tier PEFT Cache Architecture | pattern | https://docs.nvidia.com/nim/large-language-models/2.0.5/deployment/kubernetes-deployment/nim-operator-deployment.html |
| 86 | NVIDIA NIM OpenAI-Compatible API Pattern | pattern | https://docs.api.nvidia.com/nim/reference/llm-apis |

## claude-code

*Claude Code — context engineering, hooks, skills, MCP servers, agents*

**58 references**

| # | Title | Type | URL |
|---|-------|------|-----|
| 1 | Official Claude Code Documentation | course | https://code.claude.com/docs/en |
| 2 | Claude Code Best Practices (Official) | course | https://code.claude.com/docs/en/best-practices |
| 3 | Claude Code Common Workflows (Official) | course | https://code.claude.com/docs/en/common-workflows |
| 4 | Claude Code in Large Codebases (Blog) | course | https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start |
| 5 | The Claude Code Handbook (freeCodeCamp) | course | https://www.freecodecamp.org/news/claude-code-handbook/ |
| 6 | Complete Claude Code Guide 2026 (Generative Inc) | course | https://www.generative.inc/the-complete-claude-code-guide-2026-planning-context-engineering-and-high-leverage-development |
| 7 | Claude Code Hooks Reference | course | https://code.claude.com/docs/en/hooks |
| 8 | Claude Code Skills System | course | https://code.claude.com/docs/en/skills |
| 9 | 4-Phase Claude Code Workflow (Plan then Implement then Verify) | workflow |  |
| 10 | CLAUDE.md Cascade Configuration | workflow |  |
| 11 | Subagent Delegation Pattern | workflow |  |
| 12 | Hook System for Deterministic Automation | workflow |  |
| 13 | Worktree Parallel Development Pattern | workflow |  |
| 14 | CLAUDE.md Template for AI/ML Projects | example |  |
| 15 | Hook Configuration for Auto-Lint | example |  |
| 16 | MCP Server Configuration for Claude Code | example |  |
| 17 | Cost Optimization Configuration | example |  |
| 18 | Claude Code CLI | tool | https://code.claude.com/docs/en |
| 19 | Claude Code Extensions (VS Code, JetBrains) | tool | https://code.claude.com/docs/en/ide-integrations |
| 20 | MCP (Model Context Protocol) | tool | https://modelcontextprotocol.io/ |
| 21 | Claude Code Plugins System | tool | https://code.claude.com/docs/en/plugins |
| 22 | Playwright MCP for Browser Automation | tool | https://github.com/anthropics/anthropic-quickstarts/tree/main/mcp-playwright |
| 23 | Context Window Management Pattern | pattern |  |
| 24 | Verification-Driven Development Pattern | pattern |  |
| 25 | Anti-Patterns to Avoid | pattern |  |
| 26 | Model Selection Strategy | pattern |  |
| 27 | Multi-Agent Orchestration with Claude Code | pattern |  |
| 28 | Claude Code Hooks Guide (Official) | tutorial | https://code.claude.com/docs/en/hooks-guide |
| 29 | Getting Started with Claude Code (Official) | tutorial | https://code.claude.com/docs/en/getting-started |
| 30 | MCP Server Development with FastMCP | tutorial | https://modelcontextprotocol.io/quickstart/python |
| 31 | Claude Code Zero to Hero (Prabhat Dev) | book | https://prabhat.dev/claude-code-zero-to-hero-the-complete-2026-field-guide/ |
| 32 | Anthropic API Documentation | course | https://docs.anthropic.com/en/docs/about-claude/api |
| 33 | Building with Claude (Anthropic Cookbook) | course | https://github.com/anthropics/anthropic-cookbook |
| 34 | Claude Code GitHub Discussions | course | https://github.com/anthropics/claude-code/discussions |
| 35 | Claude Code Release Notes | course | https://github.com/anthropics/claude-code/releases |
| 36 | Error Recovery and Debugging Pattern | workflow |  |
| 37 | Git Integration Pattern | workflow |  |
| 38 | MCP Server Development Pattern | workflow |  |
| 39 | Custom MCP Server with FastMCP | example |  |
| 40 | CLAUDE.md with Custom Commands | example |  |
| 41 | Memory System for Cross-Session Context | example |  |
| 42 | Claude Code Memory System | tool | https://code.claude.com/docs/en/memory |
| 43 | GitHub CLI (gh) | tool | https://cli.github.com/ |
| 44 | Plan Mode Pattern | pattern |  |
| 45 | Verification Loop Pattern | pattern |  |
| 46 | Progressive Context Loading | pattern |  |
| 47 | Claude Code Settings Reference | tutorial | https://code.claude.com/docs/en/settings |
| 48 | Claude Code Security Best Practices | tutorial | https://code.claude.com/docs/en/security |
| 49 | FastMCP Python SDK Documentation | tutorial | https://gofastmcp.com/ |
| 50 | MCP Specification (Model Context Protocol) | tutorial | https://spec.modelcontextprotocol.io/ |
| 51 | Claude Code Hooks, Subagents, and Piping: Advanced Automation for Teams | tutorial | https://devops-monk.com/2026/04/claude-code-hooks-subagents-piping/ |
| 52 | Claude Code Hooks Master Guide: 18 Events and Production Workflow Automation | tutorial | https://claudelab.net/en/articles/claude-code/claude-code-hooks-automation-master-guide |
| 53 | Claude Code Power User Guide: Skills, Hooks, Subagents | tutorial | https://refactix.com/ai-development-engineering/claude-code-power-user-guide-skills-hooks-subagents |
| 54 | Claude Code CLI Guide: Install, Configure, and Use in 2026 | tutorial | https://petronellatech.com/blog/claude-code-cli-guide/ |
| 55 | Claude Code as MCP Server (steipete) | tool | https://github.com/steipete/claude-code-mcp |
| 56 | Obsidian Claude Code MCP | tool | https://github.com/iansinnott/obsidian-claude-code-mcp |
| 57 | Claude Code MCP Install Guide | pattern | https://github.com/undeadpickle/claude-code-mcpinstall |
| 58 | Stitch Skills (Google Labs) | tool | https://github.com/google-labs-code/stitch-skills |

## vector-db

*Vector databases — Qdrant, Pinecone, Weaviate, Milvus, pgvector*

**61 references**

| # | Title | Type | URL |
|---|-------|------|-----|
| 1 | Qdrant Essentials Course (Free) | course | https://qdrant.tech/course/essentials/ |
| 2 | Vector Databases: from Embeddings to Applications (DeepLearning.AI) | course | https://www.deeplearning.ai/courses/vector-databases-embeddings-applications |
| 3 | Vector Databases Deep Dive (Coursera/Packt) | course | https://www.coursera.org/learn/packt-vector-databases-deep-dive-y4haf |
| 4 | Vector Database for GenAI (KodeKloud) | course | https://kodekloud.com/courses/vector-database-for-genai |
| 5 | Vector Databases and Search (Dataquest) | course | https://www.dataquest.io/course/vector-databases/ |
| 6 | Building RAG Systems with Open Models (Coursera) | course | https://www.coursera.org/learn/building-rag-systems-with-open-models |
| 7 | Enterprise RAG: Best Practices and Advanced Techniques (SupportVectors) | course | https://supportvectors.io/course/info.php?id=59 |
| 8 | UCLA Extension: Building RAG (COM SCI 910.2) | course | https://www.uclaextension.edu/computer-science/machine-learning-ai/course/building-retrieval-augmented-generation-rag-com-sci |
| 9 | Set Up Qdrant Hybrid Search with Sparse + Dense Vectors | workflow |  |
| 10 | Production Vector DB Deployment Checklist | workflow |  |
| 11 | Embedding Model Selection Process | workflow |  |
| 12 | Data Ingestion Pipeline for Vector DB | workflow |  |
| 13 | Qdrant Quantization for Memory Reduction | workflow |  |
| 14 | Qdrant Hybrid Search with FastEmbed | example |  |
| 15 | ChromaDB Quick Start for RAG | example |  |
| 16 | Pinecone Serverless Setup | example |  |
| 17 | Weaviate Hybrid Search Setup | example |  |
| 18 | Milvus Vector Search Pipeline | example |  |
| 19 | Qdrant | tool | https://qdrant.tech/ |
| 20 | Pinecone | tool | https://www.pinecone.io/ |
| 21 | Weaviate | tool | https://weaviate.io/ |
| 22 | Milvus | tool | https://milvus.io/ |
| 23 | ChromaDB | tool | https://www.trychroma.com/ |
| 24 | Hybrid Search Pattern (Sparse + Dense) | pattern |  |
| 25 | Quantization for Memory Reduction | pattern |  |
| 26 | Chunking Strategy Selection Pattern | pattern |  |
| 27 | Re-ranking Pattern for Improved Retrieval | pattern |  |
| 28 | Multi-Vector Document Pattern | pattern |  |
| 29 | Qdrant Python Client Quickstart | tutorial | https://qdrant.tech/documentation/ |
| 30 | Weaviate Getting Started Guide | tutorial | https://weaviate.io/developers/weaviate/quickstart |
| 31 | Milvus Quickstart with PyMilvus | tutorial | https://milvus.io/docs/quickstart.md |
| 32 | Pinecone Python SDK Guide | tutorial | https://docs.pinecone.io/guides/get-started/quickstart |
| 33 | MTEB Leaderboard for Embedding Model Selection | tutorial | https://huggingface.co/spaces/mteb/leaderboard |
| 34 | Vector Databases for AI Applications (O'Reilly) | book | https://www.oreilly.com/library/view/vector-databases-for/9781098154638/ |
| 35 | AI-Powered Search (Trey Grainger) | book | https://www.manning.com/books/ai-powered-search |
| 36 | Qdrant Vector Search Masterclass | course | https://qdrant.tech/documentation/ |
| 37 | Pinecone Learning Center | course | https://docs.pinecone.io/learn |
| 38 | Weaviate Academy | course | https://weaviate.io/academy |
| 39 | Build a RAG Pipeline with Qdrant and FastEmbed | workflow |  |
| 40 | Migrate from ChromaDB to Qdrant | workflow |  |
| 41 | Set Up Qdrant with Docker Compose for Production | workflow |  |
| 42 | FAISS Index for Local Vector Search | example |  |
| 43 | FAISS (Facebook AI Similarity Search) | tool | https://github.com/facebookresearch/faiss |
| 44 | FastEmbed | tool | https://github.com/qdrant/fastembed |
| 45 | Milvus Attu (GUI) | tool | https://github.com/zilliztech/attu |
| 46 | HNSW Parameter Tuning Pattern | pattern |  |
| 47 | Namespace and Multi-Tenancy Pattern | pattern |  |
| 48 | Vector Database Sharding Pattern | pattern |  |
| 49 | FastEmbed Quickstart Guide | tutorial | https://github.com/qdrant/fastembed#quickstart |
| 50 | Milvus Partitioning and Sharding Guide | tutorial | https://milvus.io/docs/partition_key.md |
| 51 | Vector Database in RAG: How It Works, Which One to Pick (2026 Guide) | tutorial | https://krunalkanojiya.com/blog/vector-database-in-rag |
| 52 | Milvus Tutorial: Vector DB RAG in 13 Steps [2026] | tutorial | https://tech-insider.org/milvus-vector-database-tutorial-rag-13-steps-2026/ |
| 53 | Pinecone vs Qdrant: Which Vector Database Fits Production in 30 Minutes (2026) | tutorial | https://markaicode.com/vs/pinecone-vs-qdrant/ |
| 54 | HelixDB | tool | https://github.com/HelixDB/helix-db |
| 55 | CozoDB | tool | https://github.com/cozodb/cozo |
| 56 | VectorDBBench (Zilliz) | tool | https://github.com/zilliztech/VectorDBBench |
| 57 | Lantern (PostgreSQL Vector Extension) | tool | https://github.com/lanterndata/lantern |
| 58 | chromem-go | tool | https://github.com/philippgille/chromem-go |
| 59 | Write You a Vector DB | pattern | https://github.com/skyzh/write-you-a-vector-db |
| 60 | zvec (Alibaba) | tool | https://github.com/alibaba/zvec |
| 61 | HyperDB | tool | https://github.com/jdagdelen/hyperDB |

## gpu-compute

*GPU & CUDA — PyTorch, CUDA kernels, mixed precision, FlashAttention*

**63 references**

| # | Title | Type | URL |
|---|-------|------|-----|
| 1 | Foundations of Deep Learning with PyTorch (Global Knowledge) | course | https://www.globalknowledge.com/en-gb/courses/data_and_ai/data/gk840205 |
| 2 | GPU, CUDA, and PyTorch Performance Optimizations (Create With) | course | https://www.createwith.com/event/madrid-gpu-cuda-and-pytorch-performance-optimizations-may-2026-1 |
| 3 | PyTorch for Deep Learning Professional Certificate (DeepLearning.AI) | course | https://www.deeplearning.ai/specializations/pytorch-for-deep-learning-professional-certificate |
| 4 | Training PyTorch 2026: Optimizing AI Models in Production (Learni) | course | https://learni-group.com/en/training/training-pytorch-2026-expert-jjebq6-vv649y |
| 5 | GPU Programming using CUDA (HLRS Stuttgart) | course | https://www.hlrs.de/training/2026/cuda1 |
| 6 | CUDA C++ Programming Guide (NVIDIA Official) | course | https://docs.nvidia.com/cuda/cuda-c-programming-guide/ |
| 7 | NVIDIA Deep Learning Institute Courses | course | https://www.nvidia.com/en-us/training/ |
| 8 | PyTorch Performance Tuning Guide (Official) | course | https://pytorch.org/tutorials/recipes/recipes/tuning_guide.html |
| 9 | Mixed Precision Training Setup with PyTorch AMP | workflow |  |
| 10 | Distributed Training with PyTorch FSDP2 | workflow |  |
| 11 | CUDA Kernel Profiling with Nsight | workflow |  |
| 12 | RTX 5090 Optimization Checklist | workflow |  |
| 13 | Custom CUDA Kernel Development | workflow |  |
| 14 | PyTorch Mixed Precision Training with AMP | example |  |
| 15 | PyTorch torch.compile Optimization | example |  |
| 16 | GPU Memory Monitoring and OOM Prevention | example |  |
| 17 | CUDA Kernel Launch Configuration | example |  |
| 18 | Multi-GPU Data Parallel Training | example |  |
| 19 | NVIDIA Nsight Systems | tool | https://developer.nvidia.com/nsight-systems |
| 20 | NVIDIA Nsight Compute | tool | https://developer.nvidia.com/nsight-compute |
| 21 | torch.compile (PyTorch) | tool | https://pytorch.org/tutorials/intermediate/torch_compile_tutorial.html |
| 22 | NVIDIA TensorRT | tool | https://developer.nvidia.com/tensorrt |
| 23 | CUDA Toolkit | tool | https://developer.nvidia.com/cuda-toolkit |
| 24 | Flash Attention Pattern | pattern |  |
| 25 | Gradient Checkpointing Pattern | pattern |  |
| 26 | Tensor Core Optimization Pattern | pattern |  |
| 27 | Gradient Accumulation Pattern | pattern |  |
| 28 | Asynchronous Data Loading Pattern | pattern |  |
| 29 | PyTorch Performance Tuning Guide | tutorial | https://pytorch.org/tutorials/recipes/recipes/tuning_guide.html |
| 30 | CUDA Programming Tutorial (NVIDIA) | tutorial | https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html |
| 31 | PyTorch FSDP Tutorial | tutorial | https://pytorch.org/tutorials/intermediate/FSDP_tutorial.html |
| 32 | Flash Attention Implementation Guide | tutorial | https://github.com/Dao-AILab/flash-attention |
| 33 | Programming Massively Parallel Processors (Kirk and Hwu) | book | https://www.elsevier.com/books/programming-massively-parallel-processors/kirk/978-0-12-811986-0 |
| 34 | Deep Learning (Goodfellow, Bengio, Courville) | book | https://www.deeplearningbook.org/ |
| 35 | CUDA Parallel Programming (Coursera/NVIDIA) | course | https://www.coursera.org/learn/cuda-parallel-programming |
| 36 | Practical Deep Learning for Coders (fast.ai) | course | https://course.fast.ai/ |
| 37 | Distributed Deep Learning with DeepSpeed | course | https://www.deepspeed.ai/tutorials/ |
| 38 | DeepSpeed ZeRO-3 Training Setup | workflow |  |
| 39 | Benchmark GPU Performance with PyTorch Profiler | workflow |  |
| 40 | DeepSpeed ZeRO-3 Configuration for Large Models | example |  |
| 41 | DDP with Gradient Accumulation and Mixed Precision | example |  |
| 42 | DeepSpeed | tool | https://www.deepspeed.ai/ |
| 43 | PyTorch Profiler | tool | https://pytorch.org/tutorials/recipes/recipes/profiler_recipe.html |
| 44 | Weights and Biases (W&B) | tool | https://wandb.ai/ |
| 45 | Activation Checkpointing Pattern | pattern |  |
| 46 | Effective Batch Size Tuning Pattern | pattern |  |
| 47 | Learning Rate Warmup and Decay Pattern | pattern |  |
| 48 | DeepSpeed Getting Started Tutorial | tutorial | https://www.deepspeed.ai/tutorials/getting-started/ |
| 49 | PyTorch Distributed Data Parallel Tutorial | tutorial | https://pytorch.org/tutorials/intermediate/ddp_tutorial.html |
| 50 | Oxford CUDA Programming on NVIDIA GPUs | course | https://people.maths.ox.ac.uk/gilesm/cuda/index.html |
| 51 | Fundamentals of Accelerated Computing with Modern CUDA C++ (NHR@FAU/NVIDIA DLI) | course | https://hpc.fau.de/calendar/fundamentals-of-accelerated-computing-with-modern-cuda-c-online/ |
| 52 | Fundamentals of Accelerated Computing with CUDA Python (NHR@FAU/NVIDIA DLI) | course | https://hpc.fau.de/calendar/fundamentals-of-accelerated-computing-with-cuda-python-online/ |
| 53 | NVIDIA Accelerated Python Tutorial (GitHub) | tutorial | https://github.com/NVIDIA/accelerated-computing-hub/tree/main/tutorials/accelerated-python |
| 54 | Training and Deploying Large-Scale Models (University Course) | course | https://training-large-models-course.github.io/ |
| 55 | Distributed Data Parallel in PyTorch Tutorial Series (Learncafe) | tutorial | https://blog.learncafe.com/courses/distributed-data-parallel-in-pytorch-tutorial-series-20260327115333 |
| 56 | NVIDIA NGC Catalog: GPU-Optimized Containers, Models, and Helm Charts | tool | https://docs.nvidia.com/ngc/latest/ngc-catalog-user-guide.html |
| 57 | CUDA 13.2 Toolkit: cuTile Python DSL and Tile Programming Model | tool | https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html |
| 58 | CUDA C++ Best Practices Guide | tool | https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/ |
| 59 | NVIDIA RAPIDS cuDF: GPU-Accelerated DataFrames | tool | https://docs.rapids.ai/api/cudf/nightly/user_guide/10min/ |
| 60 | NVIDIA RAPIDS cuML: GPU-Accelerated Machine Learning | tool | https://docs.rapids.ai/api/cuml/latest/cuml_intro/ |
| 61 | DeepSpeed AutoTP: Automatic Tensor Parallel Training | tool | https://www.deepspeed.ai/tutorials/autotp-training/ |
| 62 | NVIDIA NeMo Framework: End-to-End LLM Training Platform | tool | https://www.nvidia.com/en-us/gpu-cloud/ |
| 63 | NVIDIA NGC AI and HPC Containers Directory | tutorial | https://developer.nvidia.com/ai-hpc-containers |

## autonomous-agents

*Autonomous systems — self-correcting loops, planning, long-horizon tasks*

**64 references**

| # | Title | Type | URL |
|---|-------|------|-----|
| 1 | PIVOT: Plan-Inspect-eVOlve Trajectory Optimization for Self-Correcting Agents | workflow | https://arxiv.org/html/2605.11225 |
| 2 | ReAct Agent Loop: Reason-Act-Observe for Autonomous Tool-Using Agents | workflow | https://langchain-ai-langgraph-40.mintlify.app/tutorials/react-agent |
| 3 | Agentic RAG with Evidence Sufficiency Gating | workflow | https://arxiv.org/pdf/2603.29085 |
| 4 | Claude Code Parallel Worktree Agent Orchestration | workflow | https://code.claude.com/docs/en/worktrees |
| 5 | Production Agent Monitoring and Graceful Degradation Pipeline | workflow | https://zylos.ai/research/2026-03-22-sre-ai-agent-systems-observability-incident-response |
| 6 | HECG Hierarchical Error-Correcting Agent Loop for Embodied Tasks | workflow | https://arxiv.org/pdf/2603.08388 |
| 7 | LangGraph ReAct Agent with Tool Calling (Python) | example | https://machinelearningplus.com/gen-ai/langgraph-react-agent-from-scratch/ |
| 8 | CrewAI Autonomous Research Crew (Python) | example | https://docs.crewai.com/en/concepts/agents |
| 9 | Self-Debugging Agent with OpenHands SDK (Python) | example | https://docs.openhands.dev/sdk |
| 10 | MCP Tool Definition for Autonomous Agents (TypeScript) | example | https://www.anthropic.com/engineering/code-execution-with-mcp |
| 11 | Browser Automation Agent with Playwright MCP (TypeScript) | example | https://github.com/microsoft/playwright-mcp |
| 12 | PreFlect: From Retrospective to Prospective Reflection in LLM Agents | pattern | https://arxiv.org/pdf/2602.07187 |
| 13 | SPIRAL: Symbolic LLM Planning via Grounded and Reflective Search | pattern | https://ojs.aaai.org/index.php/AAAI/article/view/40975 |
| 14 | Evaluator-Optimizer Pattern: Generate-Evaluate-Loop for Autonomous Agents | pattern | https://docs.langchain.com/oss/python/langgraph/workflows-agents |
| 15 | LangChain Deep Agents from Scratch Course | course | https://github.com/langchain-ai/deep-agents-from-scratch |
| 16 | LangGraph v1.0: StateGraph API for Agent Orchestration | tool | https://docs.langchain.com/oss/python/langgraph/graph-api |
| 17 | Playwright MCP: Model Context Protocol Server for Browser Automation | tool | https://github.com/microsoft/playwright-mcp |
| 18 | Orchestrator-Worker Pattern for Dynamic Task Decomposition | pattern | https://docs.langchain.com/oss/python/langgraph/workflows-agents |
| 19 | MCP Code Mode: Progressive Tool Disclosure for Token-Efficient Agents | pattern | https://www.anthropic.com/engineering/code-execution-with-mcp |
| 20 | LangGraph Multi-Agent Systems: Supervisor, Swarm, and Pipeline Patterns | tutorial | https://www.abstractalgorithms.dev/langgraph-multi-agent-supervisor-pattern |
| 21 | Synapse: Spreading Activation for Episodic-Semantic Memory in Agents | pattern | https://arxiv.org/pdf/2601.02744 |
| 22 | Kumiho: Graph-Native Cognitive Memory with AGM Belief Revision | pattern | https://arxiv.org/pdf/2603.17244 |
| 23 | CraniMem: Cranial-Inspired Gated and Bounded Memory for Agents | pattern | https://arxiv.org/pdf/2603.15642 |
| 24 | BrainMem: Brain-Inspired Evolving Memory for Embodied Agent Task Planning | pattern | https://arxiv.org/abs/2604.16331 |
| 25 | Hierarchical Memory Theory for Language Agents (CoALA Framework) | book | https://arxiv.org/pdf/2603.21564 |
| 26 | Pre-Act: Multi-Step Planning Before Action Outperforms ReAct | pattern | https://arxiv.org/pdf/2505.09970 |
| 27 | Planner-Centric DAG Framework: Decoupling Planning from Execution | pattern | https://arxiv.org/html/2511.10037 |
| 28 | THOUGHTSCULPT: Reasoning with Intermediate Revision via MCTS | pattern | https://aclanthology.org/2025.findings-naacl.428.pdf |
| 29 | CrewAI Multi-Agent Debate: Proposer-Opposer-Judge Pattern | tutorial | https://github.com/rajeswarandhandapani/crewai_multi_agent_debate |
| 30 | Multi-Agent Debate Arena with Structured Argument Cards (Python/FastAPI) | example | https://github.com/mmaazkhanhere/debate-agents |
| 31 | Claude Code Subagents: Delegated Workers with Custom Tools and Models | tool | https://code.claude.com/docs/en/sub-agents.md |
| 32 | Claude Code Agent Teams: Multi-Agent Orchestration with Shared Task Lists | tool | https://code.claude.com/docs/en/agent-teams |
| 33 | Running Parallel Claude Code Agents with Worktrees | pattern | https://refactix.com/ai-development-engineering/claude-code-worktrees-parallel-agents |
| 34 | AutoGPT Platform: Visual Agent Builder with Autonomous Mode | tool | https://github.com/Significant-Gravitas/AutoGPT |
| 35 | AutoGPT Agent Mode: Autonomous Tool Execution Loops in the Platform | tutorial | https://github.com/Significant-Gravitas/AutoGPT/pull/11547 |
| 36 | Demystifying LLM-Based Software Engineering Agents (FSE 2025) | book | https://lingming.cs.illinois.edu/publications/fse2025.pdf |
| 37 | OpenHands SDK V1: Event-Sourced State Management for Self-Debugging Agents | tool | https://openhands.dev/blog/introducing-the-openhands-software-agent-sdk |
| 38 | PAR2-RAG: Planned Active Retrieval and Reasoning for Multi-Hop QA | pattern | https://arxiv.org/pdf/2603.29085 |
| 39 | DualRAG: Dual-Process Reasoning and Retrieval Integration | pattern | https://aclanthology.org/2025.acl-long.1539.pdf |
| 40 | ACE: Agentic Context Evolution — Metacognitive To Retrieve or To Think | pattern | https://arxiv.org/pdf/2601.08747 |
| 41 | SPD-RAG: Sub-Agent Per Document for Cross-Document Synthesis | pattern | https://arxiv.org/pdf/2603.08329 |
| 42 | Osprey: Production-Ready Agentic AI for Safety-Critical Control Systems | pattern | https://arxiv.org/html/2508.15066 |
| 43 | VIGIL: Reflective Runtime for Self-Healing LLM Agents | pattern | https://arxiv.org/html/2512.07094v1 |
| 44 | HASHIRU: Hierarchical Agent System for Hybrid Intelligent Resource Utilization | tool | https://arxiv.org/pdf/2506.04255 |
| 45 | Sovereign-OS: Constitution-First AI Orchestration with CFO-Enforced Budgets | tool | https://github.com/Justin0504/Sovereign-OS |
| 46 | LangGraph ReAct Agent Tutorial: Build from Scratch with v1.0 API | tutorial | https://dev.to/agentsindex/langgraph-tutorial-build-a-working-react-agent-with-the-v10-api-3bc1 |
| 47 | LangGraph Tutorial by OpnCrafter: Cycles, Persistence, and Human-in-the-Loop | tutorial | https://opncrafter.space/guide/langgraph-tutorial |
| 48 | LangGraph create_agent: High-Level Agent Factory with Middleware (Python) | example | https://docs.langchain.com/oss/python/langgraph/use-functional-api |
| 49 | Deep Agent Pattern: TODO Lists, Context Offloading, and Sub-Agent Delegation | workflow | https://github.com/langchain-ai/deep-agents-from-scratch |
| 50 | Anthropic MCP: 10,000+ Community Servers and Registry API for Dynamic Tool Discovery | tool | https://www.anthropic.com/news/model-context-protocol |
| 51 | MIA: Memory Intelligence Agent with Manager-Planner-Executor Architecture | workflow | https://arxiv.org/pdf/2604.04503 |
| 52 | MemMA: Coordinating the Memory Cycle via Multi-Agent Reasoning and Self-Evolution | workflow | https://arxiv.org/pdf/2603.18718 |
| 53 | MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory | workflow | https://arxiv.org/pdf/2601.03192 |
| 54 | Polaris: Gödel Agent for Small Language Models via Experience-Abstracted Policy Repair | workflow | https://arxiv.org/pdf/2603.23129 |
| 55 | DeerFlow: Open-Source Long-Horizon SuperAgent Harness | workflow | https://github.com/bytedance/deer-flow |
| 56 | Agent Guide: Comprehensive AI Agent Development Guide with LangGraph and RAG | workflow | https://github.com/adongwanai/AgentGuide |
| 57 | A2A Protocol v1.0: Agent-to-Agent Communication and Task Lifecycle | workflow | https://github.com/a2aproject/A2A |
| 58 | CrewAI Flows: Event-Driven Multi-Agent Orchestration with @start/@listen/@router | workflow | https://crewai.com/crewai-flows |
| 59 | NirDiamant/agents-towards-production: End-to-End Production Agent Tutorials | workflow | https://github.com/NirDiamant/agents-towards-production |
| 60 | AG2 Build: Sample Code and Application Showcases for AutoGen v0.13+ | workflow | https://github.com/ag2ai/build-with-ag2 |
| 61 | Agentok: Visual Multi-Agent Builder for AG2 (AutoGen) | workflow | https://github.com/dustland/agentok |
| 62 | Cordum: Open Agent Control Plane for Governing Autonomous AI Agents | workflow | https://github.com/cordum-io/cordum |
| 63 | MCP Memory Service: Persistent Memory for AI Agent Pipelines | workflow | https://github.com/doobidoo/mcp-memory-service |
| 64 | SurfSense: Open-Source Privacy-Focused Alternative to NotebookLM for Teams | workflow | https://github.com/MODSetter/SurfSense |

## seo

*SEO & web promotion — landing pages, Core Web Vitals, structured data, sitemaps*

**79 references**

| # | Title | Type | URL |
|---|-------|------|-----|
| 1 | F-Pattern Scanning — Eye-Tracking Evidence for Content Pages | pattern |  |
| 2 | Z-Pattern Scanning — Conversion Page Layout Principle | pattern |  |
| 3 | 50ms First Impression Rule — Visual Credibility Judgment | pattern |  |
| 4 | Triune Brain Model in Design — Reptilian, Limbic, Neocortex Layers | pattern |  |
| 5 | Von Restorff Effect — Isolation Makes Elements Stand Out | pattern |  |
| 6 | Hick's Law — More Choices Slow Decisions | pattern |  |
| 7 | Anchoring Bias — First Information Frames Perception | pattern |  |
| 8 | Social Proof — Testimonials Beat Feature Lists | pattern |  |
| 9 | Loss Aversion — FOMO Framing Outperforms Gain Framing | pattern |  |
| 10 | Zeigarnik Effect — Unfinished Tasks Stay in Memory | pattern |  |
| 11 | Processing Fluency — Easy to Read Means Easy to Trust | pattern |  |
| 12 | Color Psychology in Web Design — Trust, Urgency, Action | pattern |  |
| 13 | Directional Cues — Guiding Eyes Toward the CTA | pattern |  |
| 14 | Cognitive Load Theory — Every Extra Element Costs Attention | pattern |  |
| 15 | Layer-Cake Scanning — Headings Drive Reading Decisions | pattern |  |
| 16 | Facial Coding in Design — Faces Draw and Direct Attention | pattern |  |
| 17 | Dopamine Loops — Micro-Interactions and Progress Rewards | pattern |  |
| 18 | Neuro-Copywriting — 'You' vs 'We' Framing for the Reptilian Brain | pattern |  |
| 19 | Hero Section Anatomy — Headline + Visual + CTA Above the Fold | pattern |  |
| 20 | Single CTA Principle — 1:1 Attention Ratio | pattern |  |
| 21 | Above-Fold Trust Signals — Instant Credibility Markers | pattern |  |
| 22 | Mobile-First CTA Placement — Thumb-Reach Design | pattern |  |
| 23 | Bento Grid Layout — 2026 Design Trend for Feature Pages | pattern |  |
| 24 | Form Design — Fewer Fields = More Completions | pattern |  |
| 25 | Show Product, Don't Describe It — Screenshots Beat Stock | pattern |  |
| 26 | Speed Under 2.5s — Every Second Costs 7% Conversions | pattern |  |
| 27 | User Decision Sequence — Recognition → Relevance → Risk → Effort → Commitment | pattern |  |
| 28 | 3 Friction Points = Abandonment — Reduce Interaction Cost | pattern |  |
| 29 | Google Search Console | tool | https://search.google.com/search-console |
| 30 | Ahrefs — SEO Analysis & Keyword Research | tool | https://ahrefs.com/ |
| 31 | SEMrush — All-in-One SEO and Marketing Platform | tool | https://semrush.com/ |
| 32 | Schema.org Structured Data Guide | tutorial | https://schema.org/ |
| 33 | Sitemap and robots.txt Setup for Web Projects | workflow |  |
| 34 | SSR vs SSG vs CSR — SEO Implications for Web Apps | pattern |  |
| 35 | Prerender.io — Dynamic Rendering for SEO | tool | https://prerender.io/ |
| 36 | Lighthouse — Web Performance and SEO Auditor | tool | https://developer.chrome.com/docs/lighthouse/ |
| 37 | PageSpeed Insights — Google's Performance Scorer | tool | https://pagespeed.web.dev/ |
| 38 | web.dev — Google's Web Development Learning Platform | tool | https://web.dev/ |
| 39 | Core Web Vitals — LCP, INP, CLS Explained | pattern |  |
| 40 | Vercel Analytics — Real-Time Web Performance Monitoring | tool | https://vercel.com/docs/analytics |
| 41 | Image Optimization — Formats, Sizing, and Lazy Loading | pattern |  |
| 42 | CDN Strategies for Static Assets | pattern |  |
| 43 | GitHub Pages Deployment for Open-Source Projects | workflow |  |
| 44 | Open Source Guides — Building Welcoming Communities | tutorial | https://opensource.guide/ |
| 45 | Product Hunt Launch Strategy for Developer Tools | workflow |  |
| 46 | GitHub README Best Practices — Your Project's Landing Page | tutorial | https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes |
| 47 | Awesome-List Strategy — Piggyback on Curated Discovery | pattern |  |
| 48 | Dev.to and Hashnode — Developer Blogging Platforms for Promotion | pattern |  |
| 49 | Google Analytics 4 — Website Analytics | tool | https://analytics.google.com/ |
| 50 | Plausible Analytics — Privacy-Focused Web Analytics | tool | https://plausible.io/ |
| 51 | Umami — Self-Hosted Privacy Analytics | tool | https://umami.is/ |
| 52 | UTM Parameters — Tracking Campaign Traffic Sources | pattern |  |
| 53 | Hotjar — Heatmaps and Session Recordings | tool | https://www.hotjar.com/ |
| 54 | Material 3 Expressive — CHI 2026 Eye-Tracking Validated Design | pattern |  |
| 55 | Carbon UI — Neuroscience-Optimized React Design System | tool | https://www.carbon-ui.com/the-neuroscience-of/ |
| 56 | Tailwind CSS — Utility-First CSS for Rapid UI Building | tool | https://tailwindcss.com/ |
| 57 | Astro — Static Site Generator for Content-Focused Sites | tool | https://astro.build/ |
| 58 | Next.js Static Export — SSG Mode for SEO-Friendly Sites | tool | https://nextjs.org/docs/app/building-your-application/deploying/static-exports |
| 59 | Responsive Design and Accessibility in Promotion Pages | pattern |  |
| 60 | DevRel Strategy — Developer Relations for Open-Source Growth | pattern |  |
| 61 | Substack — Newsletter Platform for Developer Audiences | tool | https://substack.com/ |
| 62 | Beehiiv — Modern Newsletter Platform with Growth Tools | tool | https://www.beehiiv.com/ |
| 63 | Community Building for Open-Source Projects | pattern |  |
| 64 | Base64 Encoding for Inline Images (Data URIs) in HTML/CSS | example |  |
| 65 | SVG Optimization and Base64 Embedding Workflow | example |  |
| 66 | Image Format Selection — WebP, AVIF vs PNG/JPG for Web | pattern |  |
| 67 | CSS Background-Image with Base64 Data URI | example |  |
| 68 | When to Use Base64 vs File References — Performance Tradeoffs | pattern |  |
| 69 | Figma — Collaborative Design and Prototyping | tool | https://www.figma.com/ |
| 70 | Canva — Quick Marketing Graphics and Social Media Images | tool | https://www.canva.com/ |
| 71 | Excalidraw — Diagrams and Wireframes | tool | https://excalidraw.com/ |
| 72 | SVGO — SVG Optimization CLI Tool | tool | https://github.com/svg/svgo |
| 73 | Lucide Icons — Open-Source Icon Library for Web | tool | https://lucide.dev/ |
| 74 | Hugo — Fast Static Site Generator for Documentation Sites | tool | https://gohugo.io/ |
| 75 | Technical Blog Post Structure for Developer Tool Promotion | workflow |  |
| 76 | YouTube Tutorials as Developer Marketing | pattern |  |
| 77 | Meta Tags and Open Graph — Social Sharing Preview Optimization | pattern |  |
| 78 | Canonical URLs and Hreflang — Avoiding Duplicate Content | pattern |  |
| 79 | Astro Landing Page with SEO Meta Tags and Schema.org | example |  |
