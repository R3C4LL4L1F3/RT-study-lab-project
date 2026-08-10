# RTSL AI Harness V0 Frozen Rule Pack

Policy profile: `RTSL-AIH-V0-POLICY-1`.

Stable rule IDs implemented:

- Structural: `AIH-V0-R001`–`R005`
- PAUSED/BLOCKED: `R010`–`R011`
- Transitions: `R020`–`R023`
- Gates: `R030`–`R035`
- No-gate-downgrade: `R040`–`R042`
- Approvals: `R050`–`R053`
- QA independence: `R060`–`R061`
- Validation gap / defect: `R070`–`R074`
- Contradictions: `R080`–`R082`
- Read-only boundary: `R090`

The evaluator is deterministic. Human approval cannot legalize a deterministic policy violation. Missing mandatory Tier 2/3 evidence/gates fail closed as incomplete rather than being invented or silently downgraded.

`RTSL-AIH-QA-004` is implemented by `R073`/`R074`: verified tool evidence may support defect assessment, but it cannot alone establish an authoritative `CONFIRMED_DEFECT`.

The frozen normative transition matrix is source-controlled in `config/ai_harness/transition-matrix.v1.json`.
