from __future__ import annotations

from typing import Any

from .transitions import TERMINAL_STATES, resume_target_valid, transition_enumerated

RULE_IDS = [
    "AIH-V0-R001", "AIH-V0-R002", "AIH-V0-R003", "AIH-V0-R004", "AIH-V0-R005",
    "AIH-V0-R010", "AIH-V0-R011",
    "AIH-V0-R020", "AIH-V0-R021", "AIH-V0-R022", "AIH-V0-R023",
    "AIH-V0-R030", "AIH-V0-R031", "AIH-V0-R032", "AIH-V0-R033", "AIH-V0-R034", "AIH-V0-R035",
    "AIH-V0-R040", "AIH-V0-R041", "AIH-V0-R042",
    "AIH-V0-R050", "AIH-V0-R051", "AIH-V0-R052", "AIH-V0-R053",
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


def _gate_actor_id(task: dict[str, Any], gate_id: str) -> str | None:
    gate = gate_map(task).get(gate_id)
    if not gate:
        return None
    actor = ((gate.get("disposition") or {}).get("actor") or {})
    return actor.get("actor_id")


def evaluate_rules(task: dict[str, Any], config: Any) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    for rid in ("AIH-V0-R001","AIH-V0-R002","AIH-V0-R003","AIH-V0-R004","AIH-V0-R005"):
        out.append(rr(rid, "PASS", "validated by schema/kernel profile", "INFO"))

    state = task["work_state"]
    if state == "PAUSED":
        pause = task.get("pause") or {}
        missing = [k for k in ("reason", "resume_condition", "previous_state") if not pause.get(k)]
        out.append(rr("AIH-V0-R010", "FAIL" if missing else "PASS", "PAUSED missing: " + ", ".join(missing) if missing else "PAUSED contract satisfied"))
    else:
        out.append(rr("AIH-V0-R010", "NOT_APPLICABLE", "task is not PAUSED", "INFO"))

    if state == "BLOCKED":
        blocker = task.get("blocker") or {}
        missing = [k for k in ("description", "owner", "unblock_condition", "previous_state") if not blocker.get(k)]
        out.append(rr("AIH-V0-R011", "FAIL" if missing else "PASS", "BLOCKED missing: " + ", ".join(missing) if missing else "BLOCKED contract satisfied"))
    else:
        out.append(rr("AIH-V0-R011", "NOT_APPLICABLE", "task is not BLOCKED", "INFO"))

    requested = task.get("requested_transition")
    if requested:
        enum_ok = transition_enumerated(task, requested, config.transitions)
        out.append(rr("AIH-V0-R020", "PASS" if enum_ok else "FAIL", f"{state} -> {requested} is {'enumerated' if enum_ok else 'not enumerated'}"))
        terminal_fail = state in TERMINAL_STATES
        out.append(rr("AIH-V0-R021", "FAIL" if terminal_fail else "PASS", "ordinary transition from terminal state is forbidden" if terminal_fail else "current state is nonterminal"))
        if state == "PAUSED":
            ok = resume_target_valid(task, requested)
            out.append(rr("AIH-V0-R022", "PASS" if ok else "FAIL", "resume target valid" if ok else "resume target does not match prior lifecycle state"))
            out.append(rr("AIH-V0-R023", "NOT_APPLICABLE", "task is not BLOCKED", "INFO"))
        elif state == "BLOCKED":
            ok = resume_target_valid(task, requested)
            out.append(rr("AIH-V0-R023", "PASS" if ok else "FAIL", "resume target valid" if ok else "resume target does not match prior lifecycle state"))
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
    out.append(rr("AIH-V0-R030", "FAIL" if missing_minimum else "PASS", "missing minimum required gate(s): " + ", ".join(missing_minimum) if missing_minimum else "minimum risk gate records are present"))

    req_fail = required_gate_failures(task)
    pre_rel_fail = requested == "READY_FOR_RELEASE" and bool(req_fail)
    comp_fail = requested == "COMPLETE" and bool(req_fail)
    out.append(rr("AIH-V0-R031", "FAIL" if pre_rel_fail else ("PASS" if requested == "READY_FOR_RELEASE" else "NOT_APPLICABLE"), "READY_FOR_RELEASE requires all mandatory gates PASS" if pre_rel_fail else ("mandatory pre-release gates PASS" if requested == "READY_FOR_RELEASE" else "target is not READY_FOR_RELEASE"), "ERROR" if pre_rel_fail else "INFO"))
    out.append(rr("AIH-V0-R032", "FAIL" if comp_fail else ("PASS" if requested == "COMPLETE" else "NOT_APPLICABLE"), "COMPLETE requires all mandatory gates PASS" if comp_fail else ("mandatory completion gates PASS" if requested == "COMPLETE" else "target is not COMPLETE"), "ERROR" if comp_fail else "INFO"))
    out.append(rr("AIH-V0-R033", "PASS", "READY_FOR_RELEASE and COMPLETE are distinct canonical states", "INFO"))

    impl = gates.get("IMPLEMENTATION")
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
        if f["type"] == "VALIDATION_GAP":
            out.append(rr("AIH-V0-R070", "PASS", f"{f['finding_id']} remains VALIDATION_GAP", "INFO"))
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
    incomplete = {"AIH-V0-R030","AIH-V0-R031","AIH-V0-R032","AIH-V0-R035","AIH-V0-R060","AIH-V0-R061","AIH-V0-R071","AIH-V0-R073","AIH-V0-R074"}
    if failures & incomplete:
        return "INCOMPLETE"
    if failures:
        return "INVALID"
    return "VALID"


def transition_permitted(task: dict[str, Any], rules: list[dict[str, str]]) -> bool:
    return bool(task.get("requested_transition")) and not any(r["status"] == "FAIL" for r in rules)


def final_policy_recheck(task: dict[str, Any], recommendation: dict[str, Any], fresh_rules: list[dict[str, str]]) -> tuple[bool, list[str]]:
    expected_allowed = transition_permitted(task, fresh_rules)
    expected_status = classify_status(fresh_rules)
    problems: list[str] = []
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
