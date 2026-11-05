import json, os, subprocess, sys
tr = sys.argv[1]
OLD = sys.argv[2]
seen, pend = set(), {}
ok = fail = 0
for line in open(tr):
    try:
        j = json.loads(line)
    except ValueError:
        continue
    c = (j.get("message") or {}).get("content")
    if not isinstance(c, list):
        continue
    for b in c:
        if not isinstance(b, dict):
            continue
        if b.get("type") == "tool_use" and b["id"] not in seen and b["name"] in ("Write", "Edit", "Bash"):
            seen.add(b["id"]); pend[b["id"]] = (b["name"], b["input"])
        elif b.get("type") == "tool_result" and b.get("tool_use_id") in pend:
            name, inp = pend.pop(b["tool_use_id"])
            if b.get("is_error"):
                continue
            if name == "Write":
                os.makedirs(os.path.dirname(inp["file_path"]), exist_ok=True)
                open(inp["file_path"], "w").write(inp["content"])
            elif name == "Edit":
                t = open(inp["file_path"]).read()
                if inp["old_string"] in t:
                    t = t.replace(inp["old_string"], inp["new_string"], -1 if inp.get("replace_all") else 1)
                    open(inp["file_path"], "w").write(t)
                else:
                    print("edit sem alvo", inp["file_path"][-40:])
            else:
                r = subprocess.run(["bash", "-c", inp["command"]], capture_output=True, text=True, errors="replace", timeout=590)
                if r.returncode:
                    fail += 1; print("falha", r.returncode, inp["command"][:100].replace("\n", " "), "|", r.stderr[-150:].replace("\n", " "))
                else:
                    ok += 1
print("bash ok", ok, "falhas", fail)
