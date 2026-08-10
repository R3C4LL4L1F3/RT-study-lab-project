# AIH-GH-RO-001 — GitHub Read-Only Contract

The initial V0 offline evaluator requires no GitHub connection or credential.

A future V0.x GitHub evidence adapter may be enabled only after separate reviewed permission derivation. Its interface must be evidence-only and must expose no repository mutation operation.

The V0 source includes only a disabled extension point and a read-only protocol contract. It contains no GitHub write client, push path, issue/PR mutation method, release/deployment method, or permission configuration.

If a future integration cannot verify technical read-only capability, repository-connected execution fails closed or uses supplied offline evidence.
