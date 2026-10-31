"""Verify the hash chain of runs/09_ledger_trace.json.

Each event's hash is SHA-256 over the event's JSON with the "hash" field removed,
serialized with sorted keys (Python json.dumps defaults); prevHash links each event
to the one before, starting from 64 zeros.

Usage: python tools/verify_ledger.py [path/to/09_ledger_trace.json]
"""
import hashlib, json, sys

path = sys.argv[1] if len(sys.argv) > 1 else "runs/09_ledger_trace.json"
events = json.load(open(path, encoding="utf-8"))
prev, ok = "0" * 64, True
for e in events:
    body = {k: v for k, v in e.items() if k != "hash"}
    digest = hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest()
    good = digest == e["hash"] and e["prevHash"] == prev
    ok &= good
    print(f'{e["@id"]:>6}  {"ok" if good else "FAIL"}')
    prev = e["hash"]
print("chain valid" if ok else "chain BROKEN")
sys.exit(0 if ok else 1)
