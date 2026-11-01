"""Run every check and compare its output with the stored output in checks/expected/.

Usage:
    pip install -r requirements.txt
    python3 reproduce.py            # run all checks, compare with checks/expected/
    python3 reproduce.py --update   # overwrite checks/expected/ with this machine's output

Prints one line per check and, at the end, RESULT: PASS only if every check
passes and every output matches the stored one. No AI model is called.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CHECKS = sorted((ROOT / "checks").glob("chk_*.py"))
EXPECTED = ROOT / "checks" / "expected"


def main(update):
    EXPECTED.mkdir(exist_ok=True)
    ok_all = True
    for chk in CHECKS:
        res = subprocess.run([sys.executable, str(chk)], cwd=ROOT, capture_output=True, text=True)
        out = res.stdout
        exp_file = EXPECTED / (chk.stem + ".out")
        if update:
            exp_file.write_text(out, encoding="utf-8")
        same = exp_file.exists() and exp_file.read_text(encoding="utf-8") == out
        passed = res.returncode == 0
        ok_all &= passed and same
        disc = out.count("[DISCREPANCY]")
        print(f"{chk.stem:40s} {'PASS' if passed else 'FAIL'}   output {'matches' if same else 'DIFFERS from'} expected"
              + (f"   ({disc} appendix discrepancy noted)" if disc else ""))
        if res.stderr.strip():
            print(res.stderr.strip())
    print("RESULT:", "PASS" if ok_all else "FAIL")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main("--update" in sys.argv))
