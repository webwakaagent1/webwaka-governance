# WebWaka Governance Repository

**Supreme Source of Truth for WebWaka Platform**

This repository serves as the control plane for all WebWaka platform development. It contains the Master Control Board, platform invariants, PaA Model, planning documents, architecture documents, and all governance mechanisms.

## Repository Topology

WebWaka uses a multi-repository architecture (INV-012v2):

- **webwaka-governance** (this repo) - Control plane and supreme source of truth
- **webwaka-platform-foundation** - Foundation layer (PF phases)
- **webwaka-core-services** - Core services layer (CS phases)
- **webwaka-capabilities** - Business capabilities layer (CB phases)
- **webwaka-infrastructure** - Infrastructure & deployment (ID phases)
- **webwaka-suites** - Business suites layer (SC phases)

## Key Documents

- **Master Control Board:** `docs/governance/WEBWAKA_MASTER_CONTROL_BOARD.md`
- **Platform Invariants:** See Master Control Board Section 1
- **PaA Model:** `docs/governance/PROMPTS_AS_ARTIFACTS_MODEL.md`
- **Architecture Documents:** `docs/architecture/`
- **Planning Documents:** `docs/planning/`

## Governance Supremacy

All execution must be authorized by an execution prompt in this repository. All implementation repositories are subordinate to this governance repository. The Master Control Board is the single source of truth for platform state.
