# Multi-Agent Coordination Specification

## Assigned Roles
Maker:
lesion-density-calculator

Checker:
etdrs-grade-checker

## Coordination Protocol
- **Primary Agent**: retinopathy-macular-edema-grader
- **Governance Standard**: OpenGAP Dual-Agent Control Framework v0.1.0
- **Consensus Threshold**: 100% agreement between Maker and Checker before state mutations.
- **Fail-safe Mode**: If verification fails, transaction rolls back and alerts human supervisor.
