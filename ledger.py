"""Hash chaining for Provenance Ledger events (appendix Sections 1.7, 3.8).

This is only the hashing rule used to build `runs/09_ledger_trace.json`.
It is not the Provenance Ledger itself, which is Stage 1 work (appendix
Section 6).

Canonical form: the event with its `hash` field removed, serialized by
Python's `json.dumps(event, sort_keys=True)` with the default separators
(", " and ": ") and ASCII escaping, encoded as UTF-8. The event's `hash` is
the SHA-256 hex digest of that string. Because `prevHash` is a field of the
event, each hash covers the previous one. The first event's `prevHash` is 64
zeros.
"""
import copy
import hashlib
import json

GENESIS = "0" * 64


def canonical(event):
    body = {k: v for k, v in event.items() if k != "hash"}
    return json.dumps(body, sort_keys=True)


def event_hash(event):
    return hashlib.sha256(canonical(event).encode("utf-8")).hexdigest()


def verify_chain(events):
    """Return a list of (index, problem) pairs; empty if the chain is intact."""
    problems = []
    prev = GENESIS
    for i, ev in enumerate(events):
        if ev.get("prevHash") != prev:
            problems.append((i, f"prevHash does not equal the hash of event {i - 1}"))
        h = event_hash(ev)
        if ev.get("hash") != h:
            problems.append((i, f"stored hash {ev.get('hash')} != recomputed {h}"))
        prev = ev.get("hash")
    return problems


def append(events, event):
    """Append a new event to a chain, filling prevHash and hash."""
    ev = copy.deepcopy(event)
    ev["prevHash"] = events[-1]["hash"] if events else GENESIS
    ev.pop("hash", None)
    ev["hash"] = event_hash(ev)
    return events + [ev]


def rebuild(events):
    """Recompute every prevHash and hash from the event bodies."""
    out = []
    for ev in events:
        out = append(out, {k: v for k, v in ev.items() if k not in ("hash", "prevHash")})
    return out
