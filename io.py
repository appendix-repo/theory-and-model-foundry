"""Paths and loaders shared by every check."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / "runs"
SCHEMA_DIR = ROOT / "schema"
DOCS = ROOT / "docs"
DATA = ROOT / "data"
APPENDIX = DOCS / "FOUNDRY_TECHNICAL_APPENDIX.md"
SCHEMA_PATH = SCHEMA_DIR / "theory-object.v0.schema.json"
CONTEXT_PATH = SCHEMA_DIR / "context.v0.jsonld"
LEDGER_PATH = RUNS / "09_ledger_trace.json"

RUN_FILES = {
    "00": "case_inputs.md",
    "01": "01_explicator_TCE.md",
    "02": "02_explicator_RD.md",
    "03": "03_interlocutor_institutional_TCE.md",
    "04": "04_interlocutor_behavioral_TCE.md",
    "05": "05_model_builder_TCE.md",
    "06": "06_argument_auditor_TCE.md",
    "07": "07_integrator_TCE_RD.md",
    "08": "08_validation_designer_TCE.md",
}

_JSON_BLOCK = re.compile(r"```json\n(.*?)\n```", re.S)


def read_text(path):
    return Path(path).read_text(encoding="utf-8")


def run_text(run_id):
    return read_text(RUNS / RUN_FILES[run_id])


def json_blocks(text):
    """Every ```json fenced block in a markdown text, parsed, in order."""
    return [json.loads(b) for b in _JSON_BLOCK.findall(text)]


def run_json(run_id):
    return json_blocks(run_text(run_id))


def load_schema():
    return json.loads(read_text(SCHEMA_PATH))


def load_ledger():
    return json.loads(read_text(LEDGER_PATH))


def theory_object(prefix):
    """Reading 1 of TCE ('tce') or RD ('rd'), as returned by Run 01 / Run 02."""
    blocks = run_json("01" if prefix == "tce" else "02")
    obj = blocks[0]
    assert obj["@type"] == "TheoryObject", obj.get("@id")
    return obj


def node_index(obj):
    """Map @id -> node for every identified node in a theory object."""
    idx = {}
    for key in ("constructs", "relations", "mechanisms", "assumptions",
                "scopeConditions", "propositions", "derivations"):
        for node in obj.get(key, []):
            idx[node["@id"]] = node
    return idx


class Report:
    """Collects named checks, prints them, and returns an exit status."""

    def __init__(self, title):
        self.title = title
        self.lines = []
        self.failures = 0

    def info(self, text):
        self.lines.append(text)

    def check(self, label, got, expected, tol=None):
        if tol is None:
            ok = got == expected
        else:
            ok = abs(float(got) - float(expected)) <= tol
        if not ok:
            self.failures += 1
        mark = "PASS" if ok else "FAIL"
        self.lines.append(f"[{mark}] {label}: got {got!r}, appendix/run states {expected!r}")
        return ok

    def known(self, label, got, expected, note):
        """A discrepancy found in the appendix itself, reported but not counted as a failure."""
        ok = got == expected
        mark = "PASS" if ok else "DISCREPANCY"
        self.lines.append(f"[{mark}] {label}: got {got!r}, expected {expected!r}" + ("" if ok else f" -- {note}"))
        return ok

    def finish(self):
        print(f"== {self.title} ==")
        for line in self.lines:
            print(line)
        status = "PASS" if self.failures == 0 else f"FAIL ({self.failures} check(s) failed)"
        print(f"RESULT: {status}")
        return 0 if self.failures == 0 else 1
