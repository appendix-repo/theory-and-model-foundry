"""Theory and Model Foundry: reference code for the replication package.

Nothing in this package calls an AI model. It reads the stored run
transcripts, the schema and the ledger, and recomputes every quantity the
technical appendix reports from them. The optional `harness/` folder holds
the separate code for re-running the agent roles against the Claude API.
"""
