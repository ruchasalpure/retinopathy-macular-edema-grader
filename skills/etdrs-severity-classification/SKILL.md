---
name: etdrs-severity-classification
description: Specialized capability for Retinopathy Macular Edema Grader.
license: MIT
allowed-tools: ""
metadata:
  author: "Rucha Salpure"
  version: "1.0.0"
  category: healthcare
---

# Retinopathy Macular Edema Grader — ETDRS SEVERITY CLASSIFICATION Skill

## Purpose
The `etdrs-severity-classification` capability provides high-assurance execution routines for `Retinopathy Macular Edema Grader`.

## Execution Workflow
1. Validate input parameters against typed schemas and invariant constraints.
2. Ingest contextual metrics and establish a deterministic baseline.
3. Formulate candidate recommendations with explicit confidence intervals.
4. Submit draft plans to the independent checker agent for verification.

## Boundary Conditions
- **Input validation:** Reject non-conforming or malformed payloads before evaluation.
- **Fail-safe:** Escalate immediately if telemetry indicators exhibit critical anomalies.
