"""Check 03. The Provenance Ledger trace is hash-chained as stated.

Appendix claims checked (Sections 1.7, 3.0, 3.8, Annex B.9):
- eleven events, ev:1 to ev:11, in the order and with the actors, actions and
  respondsTo links of the Section 3.8 table;
- SHA-256 over the canonical JSON of each event, including the previous hash
  (canonical form documented in foundry/ledger.py);
- ev:5, the reading-adoption gate, was passed by the demonstration operator
  (Claude) standing in for the human theorist, not by a human.

Also shows that the chain detects tampering: changing one character of one
event's rationale breaks verification from that event on.
"""
import copy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from foundry.io import load_ledger, Report
from foundry.ledger import verify_chain, rebuild, GENESIS

# Section 3.8 table: (id, HH:MM, actor kind, action, respondsTo)
TABLE = [
    ("ev:1", "18:46", "human", "ingest", None),
    ("ev:2", "18:46", "human", "ingest", None),
    ("ev:3", "18:54", "agent", "propose", "ev:1"),
    ("ev:4", "18:55", "agent", "propose", "ev:2"),
    ("ev:5", "18:56", "agent", "accept", "ev:4"),
    ("ev:6", "18:57", "agent", "challenge", "ev:5"),
    ("ev:7", "18:57", "agent", "challenge", "ev:5"),
    ("ev:8", "18:58", "agent", "annotate", "ev:5"),
    ("ev:9", "19:00", "agent", "derive", "ev:5"),
    ("ev:10", "19:01", "agent", "align", "ev:5"),
    ("ev:11", "19:02", "agent", "design", "ev:7"),
]


def main():
    r = Report("Check 03: Provenance Ledger hash chain")
    ev = load_ledger()
    r.check("number of events", len(ev), 11)
    r.check("first prevHash is the genesis value", ev[0]["prevHash"], GENESIS)
    r.check("hash-chain problems", verify_chain(ev), [])
    r.check("rebuilding every hash from the event bodies reproduces the stored file", rebuild(ev) == ev, True)

    for e, (eid, hhmm, kind, action, resp) in zip(ev, TABLE):
        row = (e["@id"], e["timestamp"][11:16], e["actor"]["kind"], e["action"], e.get("respondsTo"))
        r.check(f"{eid} matches the Section 3.8 table row", row, (eid, hhmm, kind, action, resp))

    r.check("ev:5 actor name", ev[4]["actor"]["name"],
            "demonstration operator (Claude), standing in for the human theorist")
    r.info(f"[INFO] ev:5 actor kind is recorded as {ev[4]['actor']['kind']!r}: no human passed the adoption gate (Section 3.0).")
    r.info("[INFO] Timestamps are reconstructed after the runs, not written live (Section 3.8).")

    t = copy.deepcopy(ev)
    t[5]["rationale"] = t[5]["rationale"] + "."
    probs = verify_chain(t)
    r.check("tamper test: editing ev:6 is detected at event index 5", bool(probs) and probs[0][0] == 5, True)
    return r.finish()


if __name__ == "__main__":
    sys.exit(main())
