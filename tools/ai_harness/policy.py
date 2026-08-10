from __future__ import annotations

from typing import Any

from .transitions import (
    TERMINAL_STATES,
    previous_state_provenance_valid,
    resume_target_valid,
    transition_enumerated,
)

RULE_IDS = [
    "AIH-V0-R001", "AIH-V0-R002", "AIH-V0-R003", "AIH-V0-R004", "AIH-V0-R005",
    "AIH-V0-R010", "AIH-V0-R011",
    "AIH-V0-R020", "AIH-V0-R021", "AIH-V0-R022", "AIH-V0-R023",
    "AIH-V0-R030", "AIH-V0-R031", "AIH-V0-R032", "AIH-V0-R033", "AIH-V0-R034", "AIH-V0-R035", "AIH-V0-R036",
    "AIH-V0-R040", "AIH-V0-R041", "AIH-V0-R042",
    "AIH-V0-R050", "AIH-V0-R051", "AIH-V0-R052", "AIH-V0-R053", "AIH-V0-R054",
    "AIH-V0-R060", "AIH-V0-R061",
    "AIH-V0-R070", "AIH-V0-R071", "AIH-V0-R072", "AIH-V0-R073", "AIH-V0-R074",
    "AIH-V0-R080", "AIH-V0-R081", "AIH-V0-R082",
    "AIH-V0-R090",
]


def rr(rule_id: str, status: str, reason: str, severity: str = "ERROR") -> dict[str, str]:
    return {"rule_id": rule_id, "status": status, "severity": severity, "reason": reason}


def gate_map(task: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {g["gate_id"]: g for g in task["gates"]}


def required_gate_failures(task: dict[str, Any]) -> list[str]:
    return [
        g["gate_id"] for g in task["gates"]
        if g["obligation"]["required"] and g["execution"]["state"] != "PASS"
    ]


def required_gate_completeness_issues(task: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    for gate in task["gates"]:
        if not gate["obligation"]["required"] or gate["execution"]["state"] != "PASS":
            continue
        disposition = gate.get("disposition") or {}
        actor = disposition.get("actor") or {}
        authority = gate.get("authority") or {}
        if disposition.get("decision") != "PASS":
            issues.append(f"{gate['gate_id']}: PASS execution lacks PASS authority disposition")
            continue
        if actor.get("actor_type") not in {"HUMAN", "VERIFIED_GOVERNED_SYSTEM"}:
            issues.append(f"{gate['gate_id']}: PASS execution lacks authoritative disposition actor")
            continue
        if authority.get("owner_role") and actor.get("authority_role") != authority.get("owner_role"):
            issues.append(f"{gate['gate_id']}: disposition actor role does not match gate authority")
            continue
        if gate["gate_id"] == "CLINICAL_EVIDENCE" and not disposition.get("evidence_refs"):
            issues.append("CLINICAL_EVIDENCE: required PASS lacks authoritative evidence reference")
    return issues


def _gate_actor_id(task: dict[str, Any], gate_id: str) -> str | None:
    gate = gate_map(task).get(gate_id)
    if not gate:
        return None
    actor = ((gate.get("disposition") or {}).get("actor") or {})
    return actor.get("actor_id")


def _required_transition_approval(task: dict[str, Any], config: Any) -> dict[str, str] | None:
    target = task.get("requested_transition")
    if not target:
        return None
    key = f"{task['work_state']}->{target}"
    return config.transitions.get("approval_requirements", {}).get(key)


def _has_qualifying_approval(task: dict[str, Any], requirement: dict[str, str], config: Any) -> bool:
    required_type = requirement["approval_type"]
    required_decision = requirement["decision"]
    allowed_roles = set(config.roles["approval_authority"].get(required_type, []))
    for approval in task["approvals"]:
        actor = approval["actor"]
        if (
            approval["approval_type"] == required_type
            and approval["decision"] == required_decision
            and actor.get("actor_type") == "HUMAN"
            and actor.get("authority_role") in allowed_roles
        ):
            return True
    return False


def evaluate_rules(task: dict[str, Any], config: Any) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    for rid in ("AIH-V0-R001","AIH-V0-R002","AIH-V0-R003","AIH-V0-R004","AIH-V0-R005"):
        out.append(rr(rid, "PASS", "validated by schema/kernel profile", "INFO"))

    state = task["work_state"]
    if state == "PAUSED":
        pause = task.get("pause") or {}
        missing = [k for k in ("reason", "resume_condition", "previous_state") if not pause.get(k)]
        provenance_ok = not missing and previous_state_provenance_valid(task, config.transitions)
        reason = "PAUSED missing: " + ", ".join(missing) if missing else ("PAUSED contract satisfied" if provenance_ok else "PAUSED previous_state is not a legal predecessor")
        out.append(rr("AIH-V0-R010", "PASS" if not missing and provenance_ok else "FAIL", reason))
    else:
        out.append(rr("AIH-V0-R010", "NOT_APPLICABLE", "task is not PAUSED", "INFO"))

    if state == "BLOCKED":
        blocker = task.get("blocker") or {}
        missing = [k for k in ("description", "owner", "unblock_condition", "previous_state") if not blocker.get(k)]
        provenance_ok = not missing and previous_state_provenance_valid(task, config.transitions)
        reason = "BLOCKED missing: " + ", ".join(missing) if missing else ("BLOCKED contract satisfied" if provenance_ok else "BLOCKED previous_state is not a legal predecessor")
        out.append(rr("AIH-V0-R011", "PASS" if not missing and provenance_ok else "FAIL", reason))
    else:
        out.append(rr("AIH-V0-R011", "NOT_APPLICABLE", "task is not BLOCKED", "INFO"))

    requested = task.get("requested_transition")
    if requested:
        enum_ok = transition_enumerated(task, requested, config.transitions)
        out.append(rr("AIH-V0-R020", "PASS" if enum_ok else "FAIL", f"{state} -> {requested} is {'enumerated' if enum_ok else 'not enumerated'}"))
        terminal_fail = state in TERMINAL_STATES
        out.append(rr("AIH-V0-R021", "FAIL" if terminal_fail else "PASS", "ordinary transition from terminal state is forbidden" if terminal_fail else "current state is nonterminal"))
        if state == "PAUSED":
            ok = resume_target_valid(task, requested, config.transitions)
            out.append(rr("AIH-V0-R022", "PASS" if ok else "FAIL", "PAUSED transition/resume prerequisites satisfied" if ok else "PAUSED resume lacks legal prior-state provenance or satisfied condition evidence"))
            out.append(rr("AIH-V0-R023", "NOT_APPLICABLE", "task is not BLOCKED", "INFO"))
        elif state == "BLOCKED":
            ok = resume_target_valid(task, requested, config.transitions)
            out.append(rr("AIH-V0-R023", "PASS" if ok else "FAIL", "BLOCKED transition/resume prerequisites satisfied" if ok else "BLOCKED resume lacks legal prior-state provenance or satisfied unblock evidence"))
            out.append(rr("AIH-V0-R022", "NOT_APPLICABLE", "task is not PAUSED", "INFO"))
        else:
            out.append(rr("AIH-V0-R022", "NOT_APPLICABLE", "task is not PAUSED", "INFO"))
            out.append(rr("AIH-V0-R023", "NOT_APPLICABLE", "task is not BLOCKED", "INFO"))
    else:
        for rid in ("AIH-V0-R020","AIH-V0-R021","AIH-V0-R022","AIH-V0-R023"):
            out.append(rr(rid, "NOT_APPLICABLE", "no requested transition", "INFO"))

    gates = gate_map(task)
    minimum = set(config.gates["risk_minimum_required_gates"].get(task["risk_tier"], []))
    missing_minimum = sorted(minimum - set(gates))
    nonrequired_minimum = sorted(gid for gid in minimum if gid in gates and not gates[gid]["obligation"]["required"])
    completeness_issues = required_gate_completeness_issues(task)
    r030_issues = []
    if missing_minimum:
        r030_issues.append("missing minimum required gate(s): " + ", ".join(missing_minimum))
    if nonrequired_minimum:
        r030_issues.append("risk-required gate(s) represented as non-required: " + ", ".join(nonrequired_minimum))
    r030_issues.extend(completeness_issues)
    out.append(rr("AIH-V0-R030", "FAIL" if r030_issues else "PASS", "; ".join(r030_issues) if r030_issues else "minimum risk gate obligations and authoritative PASS dispositions are present"))

    missing_authority = sorted(
        g["gate_id"] for g in task["gates"]
        if g["obligation"]["required"] and not (g.get("authority") or {}).get("owner_role")
    )
    out.append(rr("AIH-V0-R036", "FAIL" if missing_authority else "PASS", "required gate authority missing: " + ", ".join(missing_authority) if missing_authority else "all required gates identify an authority owner"))

    req_fail = required_gate_failures(task)
    pre_rel_fail = requested == "READY_FOR_RELEASE" and bool(req_fail)
    comp_fail = requested == "COMPLETE" and bool(req_fail)
    out.append(rr("AIH-V0-R031", "FAIL" if pre_rel_fail else ("PASS" if requested == "READY_FOR_RELEASE" else "NOT_APPLICABLE"), "READY_FOR_RELEASE requires all mandatory gates PASS" if pre_rel_fail else ("mandatory pre-release gates PASS" if requested == "READY_FOR_RELEASE" else "target is not READY_FOR_RELEASE"), "ERROR" if pre_rel_fail else "INFO"))
    out.append(rr("AIH-V0-R032", "FAIL" if comp_fail else ("PASS" if requested == "COMPLETE" else "NOT_APPLICABLE"), "COMPLETE requires all mandatory gates PASS" if comp_fail else ("mandatory completion gates PASS" if requested == "COMPLETE" else "target is not COMPLETE"), "ERROR" if comp_fail else "INFO"))
    out.append(rr("AIH-V0-R033", "PASS", "READY_FOR_RELEASE and COMPLETE are distinct canonical states", "INFO"))

    qa = gates.get("QA")
    out.append(rr("AIH-V0-R034", "PASS", "implementation and QA remain independent gate records", "INFO"))
    tier3_qa_fail = task["risk_tier"] == "TIER_3" and requested == "COMPLETE" and (not qa or qa["execution"]["state"] != "PASS")
    out.append(rr("AIH-V0-R035", "FAIL" if tier3_qa_fail else "PASS", "Tier 3 COMPLETE prohibited while QA is not PASS" if tier3_qa_fail else "Tier 3 QA completion invariant satisfied"))

    illegal_not_required = [g["gate_id"] for g in task["gates"] if g["obligation"]["required"] and g["execution"]["state"] == "NOT_REQUIRED"]
    out.append(rr("AIH-V0-R040", "FAIL" if illegal_not_required else "PASS", "required gate(s) illegally marked NOT_REQUIRED: " + ", ".join(illegal_not_required) if illegal_not_required else "no required gate downgraded to NOT_REQUIRED"))
    prior_removed = [g["gate_id"] for g in task["gates"] if (g["obligation"].get("origin") or {}).get("type") in {"PRIOR_RISK_TIER","ESTABLISHED_REQUIREMENT"} and not g["obligation"]["required"]]
    out.append(rr("AIH-V0-R041", "FAIL" if prior_removed else "PASS", "established gate obligation removed: " + ", ".join(prior_removed) if prior_removed else "no established gate obligation erased by risk change"))
    deviation_attempt = bool(task.get("deviations"))
    out.append(rr("AIH-V0-R042", "FAIL" if deviation_attempt else "PASS", "V0 has no generic deviation/waiver contract" if deviation_attempt else "no unsupported generic gate-removal deviation present"))

    approvals = task["approvals"]
    if not approvals:
        out += [
            rr("AIH-V0-R050", "PASS", "approval absence represented by empty list", "INFO"),
            rr("AIH-V0-R051", "PASS", "no AI advisory counted as approval", "INFO"),
            rr("AIH-V0-R052", "NOT_APPLICABLE", "no approvals present", "INFO"),
        ]
    for approval in approvals:
        actor = approval["actor"]
        human = actor["actor_type"] == "HUMAN"
        out.append(rr("AIH-V0-R050", "PASS" if human else "FAIL", f"approval {approval['approval_id']} {'is explicit human record' if human else 'is not human'}"))
        out.append(rr("AIH-V0-R051", "PASS" if human else "FAIL", "approval is not AI advisory" if human else "non-human actor cannot count as human approval"))
        allowed_roles = set(config.roles["approval_authority"].get(approval["approval_type"], []))
        role_ok = actor.get("authority_role") in allowed_roles
        out.append(rr("AIH-V0-R052", "PASS" if role_ok else "FAIL", f"approval actor role {'authorized' if role_ok else 'unauthorized'} for {approval['approval_type']}"))
    out.append(rr("AIH-V0-R053", "PASS", "approval cannot override deterministic transition legality", "INFO"))

    approval_requirement = _required_transition_approval(task, config)
    if approval_requirement is None:
        out.append(rr("AIH-V0-R054", "NOT_APPLICABLE", "requested transition has no frozen explicit approval prerequisite", "INFO"))
    else:
        approval_ok = _has_qualifying_approval(task, approval_requirement, config)
        out.append(rr("AIH-V0-R054", "PASS" if approval_ok else "FAIL", f"required {approval_requirement['approval_type']} {approval_requirement['decision']} approval present" if approval_ok else f"transition requires explicit authorized {approval_requirement['approval_type']} {approval_requirement['decision']} approval"))

    qa_required = bool(qa and qa["obligation"]["required"])
    if qa_required:
        impl_actor = _gate_actor_id(task, "IMPLEMENTATION")
        qa_actor = _gate_actor_id(task, "QA")
        same = bool(impl_actor and qa_actor and impl_actor == qa_actor)
        identities = bool(impl_actor and qa_actor)
        out.append(rr("AIH-V0-R060", "FAIL" if same or not identities else "PASS", "implementation actor equals QA actor" if same else ("implementation and QA actors are distinct" if identities else "mandatory independence identity unavailable")))
        out.append(rr("AIH-V0-R061", "PASS" if identities else "FAIL", "required actor identities available" if identities else "independence UNVERIFIED"))
    else:
        out.append(rr("AIH-V0-R060", "NOT_APPLICABLE", "QA independence not mandatory in supplied gate snapshot", "INFO"))
        out.append(rr("AIH-V0-R061", "NOT_APPLICABLE", "QA independence not mandatory in supplied gate snapshot", "INFO"))

    if not task["findings"]:
        for rid in ("AIH-V0-R070","AIH-V0-R071","AIH-V0-R072","AIH-V0-R073","AIH-V0-R074"):
            out.append(rr(rid, "NOT_APPLICABLE", "no project findings present", "INFO"))
    for f in task["findings"]:
        if f["type"] in {"VALIDATION_GAP", "OBSERVATION", "UNRESOLVED"}:
            out.append(rr("AIH-V0-R070", "PASS", f"{f['finding_id']} preserved as {f['type']}", "INFO"))
            continue
        evidence = f.get("evidence") or {}
        refs = evidence.get("evidence_refs") or []
        classification = f.get("classification") or {}
        classifier = classification.get("classified_by") or {}
        out.append(rr("AIH-V0-R071", "PASS" if refs else "FAIL", "confirmed defect has evidence" if refs else "confirmed defect lacks evidence"))
        out.append(rr("AIH-V0-R072", "FAIL" if classifier.get("actor_type") == "AI_ADVISORY" else "PASS", "AI advisory cannot classify confirmed defect" if classifier.get("actor_type") == "AI_ADVISORY" else "classifier is not AI advisory"))
        producer = evidence.get("produced_by") or {}
        tool_only = producer.get("actor_type") == "VERIFIED_TOOL" and not classifier
        out.append(rr("AIH-V0-R073", "FAIL" if tool_only else "PASS", "verified tool evidence cannot alone establish authoritative confirmed defect" if tool_only else "evidence producer not treated as sole classifier"))
        classifier_ok = classification.get("decision") == "CONFIRMED_DEFECT" and classifier.get("actor_type") == "HUMAN" and classifier.get("authority_role") in config.roles["defect_classification_authority"]
        out.append(rr("AIH-V0-R074", "PASS" if classifier_ok else "FAIL", "authorized human defect classification present" if classifier_ok else "authoritative confirmed-defect classification missing/unauthorized"))

    current_complete_conflict = state == "COMPLETE" and bool(required_gate_failures(task))
    out.append(rr("AIH-V0-R080", "FAIL" if current_complete_conflict else "PASS", "COMPLETE contradicts pending/failed mandatory gate(s)" if current_complete_conflict else "current COMPLETE state not contradicted by mandatory gate snapshot"))
    out.append(rr("AIH-V0-R081", "PASS", "all gate states canonical", "INFO"))
    contrad = []
    for g in task["gates"]:
        ex = g["execution"]["state"]
        dec = (g.get("disposition") or {}).get("decision")
        if (ex == "PASS" and dec == "FAIL") or (ex == "FAIL" and dec == "PASS"):
            contrad.append(g["gate_id"])
    out.append(rr("AIH-V0-R082", "FAIL" if contrad else "PASS", "contradictory gate execution/disposition: " + ", ".join(contrad) if contrad else "no contradictory authoritative gate facts detected"))
    out.append(rr("AIH-V0-R090", "PASS", "V0 exposes no repository/project-state mutation operation", "INFO"))
    return out


def classify_status(rule_results: list[dict[str, str]]) -> str:
    failures = {r["rule_id"] for r in rule_results if r["status"] == "FAIL"}
    if failures & {"AIH-V0-R080", "AIH-V0-R082"}:
        return "CONTRADICTORY"
    incomplete = {"AIH-V0-R030","AIH-V0-R031","AIH-V0-R032","AIH-V0-R035","AIH-V0-R036","AIH-V0-R054","AIH-V0-R060","AIH-V0-R061","AIH-V0-R071","AIH-V0-R073","AIH-V0-R074"}
    if failures & incomplete:
        return "INCOMPLETE"
    if failures:
        return "INVALID"
    return "VALID"


def transition_permitted(task: dict[str, Any], rules: list[dict[str, str]]) -> bool:
    return bool(task.get("requested_transition")) and not any(r["status"] == "FAIL" for r in rules)


def final_policy_recheck(task: dict[str, Any], recommendation: dict[str, Any], original_rules: list[dict[str, str]], fresh_rules: list[dict[str, str]]) -> tuple[bool, list[str]]:
    expected_allowed = transition_permitted(task, fresh_rules)
    expected_status = classify_status(fresh_rules)
    problems: list[str] = []
    if fresh_rules != original_rules:
        problems.append("fresh deterministic rule evaluation diverged from initial evaluation")
    if bool(recommendation.get("requested_transition_permitted")) != expected_allowed:
        problems.append("requested-transition permission diverged from fresh deterministic policy")
    if recommendation.get("deterministic_status") != expected_status:
        problems.append("deterministic status diverged from fresh deterministic policy")
    if expected_status != "VALID" and recommendation.get("requested_transition_permitted"):
        problems.append("non-VALID evaluation emitted advancement permission")
    if task.get("requested_transition") in {"COMPLETE", "READY_FOR_RELEASE"} and required_gate_failures(task) and recommendation.get("requested_transition_permitted"):
        problems.append("advancement bypassed mandatory gate")
    if any(r["status"] == "FAIL" for r in fresh_rules) and recommendation.get("requested_transition_permitted"):
        problems.append("approval/recommendation bypassed deterministic prohibition")
    return not problems, problems
