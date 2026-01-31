# CS-2: Notification Service - Architecture Document

**Version:** 1.0.0  
**Date:** January 30, 2026  
**Status:** 🟢 Complete  
**Canonical Reference:** [CS-2: Notification Service](../phases/CS-2_NOTIFICATION_SERVICE.md)

---

## 1. Executive Summary

The CS-2 Notification Service provides a centralized, multi-channel notification system for the WebWaka platform. It supports email, SMS, push notifications, and in-app messages, with template management, provider abstraction, and user preference management.

**Key Capabilities:**
- **Multi-Channel Delivery** - Email, SMS, Push, In-App
- **Template Management** - Dynamic templates with Handlebars
- **Provider Abstraction** - Pluggable providers for each channel
- **User Preferences** - User-level control over notification settings
- **Auditability** - Full audit trail of all notifications sent

---

## 2. System Architecture

### 2.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     API Layer (Express.js)                  │
│  ┌───────────────────────────────────────────────────────┐  │
│  │                  Notification Endpoints               │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    Service Layer                            │
│  ┌──────────────────┬──────────────────┬─────────────────┐  │
│  │ Notification     │ Template         │ Preference      │  │
│  │ Service          │ Service          │ Service         │  │
│  └──────────────────┴──────────────────┴─────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    Provider Layer                           │
│  ┌───────────┬───────────┬──────────────┬────────────────┐  │
│  │ Email     │ SMS       │ Push         │ In-App         │  │
│  │ Providers │ Providers │ Providers    │ Provider       │  │
│  └───────────┴───────────┴──────────────┴────────────────┘  │
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

**Notification Service**
- Orchestrates notification delivery
- Handles template rendering and provider selection
- Manages retry logic and failure handling

**Template Service**
- Manages notification templates
- Supports dynamic data with Handlebars
- Provides versioning and localization

**Preference Service**
- Manages user notification preferences
- Supports channel-level and notification-type-level settings
- Enforces user preferences before sending

**Provider Layer**
- Pluggable providers for each channel
- Abstracts provider-specific APIs
- Supports multiple providers per channel for failover

---

## 3. Data Models

### 3.1 Notification Model

```typescript
interface Notification {
  id: string;
  tenantId: string;
  userId: string;
  channel: NotificationChannel; // EMAIL, SMS, PUSH, IN_APP
  templateId: string;
  data: Record<string, unknown>;
  status: NotificationStatus; // PENDING, SENT, FAILED, DELIVERED, READ
  sentAt?: Date;
  deliveredAt?: Date;
  readAt?: Date;
  createdAt: Date;
}
```

### 3.2 Template Model

```typescript
interface Template {
  id: string;
  name: string;
  channel: NotificationChannel;
  subjectTemplate: string; // For email
  bodyTemplate: string;
  version: number;
  isDefault: boolean;
  createdAt: Date;
  updatedAt: Date;
}
```

### 3.3 Preference Model

```typescript
interface Preference {
  userId: string;
  channel: NotificationChannel;
  notificationType: string;
  isEnabled: boolean;
  updatedAt: Date;
}
```

---

## 4. Notification Workflow

```
1. Notification Request Received
   ↓
2. Check User Preferences
   ↓
3. Retrieve Template
   ↓
4. Render Template with Data
   ↓
5. Select Provider
   ↓
6. Send Notification
   ↓
7. Update Status
   ↓
8. Log to Audit Trail
```

---

## 5. Provider Abstraction

### 5.1 Provider Interface

```typescript
interface NotificationProvider {
  send(notification: Notification): Promise<void>;
}
```

### 5.2 Supported Providers

| Channel | Providers |
|---------|-----------|
| **Email** | SendGrid, Mailgun, AWS SES |
| **SMS** | Twilio, Vonage, AWS SNS |
| **Push** | Firebase Cloud Messaging (FCM), Apple Push Notification Service (APNS) |
| **In-App** | Internal WebSocket-based provider |

---

## 6. Link to Phase Document

- **Phase Document:** [CS-2: Notification Service](../phases/CS-2_NOTIFICATION_SERVICE.md)
- **Master Control Board:** [§7.3 CS-2](../governance/WEBWAKA_MASTER_CONTROL_BOARD.md#cs-2-notification-service)

---

**End of Document**
