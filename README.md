# Theory and Model Foundry: accompanying repository

This repository accompanies the Stage 1 proposal "Theory and Model Foundry," submitted to the *Organization Science* special issue *AI-Enabled Frontiers in Organizational Science*, and its technical appendix (`FOUNDRY_TECHNICAL_APPENDIX.md`). It holds the instruction sets, the mapping of Foundry roles to Project Lakatos components, the worked transcripts, the draft theory-object schema and the Provenance Ledger trace, so that reviewers can judge the composition directly.

Section references below are to the technical appendix.

## Contents

| Path | Contents | Appendix | Status |
|---|---|---|---|
| `instruction-sets/` | The six Foundry role instruction sets, v0.2 (current) and v0.1 (used for the runs) | §1, §3.0, §6 | **Placeholder: to be added** |
| `mapping/ROLE_TO_LAKATOS_MAPPING.md` | The seventeen scholarly-role agents, the role-by-role mapping, and the coverage audit | §2 | Present |
| `lakatos/LAKATOS_TABLES_1-4.md` | Project Lakatos Tables 1–4: routine agents, cognitive operators, discourse grammar, agent types | Annex C | Present |
| `schema/theory-object.v0.schema.json` | Theory-object JSON Schema, draft v0 (draft 2020-12) | §4, Annex A.1 | Present |
| `schema/context.v0.jsonld` | JSON-LD context for the schema | §4, Annex A.2 | Present |
| `runs/case_inputs.md` | The two prose theory inputs (transaction-cost and resource-dependence accounts of firm boundaries) | Annex B.0 | Present |
| `runs/01_…` to `runs/08_…` | The eight worked transcripts, one per run | §3, Annex B.1–B.8 | Present |
| `runs/09_ledger_trace.json` | The Provenance Ledger trace for Runs 01–08 (11 hash-chained events) | §3.8, Annex B.9 | Present |
| `tools/verify_ledger.py` | Recomputes the Ledger hash chain | §3.8 | Present |
| `tools/check.py` | Informal derivation check used in Run 05 | Annex B.5 | **Placeholder: to be added if available** |

## The runs

| File | Role | Input |
|---|---|---|
| `runs/01_explicator_tce.md` | Explicator | Input A (transaction-cost theory) |
| `runs/02_explicator_rd.md` | Explicator | Input B (resource-dependence theory) |
| `runs/03_interlocutor_institutional_tce.md` | Interlocutor, institutional lens | Transaction-cost reading 1 |
| `runs/04_interlocutor_behavioral_tce.md` | Interlocutor, behavioral lens | Transaction-cost reading 1 |
| `runs/05_model_builder_tce.md` | Model Builder | Transaction-cost reading 1 |
| `runs/06_argument_auditor_tce.md` | Argument Auditor | Input A and transaction-cost reading 1 |
| `runs/07_integrator_tce_rd.md` | Integrator | Transaction-cost and resource-dependence readings 1 |
| `runs/08_empirical_validation_designer_tce.md` | Empirical Validation Designer | Transaction-cost reading 1 and the rivals from Runs 02–04 |

The transcripts are single, unedited runs of instruction set v0.1, produced on 10 October 2026. Each run was executed by a separate instance of Claude (Anthropic), given only the common preamble, its own role's instruction set, the schema and its inputs. No run was repeated or selected from several. Section 3.0 of the appendix describes how the runs were produced and what stood in for the human theorist at the reading-adoption gate.

The agents' "(to verify)" flags are kept in the transcripts as part of the record. Every flagged work is checked, with any correction, in the citation verification table in Section 3.0 of the appendix.

## The Ledger trace

The Ledger is Stage 1 work. The trace in `runs/09_ledger_trace.json` was assembled after the runs, with reconstructed timestamps (Section 3.8). Each event's hash is SHA-256 over the event's JSON, without its `hash` field and with keys sorted, and each event carries the previous event's hash. To check the chain:

```
python tools/verify_ledger.py
```

## Notes

- The `https://foundry.lakatos.example/…` identifiers in the schema, the context and the transcripts are placeholder namespaces, not live URLs.
- In the transcripts, `case_inputs.md` refers to `runs/case_inputs.md`, and `../schema/context.v0.jsonld` resolves from `runs/` to `schema/`.
