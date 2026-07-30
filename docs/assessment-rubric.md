# FDE Assessment Rubric

Score each area from 1 to 5.

## 1. Workflow Understanding
- 1: vague description of the workflow
- 3: understands main steps and some exceptions
- 5: has a granular operating map with stakeholder-specific nuance and edge cases

## 2. System Design
- 1: prompt demo only
- 3: basic working automation or agent loop
- 5: robust system with tools, guardrails, traces, and integration boundaries

## 3. Reliability / Evals
- 1: no evals, no known failure modes
- 3: basic tests and a few known edge cases
- 5: golden dataset, failure taxonomy, measurable eval improvements, regression discipline

## 4. Deployment Readiness
- 1: no rollout plan
- 3: can describe how it might be adopted
- 5: clear shadow-mode, approval, rollback, and monitoring strategy

## 5. Business Value
- 1: only technical excitement
- 3: some plausible value claims
- 5: clear framing in revenue uplift, risk mitigation, and cost savings

## 6. Stakeholder Trust
- 1: cannot explain to non-technical operators
- 3: understandable but not convincing
- 5: can explain, defend, and de-risk the system for executives and operators

## 7. FDE Fit and Platform Leverage
- 1: the problem would be better served by self-serve software, simple configuration, or one-off contract engineering
- 3: some justification for an FDE motion exists, but the platform and reuse story are still weak
- 5: clearly demonstrates a technical platform for an outcome-oriented buyer, with reusable primitives and an explicit bespoke-vs-shared boundary

## Graduation bar
A capstone starts looking like real FDE proof when:
- no category is below 3
- Workflow Understanding, Reliability / Evals, Business Value, and FDE Fit and Platform Leverage average at least 4
