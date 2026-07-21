from dataclasses import dataclass


@dataclass(frozen=True)
class Module:
    slug: str
    title: str
    summary: str
    outputs: tuple[str, ...]
    prompt: str


MODULES = {
    "workflow-audit": Module(
        slug="workflow-audit",
        title="Workflow Audit",
        summary="Map how work actually happens, including exceptions, approvals, and hidden tribal knowledge.",
        outputs=(
            "operating map",
            "exception list",
            "approval points",
            "pain-point summary",
        ),
        prompt=(
            "Act like an AI forward deployed engineer auditing a real business workflow. "
            "Help me map the trigger, actors, tools, steps, exceptions, approvals, and current metrics. "
            "Return a granular workflow map and call out where AI should be used, where deterministic software should be used, and where human review should remain."
        ),
    ),
    "agent-systems": Module(
        slug="agent-systems",
        title="Agent Systems",
        summary="Build one real-loop system with tools, traces, and deliberate human approval points.",
        outputs=(
            "working agent loop",
            "architecture sketch",
            "trace sample",
            "integration map",
        ),
        prompt=(
            "Help me design a deployment-grade agent system for the workflow I audited. "
            "Use a tool-using architecture with explicit boundaries between deterministic software, model judgment, and human approval. "
            "Return components, control flow, trace requirements, and likely failure points."
        ),
    ),
    "evals-reliability": Module(
        slug="evals-reliability",
        title="Evals and Reliability",
        summary="Turn the system into something measurable with a golden dataset and failure taxonomy.",
        outputs=(
            "golden dataset",
            "failure taxonomy",
            "eval rubric",
            "before/after results",
        ),
        prompt=(
            "Help me create an eval plan for this AI workflow system. "
            "Define a golden dataset, pass/fail criteria, major failure modes, and a human-in-the-loop escalation policy. "
            "Optimize for deployment confidence, not benchmark theater."
        ),
    ),
    "deployment-integration": Module(
        slug="deployment-integration",
        title="Deployment and Integration",
        summary="Design the rollout path that fits the current stack and de-risks adoption.",
        outputs=(
            "shadow mode plan",
            "rollback path",
            "monitoring plan",
            "integration boundaries",
        ),
        prompt=(
            "Help me design a rollout plan for this AI workflow system into an existing enterprise stack. "
            "Assume the buyer is risk-sensitive and does not want a rip-and-replace migration. "
            "Return a phased deployment plan from sandbox to shadow mode to controlled autonomy to production."
        ),
    ),
    "business-value": Module(
        slug="business-value",
        title="Business Value and Trust",
        summary="Frame the system in stakeholder-safe language across ROI, risk, and adoption.",
        outputs=(
            "ROI framing",
            "risk framing",
            "stakeholder pitch points",
            "objection handling",
        ),
        prompt=(
            "Act like an FDE preparing a stakeholder brief. "
            "Translate this technical system into a business case using revenue uplift, risk mitigation, and cost savings. "
            "Also include adoption concerns, organizational incentives, and likely objections."
        ),
    ),
    "capstone": Module(
        slug="capstone",
        title="Capstone Packaging",
        summary="Turn the project into explicit FDE proof with case-study quality packaging.",
        outputs=(
            "case study",
            "audit summary",
            "eval summary",
            "deployment plan",
            "stakeholder pitch",
        ),
        prompt=(
            "Help me package this project as proof that I can do forward deployed engineering. "
            "I need a case study that covers the workflow audit, system design, failure modes, eval evidence, deployment plan, and business value. "
            "Write it so a founder, hiring manager, or client can quickly see why this is credible."
        ),
    ),
}


WEEK_PLAN = {
    1: {
        "theme": "Build one real-loop system",
        "focus": (
            "choose one real workflow",
            "map the steps",
            "build a working system",
            "include traces and approval points",
        ),
        "done": "A non-trivial task completes repeatedly and you can show what happened step by step.",
    },
    2: {
        "theme": "Harden for reality",
        "focus": (
            "add structure to inputs and outputs",
            "handle unhappy paths",
            "log failures and recoveries",
            "stop building only for the happy path",
        ),
        "done": "You know how the system fails and how major exceptions get mitigated or routed.",
    },
    3: {
        "theme": "Measure value",
        "focus": (
            "build a golden dataset",
            "run evals",
            "estimate economics",
            "improve cost, accuracy, and reliability",
        ),
        "done": "You can defend the system with evidence and speak about revenue, risk, or cost impact.",
    },
    4: {
        "theme": "Package and pitch",
        "focus": (
            "create a case study",
            "write the rollout plan",
            "rehearse the pitch",
            "get feedback from real people",
        ),
        "done": "You have one project that looks like genuine FDE proof.",
    },
}


SCORECARD = (
    ("Workflow Understanding", "Granular operating map with exceptions, stakeholders, and metrics."),
    ("System Design", "Deployment-grade boundary between tools, models, and humans."),
    ("Reliability / Evals", "Golden dataset, failure taxonomy, measurable improvements."),
    ("Deployment Readiness", "Shadow mode, approvals, monitoring, rollback."),
    ("Business Value", "Revenue uplift, risk mitigation, cost savings framing."),
    ("Stakeholder Trust", "Can explain, defend, and de-risk the system for non-technical stakeholders."),
)
