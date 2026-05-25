# learn-mcp — CLAUDE.md

## Architecture

- `server.py` — FastMCP server (Streamable HTTP, port 8001, Python 3.14). 8 MCP tools, 801 references across 12 topics.
- `data/*.json` — Per-topic reference files (the source of truth). 12 topics including `seo`.
- `merge_refs.py` — Merges `data/*.json` into `references.json`, validates schema, deduplicates.
- `references.json` — Generated (gitignored). Built by `merge_refs.py` at Docker build time and locally.
- `mcp-recommender/` — NOT part of this repo. The recommender lives at `../mcp-recommender/` and is built separately by docker-compose.

## Development workflow

1. Edit `data/<topic>.json` to add/modify references
2. Run `python3 merge_refs.py` to validate and regenerate `references.json`
3. Rebuild: `cd ../ && docker compose build --no-cache learn && docker compose up -d learn`
4. Call `index_to_qdrant()` MCP tool after restart to rebuild Qdrant index

## Docker

- Base image: `python:3.14-slim`
- Multi-stage build: builder stage runs `merge_refs.py`, runtime stage gets `server.py` + `data/` + `references.json`
- Qdrant auto-reindexes on startup if collection is empty (handles container restarts)
- Model pre-warm thread loads `all-MiniLM-L6-v2` at startup to avoid cold-start latency

## Key constraints

- `references.json` is gitignored — always run `merge_refs.py` before building Docker
- Topic names must match `VALID_TOPICS` in `merge_refs.py` AND `TOPICS` dict in `server.py` AND all tool docstrings
- The recommender is a separate project at `../mcp-recommender/`, not inside this directory