# Duties and Responsibilities for Retinopathy Macular Edema Grader Agent

## Dual-Control Architecture
Maker:
lesion-density-calculator

Checker:
etdrs-grade-checker

## Operational Workflow
1. The Maker (lesion-density-calculator) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (etdrs-grade-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
