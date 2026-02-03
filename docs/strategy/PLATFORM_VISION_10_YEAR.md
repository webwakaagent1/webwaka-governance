
# WebWaka 10-Year Platform Vision: Forensic Context Recovery v2

**Status:** DRAFT - Awaiting Founder Review  
**Author:** Chief of Staff (webwakaagent2)  
**Date:** February 3, 2026

**This document supersedes all previous Vision Recovery artifacts.**

---

## 1. Recovered Original Vision (Corrected & Complete)

Forensic analysis of archived repositories and strategic documents confirms that WebWaka was designed as a **Platform for Building Platforms** from its inception. The architecture was intentionally designed to support a future far beyond its initial implementation, with a clear trajectory toward a multi-vertical, extensible ecosystem.

This document restores the original, complete vision, correcting previous omissions and providing a single, canonical source of truth for long-term planning, governance, and execution.

### 1.1 The Platform-for-Platforms Identity

WebWaka is not a single application; it is a **recursive, multi-tenant platform** for building and operating transactional ecosystems. Its core identity is defined by:

- **Suite-Based Architecture:** The platform is composed of independent, subscribable "Suite Families" (e.g., Commerce, Transportation) that can be adopted and composed by partners.
- **Shared Primitives:** All suites are built upon a common foundation of shared primitives (e.g., identity, payments, inventory, offline sync).
- **Partner-Centric Model:** The platform is designed to be extended and resold by partners, who can build their own businesses on top of WebWaka.
- **Recursive Composition:** The platform can be used to build platforms, which can in turn be used to build more platforms, creating a fractal-like ecosystem.

### 1.2 The Anchor Domains: Commerce and Transportation

The original roadmap positioned **Commerce** and **Transportation** as the first two anchor domains, serving as reference implementations for the platform-for-platforms model. They were not intended as vertical bolt-ons, but as structural mirrors of each other, demonstrating the power and flexibility of the underlying primitives.

## 2. Commerce Suite Family (Canonical Definition)

The Commerce Suite Family was designed as the first production domain, providing a comprehensive set of tools for building and managing transactional businesses.

### 2.1 The Commerce Triad

1.  **Point of Sale (POS) Suite:** An offline-first, device-based and agent-based selling solution with an inventory-first architecture, designed for intermittent connectivity environments.
2.  **Single Vendor Marketplace (SVM) Suite:** A merchant-controlled storefront for a single merchant to sell many products, with full control over pricing, promotions, and inventory.
3.  **Multi-Vendor Marketplace (MVM) Suite:** A platform for multiple vendors to sell in a single marketplace, with vendor-isolated inventory and shared discovery, governed by platform commissions.

### 2.2 Core Invariants

-   Vendors may subscribe to any one, any two, or all three suites independently.
-   Inventory must synchronize across all subscribed suites (POS ↔ SVM ↔ MVM).
-   This synchronization is foundational, not optional.

## 3. Transportation Suite Family (Canonical Definition)

The Transportation Suite Family was architected as a structural mirror of the Commerce Suite, demonstrating the reusability of the underlying transactional primitives.

### 3.1 The Transportation Triad

1.  **Transport Company Platform:** Operates like a Single Vendor Marketplace, where routes are products and seats are inventory, with full management of pricing, schedules, and capacity.
2.  **Motor Park Platform:** Operates like a Multi-Vendor Marketplace, aggregating multiple transport companies with terminal-level governance and commissions.
3.  **Staff & Independent Agent Sales:** An offline-first ticketing solution for transport company staff, motor park staff, and independent agents, with real-time inventory synchronization.

### 3.2 Core Invariants

-   Seat inventory must sync across all actors: transport companies, motor parks, staff devices, and independent agent devices.
-   This is intentionally symmetric with the Commerce inventory logic.

## 4. Shared Transactional Primitives

Both the Commerce and Transportation Suite Families are built upon a common foundation of shared transactional primitives:

-   **Inventory Management:** A generic primitive for tracking and synchronizing stock (products, seats, etc.) across multiple channels and devices.
-   **Pricing & Promotions:** A flexible engine for defining and applying pricing rules, discounts, and promotional offers.
-   **Agents & Staff:** A role-based access control (RBAC) system for managing the permissions and activities of employees and independent agents.
-   **Offline-First Guarantees:** A robust offline-first architecture with transaction queuing and synchronization to ensure business continuity in low-connectivity environments.

## 5. Implications for Architecture

The restored vision has significant implications for the platform's architecture:

-   **Event Models:** A rich, versioned event model is required to support the complex synchronization and communication needs of the suite-based architecture.
-   **Data Models:** The data models must be designed to be generic and extensible, supporting the diverse needs of different transactional ecosystems.
-   **Synchronization Contracts:** Clear, enforceable contracts are needed to guarantee the consistency and integrity of data (especially inventory) across all suites and devices.

## 6. Implications for Governance

The omission of the Commerce and Transportation Suite Families from the current governance framework has created a significant gap. The following Founder Decisions are incomplete without this context:

-   **FD-2026-015 (Real-Time Systems):** The real-time requirements of inventory synchronization are not fully captured.
-   **FD-2026-017 (Marketplace Primitives):** The specific needs of the SVM and MVM models are not addressed.
-   **FD-2026-019 (Module SDK):** The requirements for building and composing suites are not defined.

## 7. Implications for Team & Agent Structure

The restored vision requires a re-evaluation of the team structure and agent specialization roadmap. The following roles must exist earlier than currently planned:

-   **Commerce Engineer:** A dedicated engineer to own the Commerce Suite Family.
-   **Transportation Engineer:** A dedicated engineer to own the Transportation Suite Family.
-   **Inventory & Sync Specialist:** A specialist to own the critical inventory synchronization primitive.

## 8. 10-Year Platform Trajectory

The Commerce and Transportation Suite Families serve as the anchor for future vertical expansion. The platform is designed to support a wide range of transactional ecosystems, including:

-   **Education:** School management, online learning, and student information systems.
-   **Healthcare:** Clinic management, electronic health records, and telemedicine platforms.
-   **Hospitality:** Hotel and restaurant management, booking engines, and event platforms.
-   **Logistics:** Fleet management, delivery tracking, and warehouse management systems.

## 9. Governance Recommendations

Based on the restored vision, the following governance actions are required:

### 9.1 New Founder Decisions

I recommend creating a single, comprehensive Founder Decision to define the **Transactional Ecosystem Primitives** that underpin both the Commerce and Transportation Suite Families. This FD would cover:

-   Inventory Management
-   Pricing & Promotions
-   Agents & Staff
-   Offline-First Guarantees

This is preferable to creating separate FDs for Commerce and Transportation, as it emphasizes the shared, reusable nature of the underlying primitives.

### 9.2 Amendments to Existing Founder Decisions

The following existing FDs must be amended to incorporate the restored vision:

-   **FD-2026-015 (Real-Time Systems):** Add specific requirements for real-time inventory synchronization.
-   **FD-2026-017 (Marketplace Primitives):** Add specific requirements for the SVM and MVM models.
-   **FD-2026-019 (Module SDK):** Add specific requirements for building and composing suites.

### 9.3 Changes to Execution Waves

-   **Wave 2:** Should be refocused on implementing the **Transactional Ecosystem Primitives** as the highest priority.
-   **Wave 3:** Should be dedicated to building the **Commerce and Transportation Suite Families** on top of the new primitives.

### 9.4 Changes to Agent Specialization Roadmap

The team evolution roadmap must be updated to include the following roles earlier than planned:

-   **Commerce Engineer**
-   **Transportation Engineer**
-   **Inventory & Sync Specialist**

### 9.5 Changes to Architectural Guardrails

The CI guardrail specifications must be updated to include checks for:

-   **Inventory Synchronization:** A new check to ensure that all inventory-mutating operations emit the required synchronization events.
-   **Suite Composition:** A new check to prevent direct dependencies between suites.
