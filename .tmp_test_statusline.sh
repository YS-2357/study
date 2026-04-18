#!/bin/bash
# Mirror of ~/.claude/statusline.sh for local testing
python <<'PY'
import json, sys, os, subprocess, math, time

try:
    j = json.load(sys.stdin)
except Exception:
    sys.exit(0)

def g(obj, *path, default=None):
    for p in path:
        if not isinstance(obj, dict):
            return default
        obj = obj.get(p)
        if obj is None:
            return default
    return obj

model    = g(j, "model", "display_name") or g(j, "model", "id")
cwd      = g(j, "workspace", "current_dir") or g(j, "cwd") or ""
ctx_pct  = g(j, "context_window", "used_percentage")
fh_pct   = g(j, "rate_limits", "five_hour", "used_percentage")
fh_epoch = g(j, "rate_limits", "five_hour", "resets_at")
cost     = g(j, "cost", "total_cost_usd")

home = os.path.expanduser("~")
short_cwd = cwd.replace(home.replace("\\", "/"), "~").replace(home, "~") if cwd else ""

branch = ""
if cwd:
    try:
        r = subprocess.run(
            ["git", "-C", cwd, "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True, text=True, timeout=2,
        )
        if r.returncode == 0:
            branch = r.stdout.strip()
    except Exception:
        pass

fh_reset = ""
if fh_epoch is not None:
    try:
        fh_reset = time.strftime("%H:%M", time.localtime(int(fh_epoch)))
    except Exception:
        pass

parts = []
if short_cwd: parts.append(short_cwd)
if branch:   parts.append(f"⎇ {branch}")
if model:    parts.append(model)
if ctx_pct is not None:
    parts.append(f"ctx {math.floor(ctx_pct)}%")
if fh_pct is not None:
    seg = f"5h {math.floor(fh_pct)}%"
    if fh_reset:
        seg += f" ↻{fh_reset}"
    parts.append(seg)
if cost is not None:
    parts.append(f"${cost:.2f}")

if len(parts) >= 2 and parts[1].startswith("⎇"):
    head = parts[0] + " " + parts[1]
    tail = parts[2:]
else:
    head = parts[0] if parts else ""
    tail = parts[1:]

out = head
if tail:
    out = (head + " · " if head else "") + " · ".join(tail)

sys.stdout.write(out)
PY
