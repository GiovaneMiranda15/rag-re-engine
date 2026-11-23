#!/usr/bin/env python3
"""Reconstrói arquivos do experimento reproduzindo Write/Edit e leituras integrais dos transcripts."""
import glob, json, os, sys
P, OLD = sys.argv[1], sys.argv[2]
files, sources, read_full = {}, {}, {}
errors = 0
for tr in sorted(glob.glob(f"{P}/subagents/*.jsonl"), key=os.path.getmtime):
    pending = {}
    for line in open(tr):
        try:
            j = json.loads(line)
        except ValueError:
            continue
        content = (j.get("message") or {}).get("content")
        if not isinstance(content, list):
            continue
        for b in content:
            if not isinstance(b, dict):
                continue
            if b.get("type") == "tool_use" and b["name"] in ("Write", "Edit", "Read"):
                pending[b["id"]] = (b["name"], b["input"])
            elif b.get("type") == "tool_result" and b.get("tool_use_id") in pending:
                name, inp = pending.pop(b["tool_use_id"])
                path = inp.get("file_path", "")
                if not path.startswith(OLD) or b.get("is_error"):
                    continue
                if name == "Write":
                    files[path] = inp["content"]; sources[path] = "write"
                elif name == "Edit" and path in files:
                    if inp["old_string"] in files[path]:
                        files[path] = files[path].replace(inp["new_string"] if False else inp["old_string"], inp["new_string"], -1 if inp.get("replace_all") else 1)
                    else:
                        errors += 1
                elif name == "Read":
                    res = j.get("toolUseResult")
                    f = res.get("file") if isinstance(res, dict) else None
                    if f and f.get("startLine", 1) == 1 and f.get("numLines") == f.get("totalLines"):
                        read_full[path] = f["content"]
restored = 0
for path, text in read_full.items():
    files[path] = text if path not in files else files[path]
    sources.setdefault(path, "read")
for path, text in files.items():
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").write(text); restored += 1
import collections
print("restaurados", restored, collections.Counter(sources.values()), "edits_sem_alvo", errors)
