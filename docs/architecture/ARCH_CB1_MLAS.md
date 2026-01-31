# CB-1: Multi-Level Affiliate System (MLAS) - Architecture Document

**Version:** 1.0.0  
**Date:** January 30, 2026  
**Status:** 🟢 Complete  
**Canonical Reference:** [CB-1: MLAS Capability](../phases/CB-1_MLAS_CAPABILITY.md)

---

## 1. Executive Summary

The CB-1 Multi-Level Affiliate System (MLAS) is a configurable revenue-flow infrastructure that enables WebWaka to support complex affiliate and commission structures. The system provides attribution tracking, flexible commission calculation, payout routing, comprehensive auditability, and dispute resolution capabilities.

**Key Capabilities:**
- **Attribution Tracking** - Track sales to correct affiliates with multi-touch attribution support
- **Commission Calculation** - Flexible rules engine supporting flat rate, percentage, tiered, and performance-based models
- **Payout Routing** - Intelligent routing to multiple payout methods (bank transfer, PayPal, Stripe, crypto)
- **Auditability** - Immutable audit trail for all MLAS transactions
- **Dispute Resolution** - Webhook-based dispute resolution workflows
- **Multi-Level Revenue Trees** - Support for complex affiliate hierarchies with unlimited depth

**Revenue Models Supported:**
- Platform-First (platform takes cut first)
- Partner-Owned (partner owns revenue, pays platform)
- Client-Owned (client owns revenue, pays platform)
- Zero-Platform-Cut (platform takes no cut)
- Hybrid (combination of models)

---

## 2. System Architecture

### 2.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     API Layer (Express.js)                  │
│  ┌──────────────┬──────────────┬──────────────┬──────────┐  │
│  │ Attribution  │ Commission   │ Payout       │ Dispute  │  │
│  │ Endpoints    │ Endpoints    │ Endpoints    │ Endpoints│  │
│  └──────────────┴──────────────┴──────────────┴──────────┘  │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    Service Layer                            │
│  ┌──────────────┬──────────────┬──────────────┬──────────┐  │
│  │ Attribution  │ Commission   │ Payout       │ Audit &  │  │
│  │ Service      │ Service      │ Service      │ Dispute  │  │
│  └──────────────┴──────────────┴──────────────┴──────────┘  │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    Model Layer                              │
│  ┌──────────────┬──────────────┬──────────────┬──────────┐  │
│  │ Affiliate    │ Commission   │ Payout       │ Dispute  │  │
│  │ Model        │ Model        │ Model        │ Model    │  │
│  └──────────────┴──────────────┴──────────────┴──────────┘  │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    Data Layer                               │
│  ┌──────────────┬──────────────┬──────────────┬──────────┐  │
│  │ PostgreSQL   │ Redis Cache  │ Audit Log    │ Event    │  │
│  │ (Primary)    │ (Sessions)   │ (Immutable)  │ Stream   │  │
│  └──────────────┴──────────────┴──────────────┴──────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Core Components

**Attribution Service**
- Tracks sales to affiliates
- Maintains affiliate chains for multi-level structures
- Supports multiple attribution models (direct, referral, multi-touch)
- Calculates attribution weights for revenue distribution

**Commission Calculation Service**
- Evaluates commission rules based on conditions
- Supports multiple commission models (flat, percentage, tiered, performance-based)
- Calculates commissions for each affiliate in chain
- Applies caps, minimums, and bonus rates
- Handles tier-based commission reduction

**Payout Service**
- Schedules payout batches
- Processes payouts to multiple methods
- Tracks payout status and failures
- Implements retry logic for failed payouts
- Generates payout statistics and reports

**Audit & Dispute Service**
- Maintains immutable audit trail
- Logs all MLAS transactions
- Provides dispute creation and resolution
- Supports webhook-based dispute workflows
- Tracks dispute history and resolutions

---

## 3. Data Models

### 3.1 Affiliate Model

```typescript
interface Affiliate {
  id: string;
  tenantId: string;
  organizationId: string;
  name: string;
  email: string;
  tier: number;                    // 1 = direct, 2+ = sub-affiliates
  parentAffiliateId?: string;
  status: AffiliateStatus;         // ACTIVE, INACTIVE, SUSPENDED, TERMINATED
  commissionRate: Decimal;
  payoutMethod: PayoutMethod;
  payoutDetails: PayoutDetails;
  createdAt: Date;
  updatedAt: Date;
}
```

**Key Features:**
- Hierarchical structure with parent-child relationships
- Configurable commission rates per affiliate
- Multiple payout methods supported
- Status tracking for lifecycle management

### 3.2 Attribution Model

```typescript
interface Attribution {
  id: string;
  tenantId: string;
  saleId: string;
  affiliateId: string;
  affiliateChain: string[];        // Array of affiliate IDs from direct to root
  attributionType: AttributionType; // DIRECT, REFERRAL, MULTI_TOUCH, etc.
  attributionWeight: Decimal;      // For multi-touch attribution
  createdAt: Date;
}
```

**Key Features:**
- Tracks complete affiliate chain for multi-level commissions
- Supports multiple attribution models
- Weighted attribution for multi-touch scenarios
- Immutable record of attribution

### 3.3 Commission Model

```typescript
interface CommissionCalculation {
  id: string;
  tenantId: string;
  saleId: string;
  affiliateId: string;
  affiliateChain: string[];
  commissionRuleId: string;
  grossAmount: Decimal;
  commissionAmount: Decimal;
  commissionRate: Decimal;
  netAmount: Decimal;
  status: CommissionStatus;        // PENDING, CALCULATED, APPROVED, DISPUTED, PAID
  calculatedAt: Date;
  paidAt?: Date;
}
```

**Key Features:**
- Tracks full commission lifecycle
- Maintains gross, commission, and net amounts
- Links to commission rule for auditability
- Status tracking from calculation to payment

### 3.4 Payout Model

```typescript
interface Payout {
  id: string;
  tenantId: string;
  batchId: string;
  affiliateId: string;
  amount: Decimal;
  payoutMethod: PayoutMethod;
  status: PayoutStatus;            // SCHEDULED, PROCESSING, COMPLETED, FAILED
  transactionId?: string;
  failureReason?: string;
  processedAt?: Date;
  createdAt: Date;
}
```

**Key Features:**
- Batch-based payout processing
- Multiple payout method support
- Transaction tracking and failure handling
- Retry capability for failed payouts

### 3.5 Dispute Model

```typescript
interface Dispute {
  id: string;
  tenantId: string;
  commissionId: string;
  affiliateId: string;
  reason: DisputeReason;
  description: string;
  status: DisputeStatus;           // OPEN, UNDER_REVIEW, RESOLVED, APPEALED
  evidence?: string[];
  resolution?: DisputeResolution;
  createdAt: Date;
  updatedAt: Date;
  resolvedAt?: Date;
}
```

**Key Features:**
- Full dispute lifecycle tracking
- Evidence attachment support
- Resolution tracking with adjustment amounts
- Audit trail of all dispute actions

---

## 4. Commission Calculation Engine

### 4.1 Commission Rule Structure

```typescript
interface CommissionRule {
  id: string;
  name: string;
  ruleType: CommissionRuleType;    // FLAT_RATE, PERCENTAGE, TIERED, PERFORMANCE_BASED
  conditions: CommissionCondition[];
  commissionStructure: CommissionStructure;
  priority: number;
  isActive: boolean;
}
```

### 4.2 Commission Calculation Flow

```
1. Sale Event Received
   ↓
2. Retrieve Affiliate Chain
   ↓
3. Evaluate Commission Rules (by priority)
   ↓
4. For Each Affiliate in Chain:
   a. Check Rule Conditions
   b. Calculate Base Commission
   c. Apply Tier Reduction (if sub-affiliate)
   d. Apply Bonus Rates (if applicable)
   e. Apply Cap/Minimum
   ↓
5. Create Commission Records
   ↓
6. Log to Audit Trail
   ↓
7. Return Commission Calculations
```

### 4.3 Commission Models Supported

**Flat Rate**
- Fixed commission amount per sale
- Example: $10 per sale

**Percentage**
- Percentage of sale amount
- Example: 10% of sale amount

**Tiered**
- Different rates based on sale amount thresholds
- Example: 5% for sales < $100, 10% for $100-$500, 15% for > $500

**Performance-Based**
- Commission varies based on affiliate performance metrics
- Example: Higher commission for high-volume affiliates

**Hybrid**
- Combination of multiple models
- Example: Base 5% + 2% bonus for top performers

---

## 5. Payout Processing

### 5.1 Payout Methods

| Method | Details | Use Case |
|--------|---------|----------|
| **Bank Transfer** | Direct to bank account | Traditional affiliates |
| **PayPal** | PayPal account transfer | International affiliates |
| **Stripe** | Stripe Connect payout | Merchant affiliates |
| **Crypto** | Blockchain transfer | Tech-savvy affiliates |
| **Internal Credit** | Platform account credit | Platform affiliates |

### 5.2 Payout Workflow

```
1. Commission Approval
   ↓
2. Batch Scheduling
   - Collect approved commissions
   - Group by payout method
   - Set scheduled date
   ↓
3. Batch Processing
   - Validate batch integrity
   - Process each payout
   - Handle failures
   ↓
4. Payout Execution
   - Call payout provider API
   - Get transaction ID
   - Update status
   ↓
5. Failure Handling
   - Log failure reason
   - Queue for retry
   - Notify affiliate
   ↓
6. Completion
   - Mark batch as completed
   - Generate reports
   - Archive records
```

### 5.3 Failure Handling

**Retry Strategy:**
- Automatic retry for transient failures
- Exponential backoff (1s, 2s, 4s, 8s, 16s)
- Manual retry option for persistent failures
- Failure notification to operations team

---

## 6. Audit & Compliance

### 6.1 Audit Trail

All MLAS transactions are logged immutably:

```typescript
interface MLASTransaction {
  id: string;
  tenantId: string;
  transactionType: TransactionType;
  actor: Actor;
  resource: TransactionResource;
  changes: Record<string, unknown>;
  status: TransactionStatus;
  ipAddress: string;
  userAgent: string;
  createdAt: Date;
}
```

**Transaction Types Logged:**
- ATTRIBUTION_CREATED
- COMMISSION_CALCULATED
- COMMISSION_APPROVED
- COMMISSION_DISPUTED
- PAYOUT_SCHEDULED
- PAYOUT_PROCESSED
- DISPUTE_CREATED
- DISPUTE_RESOLVED
- AFFILIATE_CREATED
- AFFILIATE_UPDATED
- RULE_CREATED
- RULE_UPDATED

### 6.2 Dispute Resolution

**Dispute Workflow:**

```
1. Affiliate Initiates Dispute
   - Provides reason and description
   - Attaches evidence
   ↓
2. Dispute Created
   - Status: OPEN
   - Logged to audit trail
   ↓
3. Review Process
   - Operations team reviews
   - Status: UNDER_REVIEW
   ↓
4. Resolution
   - Approve, reject, or partial approval
   - Adjust commission if needed
   - Status: RESOLVED
   ↓
5. Appeal (Optional)
   - Affiliate can appeal
   - Status: APPEALED
   ↓
6. Final Resolution
   - Status: CLOSED
```

**Webhook Support:**
- Dispute created webhook
- Dispute resolved webhook
- Dispute appealed webhook
- Custom webhook endpoints supported

---

## 7. Multi-Level Revenue Trees

### 7.1 Revenue Tree Structure

```
Organization
  ├── Affiliate 1 (Tier 1, 10% commission)
  │   ├── Affiliate 1.1 (Tier 2, 8% commission)
  │   │   └── Affiliate 1.1.1 (Tier 3, 6% commission)
  │   └── Affiliate 1.2 (Tier 2, 8% commission)
  └── Affiliate 2 (Tier 1, 10% commission)
      └── Affiliate 2.1 (Tier 2, 8% commission)
```

### 7.2 Commission Distribution

When a sale is attributed to Affiliate 1.1.1:
1. Affiliate 1.1.1 receives 6% commission
2. Affiliate 1.1 receives 2% (tier-based reduction)
3. Affiliate 1 receives 1% (tier-based reduction)

**Tier Reduction Formula:**
```
Commission for Tier N = Base Rate × (1 - 0.1 × (N - 1))

Example:
- Tier 1: 10% × (1 - 0) = 10%
- Tier 2: 10% × (1 - 0.1) = 9%
- Tier 3: 10% × (1 - 0.2) = 8%
```

---

## 8. Revenue Models

### 8.1 Platform-First Model

Platform takes its cut first, remainder distributed to partners/affiliates.

```
Sale Amount: $100
Platform Cut: 30% = $30
Remaining: $70
  ├── Partner Cut: 50% = $35
  └── Affiliate Commission: 50% = $35
```

### 8.2 Partner-Owned Model

Partner owns revenue, pays platform a fee.

```
Sale Amount: $100
Partner Revenue: $100
  ├── Platform Fee: 10% = $10
  └── Partner Net: $90
```

### 8.3 Client-Owned Model

Client owns revenue, pays platform a fee.

```
Sale Amount: $100
Client Revenue: $100
  ├── Platform Fee: 5% = $5
  └── Client Net: $95
```

### 8.4 Zero-Platform-Cut Model

Platform takes no cut.

```
Sale Amount: $100
Platform Cut: 0% = $0
Partner/Affiliate Revenue: $100
```

### 8.5 Hybrid Model

Combination of models based on conditions.

```
If Sale Amount < $50:
  - Platform-First (30% cut)
```

---

## 9. Related Documents

- [Runbook](../runbooks/RUNBOOK_CB1_MLAS.md)
- [API Reference](../api/API_CB1_MLAS.md)
