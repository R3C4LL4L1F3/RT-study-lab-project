# RTSL AI Harness V0 Audit Contract

Serialization profile: `RTSL-CANONICAL-RECORD-1`  
Hash: SHA-256

Canonical JSON rules:

- UTF-8;
- recursive lexicographic object-key order;
- array order preserved;
- no insignificant whitespace;
- explicit `null` when present in the payload;
- lowercase JSON booleans;
- integer decimal representation;
- UTC ISO-8601 normalization for timestamp fields;
- canonical uppercase enums;
- no comments, NaN, Infinity, or implementation object repr.

Separate SHA-256 identities are produced for:

1. normalized input snapshot;
2. deterministic findings;
3. deterministic result payload;
4. final audit content.

The human-readable console summary is never a hash source.

## Mandatory final recheck

Immediately before successful output, V0 re-evaluates the original normalized task and compares the final candidate recommendation against fresh deterministic policy. A corrupted recommendation cannot be emitted as legal advancement.

Acceptance test: `TEST-AIH-V0-FINAL-RECHECK-001`.
