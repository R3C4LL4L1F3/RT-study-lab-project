# Production Repository Verification

## Purpose

This document converts RT Study Lab project-history claims into facts traceable to production source, executable evidence and deployment evidence. Source inspection, automated execution, clinical review, accessibility review, deployment verification and manual mechanical/visual review are intentionally distinct evidence categories.

## Canonical production source

- Repository: `R3C4LL4L1F3/RT-study-lab`
- Visibility: Private
- Default branch: `main`
- Original source baseline: `a0495e9fa4e5437d8a027312b618b5c1c389ef94` — `Redesign Shock visual teaching page`
- Current `main`: `d64bde34b69a73c2f71f5a7f5863eca4b5bdbdf6`
- Current commit: `Run production validation on main pushes (#2)`
- Source evidence state: **Verified against production repository**

Do not equate GitHub source state with live ChatGPT Sites deployment state without authoritative Sites deployment/version evidence.

## Current production repository-control state

At the synchronization inspection:

- automatic `Production Validation` on current `main`: **PASS** — Actions run `31311314980`;
- open production pull requests: none;
- open production issues: none;
- production `main` branch protection: **not enabled** (`protected: false`);
- production Git tags: none;
- production GitHub Releases: none;
- retained validation branches:
  - `validation/issue-6-test-baseline`;
  - `validation/issue-7-main-push`;
  - `validation/post-merge-main-verification`.

The validation branches are cleanup candidates only. Do not delete them during project-control synchronization.

Issue #12 records future branch/release-control policy work. Recording that policy does not authorize branch-protection changes, tag/Release creation, deployment changes or branch deletion.

## Automated production validation

Issue #6 established the complete npm-based production validation path and merged it through production PR #1.

Canonical validation contract:

- Node `22.13.0`;
- npm + maintained `package-lock.json`;
- `npm ci`;
- `npm run lint`;
- `npm run build`;
- complete recursive `tests/**/*.test.mjs` discovery/execution;
- dedicated Ventilator historical-P1 regression;
- diagnostic report artifact upload.

Issue #6 evidence:

- validated PR ref: `96b5535f9228c7b01c709386e050ce53e68f14d4`;
- pre-merge Actions run `31309995943`: **PASS**;
- merged production ref: `fb9f23b7442d4dddeac0eab38ed01676aaf914e2`;
- exact-commit post-merge run `31310610948`: **PASS**.

Issue #7 added automatic validation after pushes/merges to `main` through production PR #2.

Issue #7/current-main evidence:

- validated PR ref: `586314ab8e252dba0a479c062a9ade9c96c5d1e6`;
- branch-push run `31310866155`: **PASS**;
- pull-request run `31310877109`: **PASS**;
- current production ref: `d64bde34b69a73c2f71f5a7f5863eca4b5bdbdf6`;
- automatic `main` run `31311314980`: **PASS** for install, lint, build, complete suite, dedicated Ventilator P1 regression, diagnostic artifact and overall job.

Several existing `.test.mjs` files import application `.ts` modules directly. The validation runner uses Node 22.13.0 with explicit `--experimental-strip-types`. Earlier `ERR_UNKNOWN_FILE_EXTENSION` runs were test-harness loader failures rather than application or clinical regressions.

## ChatGPT Sites source/deployment relationship — Issue #8

### Verified source-side relationship

Production contains `.openai/hosting.json`, linking the source project to a provisioned ChatGPT Sites project. The private project identifier is intentionally not reproduced in this public repository.

`build/sites-vite-plugin.ts` packages `.openai/hosting.json` into the build artifact and packages Drizzle migrations when present. `vite.config.ts` combines Vinext, the local Sites packaging plugin and the Cloudflare Vite plugin.

This proves source-side Sites integration. It does **not** identify the active deployed Git revision.

### Current deployment evidence state

Issue #8 status: **P2 High / Tier 1 / BLOCKED**.

The active deployed Git ref remains **Unknown pending authoritative private Sites saved/deployed-version metadata**.

Canonical verification remains:

1. inspect RT Study Lab saved/deployed versions in ChatGPT Sites management;
2. identify the active deployed version;
3. obtain its associated Git commit;
4. verify that commit in private production GitHub history;
5. compare it with current `main`;
6. classify any divergence before any deployment action.

Do not redeploy merely to manufacture evidence. Do not expose private Sites identifiers, internal Sites remotes, private local paths or private URLs unnecessarily.

## Future release relationship

Issue #12 owns policy definition for branch/release controls.

No production tag or GitHub Release should be created until Issue #8 establishes authoritative deployment-to-Git correspondence and the release convention is approved.

Future evidence sequence:

**validated Git commit → saved Sites version → reviewed deployment candidate → explicit deploy → post-deploy ref verification → tag/Release record when policy permits**

A successful GitHub CI run is repository evidence, not deployment evidence.

## Repository architecture observed

### Runtime/build

- Node `>=22.13.0`
- Next.js `16.2.6`
- React/ReactDOM `19.2.6`
- TypeScript `5.9.3`
- Vinext `0.0.50`
- Vite `8.0.13`
- Cloudflare Vite plugin + Wrangler
- Three.js / React Three Fiber / Drei used by chest-trauma 3D
- Drizzle ORM/tooling present; baseline schema intentionally empty
- static/educational assets primarily under `public/`

### Package-management disposition

Production contains `package-lock.json`, `pnpm-lock.yaml` and `pnpm-workspace.yaml`.

DEC-007 establishes npm + maintained `package-lock.json` as canonical reproducible **repository-validation** tooling.

Do not delete/regenerate retained pnpm artifacts until their Sites/Vinext role is verified under PC-004.

## Module verification register

### ECG / ACLS Lab

- Production path: `app/acls/ecg-lab/`
- Route: `/acls/ecg-lab`
- Implementation: **Verified against production repository — implemented**
- Observed architecture includes ECG waveform/rhythm generation, caliper/landmark tooling, Learn/Practice/Exam workflows, patient-state/clinical-scenario layer, pathway/treatment engines and arrest/post-arrest systems.
- Current source-controlled ECG/ACLS tests pass in canonical production validation.
- Independent contemporary clinical validation remains incomplete and is P1 approved.
- Comprehensive accessibility validation remains separate.

### Ventilator Waveform Lab

- Production paths: `app/visual-lab/VentilatorWaveformLab.tsx`, `app/visual-lab/ventilator/`
- Implementation: **Verified against production repository — implemented**
- Source contains deterministic waveform/breath logic, breath records, monitoring calculations, triggering/neural clock, patient profiles, scenario/configuration state, renderer and bounded-history `LiveVentilatorSession`.
- Historical P1 concerns have passing automated regression evidence.
- Issue #3 remains open for learner-facing browser/manual verification.
- Independent Ventilator clinical validation remains incomplete and is P1 approved.

### Interactive Models & Simulation Lab — Shock / Circulation / Oxygen Transport

- Current production path: `app/disease-processes/cardiovascular/shock/`
- Route: `/disease-processes/cardiovascular/shock`
- Current status: **Shock learning page implemented; numerical physiology simulation not implemented**
- Current page contains an explicit simulation-free future-lab integration boundary.
- No Hb→CaO₂→DO₂→VO₂→CvO₂/SvO₂→extraction→oxygen-debt simulation exists.
- No shared general physiology simulation clock/state/invariant/serialization framework was identified.
- `tests/shock-page.test.mjs` passes as a page/content/boundary test, not a numerical physiology-engine validation.

Forward project-control ownership is **Interactive Models & Simulation Lab — Shock / Circulation**.

Issue #9 is **approved for specification only; implementation not approved**. It requires an approved clinical/model contract and approved reusable architecture/model contract before production implementation.

The Ventilator Waveform Lab, ECG & ACLS Lab and 3D Equipment Lab remain separate specialized owners and are not migrated under Interactive Models.

### Equipment catalog

- Production paths: `app/equipment-lab/`, `public/equipment/`
- Status: implemented as image/HTML-overlay interactive lessons
- Historical Shiley Blender/snap-lock 3D work is not production-integrated.
- Dedicated equipment-catalog automated coverage has not been established.

### Chest-trauma 3D

- Production paths: `app/disease-processes/trauma/chest-trauma-3d/`, `public/visual-labs/chest-trauma/`
- Status: integrated production 3D module
- Automated source/model/visual contracts pass.
- Manual browser clipping/intersection, morph quality, responsive behavior, performance, reduced motion and anatomical/educational visual review remain under Issue #5.

### PFT

- Production paths: `app/pft-reports/`, `public/pft-images/`
- Status: implemented
- Source-controlled PFT loop/report contract tests pass.
- Independent clinical review remains separate.

### ABG / Hemodynamics

- Production path: `app/abg-lab/`
- Status: 25-case ABG learning lab implemented; no reusable general hemodynamic simulation engine identified.
- No dedicated ABG automated test file was identified during baseline mapping.

### Respiratory pharmacology

- Production path: `app/medications/`
- Structured monographs/shared source registry are implemented.
- Dedicated medication automated coverage has not been identified; source presence is not independent clinical validation.

## Clinical validation inventory

Production source contains substantial guideline/source evidence and educational boundaries.

**No current independent end-to-end clinical validation artifact tied to current production `main` is established.**

Issue #10 records the approved repeatable clinical-validation framework. Initial P1 module-specific clinical validation begins with ECG/ACLS and Ventilator.

Automated pass results must not be called clinical validation.

## Accessibility validation inventory

Source includes ARIA/live regions, focus/keyboard behavior, semantic structures, responsive code, reduced-motion handling and accessibility-adjacent tests in major modules.

**No comprehensive current accessibility baseline / manual assistive-technology review is established.**

Issue #11 records the approved project-level accessibility-validation framework.

## Mechanical / 3D validation inventory

Chest-trauma automated model/source contracts have passing executable evidence. Manual browser/mechanical/visual validation remains open under Issue #5.

External Blender equipment-model work remains project-history evidence unless deliberately version-controlled and integrated.

## Current unresolved verification / governance questions

1. Which Git commit is associated with the active RT Study Lab Sites deployment? — **Issue #8**
2. Do Ventilator learner-facing browser behaviors agree with passing P1 regressions? — **Issue #3**
3. Does chest-trauma 3D pass current manual browser/mechanical/visual review? — **Issue #5**
4. What implementation-ready clinical/model contract and reusable architecture should govern Interactive Models? — **Issue #9**
5. What repeatable independent clinical-validation protocol should govern safety-sensitive modules? — **Issue #10**
6. What comprehensive accessibility-validation protocol should be used? — **Issue #11**
7. What production branch/release controls should be adopted, and when should they be executed? — **Issue #12**
8. Are retained pnpm files required by Sites/Vinext tooling? — PC-004

## Baseline completion status

- **Production source baseline:** complete
- **Automated repository validation baseline:** complete, merged and green on current `main`
- **Live deployment baseline:** incomplete / blocked under Issue #8
- **Independent clinical-validation baseline:** incomplete
- **Comprehensive accessibility-validation baseline:** incomplete
- **Ventilator browser/manual historical-P1 closure:** incomplete
- **Chest-trauma 3D manual/runtime validation:** incomplete
- **Reusable Interactive Models numerical physiology framework:** not implemented; specification/architecture gate pending

Overall project state remains **stable, but not yet release-mature**.
