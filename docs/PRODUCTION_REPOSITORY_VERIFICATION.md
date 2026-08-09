# Production Repository Verification

## Purpose

This document converts RT Study Lab project-history claims into facts traceable to production source, executable evidence, and deployment evidence. Source inspection, automated execution, clinical review, accessibility review, deployment verification, and manual mechanical/visual review are intentionally distinct evidence categories.

## Canonical production source

- Repository: `R3C4LL4L1F3/RT-study-lab`
- Visibility: Private
- Default branch: `main`
- Original source baseline ref: `a0495e9fa4e5437d8a027312b618b5c1c389ef94`
- Original baseline commit: `Redesign Shock visual teaching page`
- Current `main`: `d64bde34b69a73c2f71f5a7f5863eca4b5bdbdf6`
- Current commit: `Run production validation on main pushes (#2)`
- Source evidence state: **Verified against production repository**

Do not equate GitHub source state with live ChatGPT Sites deployment state without Sites deployment/version evidence.

## Automated production validation

Issue #6 established the complete npm-based production validation path and merged it through production PR #1.

Canonical validation contract:

- Node `22.13.0`
- `npm ci`
- `npm run lint`
- `npm run build`
- complete recursive `tests/**/*.test.mjs` discovery and execution
- dedicated Ventilator historical-P1 regression
- diagnostic report artifact upload

Issue #6 evidence:

- validated PR ref: `96b5535f9228c7b01c709386e050ce53e68f14d4`
- successful pre-merge Actions run: `31309995943`
- merged production ref: `fb9f23b7442d4dddeac0eab38ed01676aaf914e2`
- successful exact-commit post-merge verification run: `31310610948`

Issue #7 added automatic validation after pushes/merges to `main` through production PR #2.

Issue #7 evidence:

- validated PR ref: `586314ab8e252dba0a479c062a9ade9c96c5d1e6`
- successful branch-push run: `31310866155`
- successful pull-request run: `31310877109`
- merged production ref: `d64bde34b69a73c2f71f5a7f5863eca4b5bdbdf6`
- automatic `main` push run: `31311314980`
- automatic `main` run result: **PASS** for install, lint, build, complete suite, dedicated Ventilator P1 regression, diagnostic artifact, and overall job

Several existing `.test.mjs` files import application `.ts` modules directly. The validation runner therefore invokes Node 22.13.0 with explicit `--experimental-strip-types`. Earlier `ERR_UNKNOWN_FILE_EXTENSION` runs were test-harness loader failures rather than application or clinical regressions.

## ChatGPT Sites source/deployment relationship — Issue #8

### Production-source evidence

Production contains `.openai/hosting.json`. This file links the local source project to a provisioned ChatGPT Sites project. The private Sites project identifier is intentionally not reproduced in this public project-control repository.

Git history shows the hosting-linkage file has existed since the initial `Build RT Study Lab` commit.

`build/sites-vite-plugin.ts` packages `.openai/hosting.json` into the build artifact under `dist/.openai/hosting.json` and also packages Drizzle migrations when present.

`vite.config.ts` imports the hosting configuration and combines Vinext, the local Sites packaging plugin, and the Cloudflare Vite plugin.

These facts prove a source-side Sites integration. They do **not** identify the currently deployed source revision.

### Official platform evidence

Current official ChatGPT Sites documentation establishes that:

1. a Sites project links a local source project to hosting managed through Sites, with the linkage stored in `.openai/hosting.json`;
2. Sites publishing has two distinct stages: **save a version** and **deploy a version**;
3. for a local source project, ChatGPT associates the saved version with the Git commit used for the build;
4. saved versions can be listed/inspected to identify previous deployment candidates;
5. deploying publishes the selected saved version; changing GitHub source by itself is not proof of a deployment.

### Canonical deployment-verification method

To verify the live RT Study Lab deployment:

1. open the RT Study Lab Site in ChatGPT Sites management;
2. list/inspect saved versions;
3. identify the version currently deployed;
4. obtain the Git commit associated with that version;
5. verify that commit exists in the private production GitHub history;
6. compare the deployed commit with current production `main`;
7. classify any difference before changing the live Site.

Evidence states:

- **Verified deployed ref** — Sites version metadata explicitly associates the active deployment with a Git commit present in GitHub.
- **GitHub ahead of deployment** — current GitHub `main` contains commits newer than the deployed Sites version.
- **Deployment ahead/diverged** — the deployed commit is not current GitHub `main` or is not reachable from expected GitHub history; investigate before modifying anything.
- **Unknown** — Sites version metadata has not been retrieved.

Current live deployment ref: **Unknown pending private Sites version inspection**.

Do not redeploy simply to manufacture evidence. Do not expose the private Sites project identifier, internal Sites Git remote, private local filesystem paths, or private Site URL in public project-control records unnecessarily.

### Future release rule

Once Issue #8 establishes the active deployment ref, use this release sequence:

**validated Git commit -> saved Sites version -> reviewed deployment candidate -> explicit deploy -> post-deploy version/ref verification**

A successful GitHub CI run is a prerequisite for a reviewed production source revision, but it is not deployment evidence by itself.

## Repository architecture observed

### Runtime/build

- Node engine: `>=22.13.0`
- Next.js `16.2.6`
- React/ReactDOM `19.2.6`
- TypeScript `5.9.3`
- Vinext `0.0.50`
- Vite `8.0.13`
- Cloudflare Vite plugin and Wrangler present
- Three.js, React Three Fiber and Drei actively used by chest-trauma 3D
- Drizzle ORM/tooling present; baseline schema intentionally empty
- static/educational assets primarily under `public/`

### Package-management disposition

Production contains `package-lock.json`, `pnpm-lock.yaml`, and `pnpm-workspace.yaml`.

Issue #6 established **npm as the canonical reproducible validation package manager** because the maintained npm lockfile tracks current production dependencies. The pnpm artifacts are intentionally retained until their Sites/Vinext role is proven safe to change.

## Module verification register

### ECG Rhythm / ACLS Lab

- Production path: `app/acls/ecg-lab/`
- Route: `/acls/ecg-lab`
- Implementation: **Verified against production repository — implemented**
- Observed architecture includes the 500 Hz ECG engine, source-defined rhythm library, caliper/landmark tooling, Learn/Practice/Exam workflows, patient-state/clinical-scenario layer, pathway/treatment engines, and arrest/post-arrest systems.
- Current source-controlled ECG/ACLS tests pass within the canonical complete production validation suite.
- Passing software tests are not independent current AHA clinical validation or comprehensive accessibility conformance.

### Ventilator Waveform Lab

- Production paths: `app/visual-lab/VentilatorWaveformLab.tsx`, `app/visual-lab/ventilator/`
- Implementation: **Verified against production repository — implemented**
- Source contains deterministic waveform/breath logic, breath records, monitoring calculations, triggering/neural clock, patient profiles, scenario/configuration state, renderer, provenance helpers and bounded-history `LiveVentilatorSession`.
- Tests include engine, Session 3, Session 3.5 and Session 3.5.2 suites.
- Historical P1 concerns have passing automated regression evidence for double-trigger/minute-ventilation behavior, dynamic-compliance validity, immutable mode provenance, and expiratory-hold scheduling/rescheduling.
- Issue #3 remains open for learner-facing browser verification.

### Shock / Oxygen Transport

- Production path: `app/disease-processes/cardiovascular/shock/`
- Route: `/disease-processes/cardiovascular/shock`
- Status: **Shock learning page implemented; physiology simulation not implemented**
- The current page explicitly contains an integration boundary rather than a coupled circulation engine.
- Hb->CaO2->DO2->VO2->CvO2/SvO2->extraction->oxygen-debt simulation is absent at the verified source ref.
- Automated Shock page tests pass.

### Equipment catalog

- Production paths: `app/equipment-lab/`, `public/equipment/`
- Status: **implemented as image/HTML-overlay interactive lessons**
- Historical Shiley Blender/snap-lock 3D work is not production-integrated.
- Dedicated equipment-catalog automated coverage has not been established.

### Chest-trauma 3D

- Production paths: `app/disease-processes/trauma/chest-trauma-3d/`, `public/visual-labs/chest-trauma/`
- Status: **integrated production 3D module**
- Automated source/model/visual contracts pass.
- Manual browser clipping/intersection, morph visual quality, responsive behavior, performance, reduced-motion, and anatomical/educational visual review remain under Issue #5.

### PFT

- Production paths: `app/pft-reports/`, `public/pft-images/`
- Status: **implemented**
- Source-controlled PFT loop/report contract tests pass.
- Independent clinical review remains separate.

### ABG / Hemodynamics

- Production path: `app/abg-lab/`
- Status: **25-case ABG learning lab implemented; no general hemodynamic calculation engine identified**.
- No dedicated ABG automated file was identified during baseline mapping.

### Disease-process modules

Generic disease records include ARDS, COPD exacerbation, status asthmaticus, pneumonia, acute pulmonary edema, pulmonary embolism, pulmonary fibrosis, cystic fibrosis, neuromuscular respiratory failure and bronchiectasis. Specialized modules include Shock, Stroke, Burns, Chest Trauma, traumatic brain injury and trauma content.

Selected specialized tests pass within the canonical complete suite; comprehensive automated coverage of every disease record is not established.

### Respiratory pharmacology

- Production path: `app/medications/`
- Status: **implemented**
- Structured monographs and shared source registry are present.
- Dedicated medication automated coverage has not been identified; reference presence is not independent clinical validation.

## Clinical validation inventory

Production source contains substantial guideline/source evidence and educational boundaries. No current independent end-to-end clinical validation artifact tied to current production `main` has been established.

Automated pass results must not be called clinical validation.

## Accessibility validation inventory

Source includes ARIA/live regions, focus/keyboard behavior, semantic structures, responsive code, reduced-motion handling and accessibility-adjacent tests in major modules.

No comprehensive current WCAG conformance report or documented manual assistive-technology review is established.

## Mechanical / 3D validation inventory

Chest-trauma automated model/source contracts have passing executable evidence. Manual browser/mechanical/visual validation remains open under Issue #5.

External Blender equipment-model work remains project-history evidence unless deliberately version-controlled and integrated.

## Security and repository hygiene

Positive controls include:

- `.env*`, `node_modules`, runtime/build state and PEM files ignored;
- no tracked environment file identified in the production tree;
- `.openai/hosting.json` contains project linkage metadata but no credential was observed during source inspection;
- dependency/build output such as `node_modules` is not source-controlled;
- third-party chest-trauma asset attribution is source-controlled;
- production validation workflow uses `contents: read`, no deployment credentials, and performs no deployment.

Current hygiene items:

- pnpm artifacts remain pending deployment-aware disposition;
- production README remains starter-oriented;
- deployment release records should be added after Issue #8 establishes the saved-version/Git-commit correspondence.

## Current unresolved verification questions

1. Which Git commit is associated with the currently deployed RT Study Lab Sites version? — **Issue #8**
2. Do Ventilator learner-facing browser behaviors agree with the passing automated P1 regressions? — **Issue #3**
3. Does chest-trauma 3D pass current manual browser/mechanical/visual review across supported devices? — **Issue #5**
4. What independent clinical-review cadence/evidence should govern safety-sensitive modules?
5. What comprehensive accessibility-validation workflow should be adopted?
6. Are the retained pnpm files required by the Sites/Vinext development/deployment environment?

## Baseline completion status

The **production source baseline is complete**.

The **automated validation baseline is complete, merged, and automatically re-runs after production `main` updates**.

The **live deployment baseline remains incomplete** until Issue #8 retrieves the active Sites version's associated Git commit.

Runtime/browser, clinical, accessibility and manual 3D validation remain separate follow-on evidence categories.
