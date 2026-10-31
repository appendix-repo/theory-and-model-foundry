# Still needed before posting (delete this file once done)

Mihnea, these are the files the appendix names but doesn't reproduce, so they have to come from the original runs. Each has a placeholder at its path that says what it is.

## Instruction sets

- [ ] `instruction-sets/FOUNDRY_ROLE_INSTRUCTION_SETS.md` (v0.2, current). The appendix only reproduces the instruction sets "in substance" (Section 1), so the full text exists nowhere else.
- [ ] `instruction-sets/FOUNDRY_ROLE_INSTRUCTION_SETS_v0.1.md`, the version used for Runs 01 to 08. It must match what the runs were given. Per Sections 1.8 and 3.0, it should differ from v0.2 only in the lens table.

Once both are in, delete `instruction-sets/README.md`.

## Code

- [ ] `tools/check.py`, the finite-difference and grid check from Run 05. The transcript calls it `scratchpad/mb/check.py` and says it was "not published." If it still exists, add it here and confirm it reproduces the results reported in the Run 05 transcript. If it's gone, delete `tools/README.md` and the README's `check.py` row.

## Please check

- [ ] **Files taken from the appendix.** Everything else here was copied from the appendix: `runs/case_inputs.md` (Annex B.0), the eight transcripts `runs/01_…` to `runs/08_…` (Annex B.1 to B.8), `runs/09_ledger_trace.json` (Annex B.9), the two `schema/` files (Annex A), `lakatos/LAKATOS_TABLES_1-4.md` (Annex C) and `mapping/ROLE_TO_LAKATOS_MAPPING.md` (Section 2). The transcripts are unedited, except that the heading levels the appendix had lowered are restored. If you have the original run files, use yours. If yours differ from the appendix, the appendix has to change to match.
- [ ] **File names.** The appendix names only `runs/09_ledger_trace.json`, and the transcripts name `case_inputs.md`. The other run file names (`01_explicator_tce.md` and so on) are mine. Rename them to match your files, and update the README's tables if you do.
- [ ] **Case author.** The Ledger records the two case inputs as written by a human "case author." If a model drafted them, the entries in `runs/09_ledger_trace.json` and Annex B.9 must change, and the hash chain has to be recomputed. Run `python tools/verify_ledger.py` afterwards to confirm the chain still validates.
- [ ] **Summarizer entry.** Table 1 in `lakatos/LAKATOS_TABLES_1-4.md` completes the Summarizer/Conclusion Builder entry as "…or in the creation of its concluding section." It breaks off in the source. Please confirm or correct it, here and in Annex C.
- [ ] **Schema version.** The schema file is named `v0`, and its `$id` and title say v0. But its `schemaVersion` is `"0.1-draft"`, and appendix Section 4 calls it "draft v0.1." Settle on one. If you rename the file, the appendix's references to it (Section 4 and Annex A) change too.
- [ ] **Repository link.** The proposal and the appendix's opening note both give https://github.com/appendix-repo/theory-and-model-foundry. Make sure the repository is public at that address. Also check that the commit history, contributor list and account profile don't name us.
- [ ] **Licence.** None has been added yet.
