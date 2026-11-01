# Theory and Model Foundry: replication package

This repository accompanies the Stage 1 proposal "Theory and Model Foundry," submitted to the Organization Science Special Issue *AI-Enabled Frontiers in Organizational Science*, and its technical appendix (a copy is in `technical-appendix/FOUNDRY_TECHNICAL_APPENDIX.md`). Section numbers below refer to the appendix. The repository is anonymized for review.

It contains everything the appendix and the proposal cite: the six role instruction sets, the draft theory-object schema, the transcripts of the eight worked runs, the Provenance Ledger trace, and the Project Lakatos component tables. It adds code that recomputes, from those files, every number, count and structural claim the appendix reports, and a harness for re-running the agent roles.

**What was run, and by whom.** Runs 01 to 08 were produced on 10 October 2026 by separate instances of Claude (Anthropic), one per run, each given the common preamble, its role's instruction set (v0.1), the schema and its inputs (Section 3.0). No human theorist took part: Claude stood in for the theorist at the reading-adoption gate, and the Ledger records this (event ev:5). The Ledger trace was assembled after the runs, with reconstructed timestamps (Section 3.8).

## Quick start

The checks need Python 3.10 or later with `jsonschema` and `sympy`. They were run with Python 3.13, jsonschema 4.26 and SymPy 1.14. They call no AI model and take a few seconds.

```
pip install -r requirements.txt
python3 reproduce.py
```

`reproduce.py` runs the eleven checks in `checks/`, compares each one's output with the stored output in `checks/expected/`, and ends with `RESULT: PASS` only if every check passes and every output matches. Each check can also be run on its own, for example `python3 checks/chk_05_inferential_distance.py`.

## What is here

| Folder | Contents | Appendix |
|---|---|---|
| `instruction-sets/` | Role instruction sets: v0.2 (current) and v0.1 (used for the runs). They differ only in the lens table. | 1, 1.8 |
| `schema/` | `theory-object.v0.schema.json` (JSON Schema draft 2020-12) and `context.v0.jsonld` | 4, Annex A |
| `runs/` | `case_inputs.md` (Inputs A and B), the eight transcripts `01` to `08`, and `09_ledger_trace.json` | 3, Annex B |
| `lakatos/` | Project Lakatos Tables 1 to 4 | 2, Annex C |
| `foundry/` | Shared code: loaders, schema validation, the Ledger's hash rule, the Section 4.3 quantities | 1.7, 4 |
| `checks/` | The eleven checks and their stored outputs (`expected/`) | see the map below |
| `data/` | Values transcribed from the runs for the checks (`run07_pairs.json`), and the citation table extracted from Section 3.0 (`citation_verification.csv`) | 3.0, 3.3 |
| `extracted/` | The JSON objects inside the transcripts as standalone files: both reading-1 theory objects, the reading deltas, both ensembles, the AlignmentMap. Written by Check 02. | 3, Annex B |
| `harness/` | Code to rebuild each run's prompt and re-run it against the Claude API | 3.0 |
| `docs/` | The technical appendix | |

## Map from results to code

Every row is a claim in the appendix (or, where marked, the proposal) and the check that recomputes it.

| Claim | Where stated | Check |
|---|---|---|
| Annex B reproduces `runs/` unedited; Annex A reproduces `schema/`; Annex B.9 is the Ledger file | Annex A, B | `chk_01` |
| v0.2 differs from v0.1 only in the lens table; Section 1.8 is the v0.2 table | 1.8, 3.0 | `chk_01` |
| The runs' theory objects, ensembles and AlignmentMap validate against schema v0 (0 errors) | 4, 3.3, Run 07 §6 | `chk_02` |
| All eleven Ledger events validate against the schema | 3.8 | `chk_02` |
| `adoptedReading` is unset in both ensembles; no derivation is `closed` | 3.0, 1.4 | `chk_02` |
| Which Section 4.1 design principles the JSON Schema enforces by itself | 4.1 | `chk_02` |
| The Ledger is SHA-256 hash-chained over canonical JSON including the previous hash; eleven events with the actors, actions and links of the Section 3.8 table; ev:5 passed by Claude standing in for the theorist | 1.7, 3.0, 3.8 | `chk_03` |
| Run 01: 19 constructs, each with all four inferential-role fields; 13 assumptions (7 core, 6 auxiliary); 7 propositions; P1 accommodation, P5 and P6 novel; 3 readings; 4 pivotal differences; A13 a surfaced auxiliary | 3.1, 3.7 | `chk_04` |
| Run 02: 19 constructs; 10 assumptions (4 core); 9 propositions; 3 readings | 3.1 | `chk_04` |
| Run 02: the four dyadic quantities have only two independent dimensions | 3.1 | `chk_08` |
| Run 01 ensemble dispersion 0.43 (the run's own proxy) | Run 01 | `chk_08` |
| Run 03: 10 objections, 1 fatal, 7 damaging, 2 minor. Run 04: 9 objections, 1, 6, 2 | 3.2 | `chk_04` |
| Run 05: 11 derivation attempts, 5 asserted, 5 open, 1 refuted, none closed; surfaced A16 to A21 | 3.4 | `chk_04` |
| Run 05: the D6 counter-example (hybrid never chosen at s = (1, 0.5, 0), β_H = 1, β_X = 0.6); A18 as the chord condition; P6 refuted on the probability scale (P ≈ 0.85, cross-partial ≈ −0.10; +0.23 at (1, 1)); the A19 counter-example φ = k + u k e^(−k); D8, D12, D13; the A21 expansion (s̄ = 0.73, band (0.50, 2.33), width 0.17, empty by u = 2.5); the contraction removing A1 | 3.4, Run 05 §4 to §7 | `chk_06` |
| Run 06: 11 Toulmin steps, none with backing; 11 warrant gaps; 5 inference-mode mismatches; one defeater per warrant | 3.5 | `chk_04` |
| Run 07: 1 bridge, 1 rivalry, 3 complementarities, 2 equivocations, 1 pair with no alignment | 3.3 | `chk_04` |
| Run 07: inferential distance 13/17 ≈ 0.76, its sensitivity values (0.875, 0.75, 0.88), and 0.38 under the graded weights; pair weights recomputed from the theory objects | 3.3, 3.9, 4.3 | `chk_05` |
| Run 08: 7 risky predictions, 3 contrasts on which all agree, 7 designs, D1 ranked first and D6 last | 3.6 | `chk_04` |
| Run 08: every power figure (588 and 823 per arm for D1; 1,018 and 1,111 for D2; 71,000 and 106,500 pair-years and the RR 0.72 minimum detectable effect for D3, which is underpowered; 95, 136, 190, 543) | 3.6 | `chk_07` |
| Every Table 4 agent and Table 2 operator is used by at least one role; 10 of 12 routine agents are used; Sections 2.1, 2.2 and 2.3 agree | 2.1 to 2.3 | `chk_09` |
| Citation table: 36 works, 33 supported, 3 partly supported; each work is cited in the runs listed for it | 3.0 | `chk_10` |
| The Section 4.3 quantities are computable directly from the schema (values shown are new, not reported in the appendix) | 4.3, 1.4 | `chk_11` |

The proposal's own empirical statements (Sections 1 to 2: that the Explicator returns candidate readings separating constructs from measurement commitments and core from auxiliary assumptions, that the Interlocutors object in the voice of their tradition, that an Integrator run locates bridges and conflicts) rest on the same runs, and the checks above cover the countable parts of them.

## Inferred values and operational choices

Three values used by the checks are not stated in the runs and were recovered so that the runs' numbers come out. Each is printed as `[INFO]` where it is used.

- **Run 05, item 4** (Pr(H | k = 0) = 0.1745): β_X = 0.3, β_H = 1, σ = 1.
- **Run 05, item 5** (the A21 expansion): the hybrid-safeguard schedule s_X(u) = 0.3 + 0.2u.
- **Run 07, pair weights**: the Integrator's rule (count `licenses` entries; an entry that says the construct licenses nothing, and a scope condition, count 0) is implemented in `foundry/metrics.py` and reproduces all eight stated weights.

Run 05 cites an informal numeric check from a script that was not kept. `checks/chk_06_model_builder.py` is a new script written for this repository. It confirms the arithmetic and the counter-examples, and it does not change any derivation status: the appendix's statement that no derivation can be `closed` before the Stage 1 checking backend exists still describes the Foundry.

## What a script cannot re-run

- **The agent runs.** A model gives different output each time, and the model version used on 10 October 2026 was not recorded. The prompts given to the runs were not archived either. `harness/` rebuilds each prompt from the instruction sets, the schema and the inputs each run names, and can re-run any role, or the whole sequence, against the Claude API. See `harness/README.md`.
- **The citation verification** in Section 3.0, which was a manual check against the published record. `chk_10` checks the table's internal consistency and its fit to the transcripts, not the verdicts.
- **The validation studies** of Section 5 (retrospective validity, reliability at scale, prospective value in use). They are designed and will be pre-registered in Stage 1; there are no results yet.

## Discrepancies found

Building the checks turned up two small inconsistencies in the appendix text. They are reported by the checks as `[DISCREPANCY]` and do not count as failures.

1. **Section 2.1 versus 2.2 and 2.3 (Meta-Analyzer).** Section 2.1 says L9 Meta-Analyzer feeds the Empirical Validation Designer and the Interlocutors (evidence); Sections 2.2 and 2.3 list it only under the Empirical Validation Designer. (`chk_09`)
2. **Citation table, Casciaro & Piskorski 2005.** The table lists Runs 02, 07 and 08. Run 07 refers to the work only through Run 02 ("the indicator Run 02 names") and does not name it. (`chk_10`)

`chk_01` also prints the appendix's word count for information: Sections 0 to 6 have about 11,800 whitespace-separated words, against "about 10,500" in the front matter.

## Licence

The code (`foundry/`, `checks/`, `harness/`, `reproduce.py`) is released under the MIT License (`LICENSE`). The instruction sets, schema, transcripts, Ledger trace and data files are released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).
