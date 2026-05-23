#!/usr/bin/env python3
"""Merge per-topic reference JSON files into a single references.json.

Reads data/*.json, deduplicates by URL, validates schema,
and writes the combined references.json.
"""

import json
import sys
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
OUTPUT = Path(__file__).parent / "references.json"

REQUIRED_FIELDS = {"topic", "type", "title", "description", "tags", "difficulty"}
# url is required for types that reference external resources
URL_REQUIRED_TYPES = {"course", "tool", "book", "tutorial"}
VALID_TYPES = {"course", "workflow", "example", "tool", "pattern", "book", "tutorial"}
VALID_DIFFICULTIES = {"beginner", "intermediate", "advanced"}
VALID_TOPICS = {
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
}


def main():
    all_refs = []
    seen_keys = set()
    errors = []

    for path in sorted(DATA_DIR.glob("*.json")):
        print(f"Loading {path.name}...")
        try:
            refs = json.loads(path.read_text())
        except json.JSONDecodeError as e:
            errors.append(f"{path.name}: invalid JSON: {e}")
            continue

        if not isinstance(refs, list):
            errors.append(f"{path.name}: expected list, got {type(refs).__name__}")
            continue

        for i, ref in enumerate(refs):
            # Validate required fields
            missing = REQUIRED_FIELDS - set(ref.keys())
            if missing:
                errors.append(f"{path.name}[{i}]: missing fields: {missing}")
                continue

            # Validate enum fields
            if ref["type"] not in VALID_TYPES:
                errors.append(f"{path.name}[{i}]: invalid type '{ref['type']}'")
            if ref["difficulty"] not in VALID_DIFFICULTIES:
                errors.append(
                    f"{path.name}[{i}]: invalid difficulty '{ref['difficulty']}'"
                )
            if ref["topic"] not in VALID_TOPICS:
                errors.append(f"{path.name}[{i}]: invalid topic '{ref['topic']}'")

            # url required for course/tool/book/tutorial, optional for workflow/example/pattern
            if ref["type"] in URL_REQUIRED_TYPES and not ref.get("url"):
                errors.append(
                    f"{path.name}[{i}]: missing required url for type '{ref['type']}'"
                )

            # Validate URL format
            url = ref.get("url", "")
            if url and not url.startswith(("http://", "https://")):
                errors.append(f"{path.name}[{i}]: invalid URL format '{url[:50]}'")

            # Validate code field for examples
            if ref["type"] == "example" and not ref.get("code"):
                errors.append(
                    f"{path.name}[{i}]: missing required 'code' field for type 'example'"
                )

            # Validate workflow field for workflows
            if ref["type"] == "workflow" and not ref.get("workflow"):
                errors.append(
                    f"{path.name}[{i}]: missing required 'workflow' field for type 'workflow'"
                )

            # Deduplicate by (url, title) — keeps entries that share a URL
            # but have different titles (e.g., multiple patterns from same blog post)
            title = ref.get("title", "")
            key = (url, title) if url else title
            if key in seen_keys:
                continue
            seen_keys.add(key)
            all_refs.append(ref)

    if errors:
        print(f"\n{len(errors)} validation issues found:")
        for e in errors:
            print(f"  - {e}")

    # Sort by topic then title
    all_refs.sort(key=lambda r: (r.get("topic", ""), r.get("title", "")))

    # Warn about duplicate titles (may need manual disambiguation)
    title_counts = {}
    for ref in all_refs:
        t = ref.get("title", "")
        title_counts[t] = title_counts.get(t, 0) + 1
    dup_titles = {t: c for t, c in title_counts.items() if c > 1}
    if dup_titles:
        print(
            f"\n{len(dup_titles)} duplicate titles found (may need manual disambiguation):"
        )
        for t, c in sorted(dup_titles.items()):
            print(f"  [{c}x] {t}")

    OUTPUT.write_text(json.dumps(all_refs, indent=2, ensure_ascii=False))
    print(f"\nWrote {len(all_refs)} references to {OUTPUT}")

    # Stats
    by_topic = {}
    by_type = {}
    for ref in all_refs:
        by_topic[ref["topic"]] = by_topic.get(ref["topic"], 0) + 1
        by_type[ref["type"]] = by_type.get(ref["type"], 0) + 1

    print("\nBy topic:")
    for topic, count in sorted(by_topic.items()):
        print(f"  {topic}: {count}")
    print("\nBy type:")
    for typ, count in sorted(by_type.items()):
        print(f"  {typ}: {count}")


if __name__ == "__main__":
    main()
