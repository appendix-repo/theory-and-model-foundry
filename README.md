# Re-running the agent roles

The transcripts in `runs/` are single, unedited runs (appendix Section 3.0). They cannot be reproduced word for word: a language model gives different output on each call, the model version used on 10 October 2026 was not recorded (the Ledger says only "Claude (Anthropic)"), and the exact prompts were not archived. This folder lets a reviewer re-run any role, or the whole sequence, and judge whether the instruction sets reliably produce outputs of the type the appendix describes.

## Files

| File | What it does |
|---|---|
| `runs.json` | The input bundle of each run: which role section, which lens, which inputs. It follows the inputs each transcript names in its header and the sequence table of Section 3.0. |
| `build_prompts.py` | Builds each prompt: the common preamble and the role's section of instruction set v0.1 as the system prompt; the schema and the inputs as the user message. Writes `harness/prompts/run_XX.md` for inspection. |
| `run_role.py` | Sends a prompt to the Claude API, streams the response, and saves `reruns/run_XX_<UTC time>.md` with a `.json` record of the model that served it, the stop reason, token usage, the prompt's SHA-256 and the prompt's sources. |
| `inspect_rerun.py` | Validates the JSON in a rerun against schema v0 and prints its counts (constructs, assumptions, propositions, derivation statuses, link kinds), for comparison with `checks/chk_04_run_counts.py` on the stored runs. |

## Use

```
pip install -r harness/requirements.txt
export ANTHROPIC_API_KEY=...

python3 harness/build_prompts.py                         # inspect the prompts first
python3 harness/run_role.py 05                           # rerun the Model Builder on the stored Run 01 object
python3 harness/run_role.py 01 02 03 04 05 06 07 08 --chain   # rerun the sequence, each run fed by the reruns before it
python3 harness/inspect_rerun.py reruns/run_01_<time>.md
```

Without `--chain`, every run takes its upstream inputs from the stored transcripts, so each role can be judged on exactly the inputs the original run had. With `--chain`, a run takes its inputs from the latest rerun of the run it depends on.

The default model is `claude-opus-5-5` with adaptive thinking at effort `high`; `--model` and `--effort` change them. Server-side refusal fallback, which can finish a request on a different model, is off by default so that each rerun record names one model; `--allow-fallback` turns it on, and the `.json` record always says which model served the response.

## Reconstruction choices

- Interlocutors get only their own lens row, with `[LENS]` filled in.
- Theory objects are passed as the reading-1 JSON object (the first JSON block of Run 01 or Run 02). The original runs may have been given the whole transcript.
- The Integrator is also given the draft definitions of Section 4.3, because Run 07 quotes them ("draft definition, appendix D §4.3"). Whether the other runs saw any part of the appendix is not recorded.
- The Empirical Validation Designer is given both reading-1 objects and the full transcripts of Runs 03 and 04, which are where the rival explanations it uses come from.
