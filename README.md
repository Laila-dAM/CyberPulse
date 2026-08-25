# CyberPulse

> **Cloud-based infrastructure monitoring platform for computers and servers.**

CyberPulse is an infrastructure monitoring platform designed to collect, analyze, and visualize system metrics from computers and servers.

The project is being progressively evolved from a local monitoring application into a cloud-ready, multi-tenant monitoring platform with a dedicated **CyberPulse Agent**, REST API, PostgreSQL, analytics, anomaly detection, alerting, automated testing, Docker, and CI/CD.

---

## 🚧 Project Status

**Status:** Active Development

CyberPulse is currently undergoing an incremental architectural transformation.

The existing system already contains several working components, including:

* FastAPI backend
* REST API
* System metrics collection
* Authentication
* PostgreSQL/Docker environment
* Alerts
* Analytics
* Machine Learning-based anomaly detection
* Frontend dashboard
* Automated tests
* GitHub Actions workflows

The current development focus is consolidating the existing architecture before introducing the cloud-based agent and multi-tenant infrastructure.

> The roadmap describes planned architecture and future capabilities. Features marked as planned are not necessarily implemented yet.

---

## 🎯 Project Goals

CyberPulse aims to provide a centralized monitoring platform capable of monitoring multiple computers and servers from a single web dashboard.

The long-term goal is to provide an experience similar in concept to modern infrastructure monitoring platforms while keeping the architecture appropriate for an independent project.

The platform is designed to demonstrate practical knowledge of:

* Backend Engineering
* REST API Design
* Database Architecture
* Authentication & Authorization
* Multi-Tenant Systems
* Cloud Architecture
* Docker
* CI/CD
* System Monitoring
* Observability
* Data Analytics
* Machine Learning
* Automated Testing
* Security

---

## 🏗️ Planned Architecture

The target architecture follows a modular monolith approach.

```text
                         CyberPulse Cloud
                                │
                                ▼
                    ┌─────────────────────┐
                    │    Web Dashboard    │
                    └──────────┬──────────┘
                               │
                              HTTPS
                               │
                               ▼
                    ┌─────────────────────┐
                    │     FastAPI API     │
                    │       /api/v1       │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
                ▼              ▼              ▼
           Services      Repositories    Analytics
                │              │
                └───────┬──────┘
                        ▼
                ┌───────────────┐
                │  PostgreSQL   │
                └───────────────┘
                        ▲
                        │
                       HTTPS
                        │
                ┌───────┴────────┐
                │ CyberPulse     │
                │     Agent      │
                └───────┬────────┘
                        │
             ┌──────────┼──────────┐
             ▼          ▼          ▼
            CPU        RAM       Disk
```

The core architectural principle is:

```text
Frontend
   ↓
API
   ↓
Services / Business Logic
   ↓
Repositories / Data Access
   ↓
PostgreSQL
```

The monitoring agent follows:

```text
CyberPulse Agent
   ↓
HTTPS
   ↓
CyberPulse API
   ↓
Services
   ↓
PostgreSQL
```

Neither the frontend nor the Agent will access the database directly.

---

## 🧩 Main Components

### Web Dashboard

The web dashboard provides the interface for monitoring infrastructure.

Planned capabilities include:

* System overview
* Device management
* Metrics visualization
* Alert management
* Analytics
* Anomaly detection
* Predictions
* Organization management
* User management
* Configuration

The current frontend uses HTML, CSS, and JavaScript.

The existing visual identity will be preserved while the interface is progressively connected to real backend data.

---

### FastAPI Backend

The backend is responsible for:

* REST API
* Authentication
* Authorization
* Organization management
* Device management
* Metrics ingestion
* Metrics querying
* Alert management
* Analytics
* Machine Learning
* Health checks
* Security controls

The API will progressively migrate toward versioned endpoints:

```text
/api/v1/
```

---

### PostgreSQL

PostgreSQL is the target database for the application.

The planned data model includes entities such as:

```text
User
Organization
OrganizationMember
Device
DeviceCredential
Metric
Alert
AlertRule
Prediction
Notification
AuditLog
```

Database evolution will use:

* SQLAlchemy
* Alembic
* Versioned migrations

---

### CyberPulse Agent

The CyberPulse Agent is a planned standalone application responsible for collecting system information from monitored machines.

The Agent will collect metrics such as:

* CPU usage
* Memory usage
* Disk usage
* Network activity
* Temperature when available
* Running processes
* Hostname
* Operating system
* Architecture
* Uptime
* Basic system information

The Agent will communicate with the CyberPulse API using HTTPS.

Planned architecture:

```text
CyberPulse Agent
├── Collector
├── Scheduler
├── API Client
├── Authentication
├── Configuration
├── Logging
└── System Information
```

The Agent is planned to support:

* Windows
* Linux

Windows support will initially target a Windows Service deployment.

Linux support will initially target systemd.

---

## 📊 Monitoring

CyberPulse is designed around device-oriented monitoring.

The target relationship is:

```text
Organization
     │
     └── Device
           │
           ├── Metrics
           ├── Alerts
           ├── Predictions
           └── Heartbeats
```

Supported and planned metrics include:

| Metric             | Status                   |
| ------------------ | ------------------------ |
| CPU                | Available                |
| Memory             | Available                |
| Disk               | Available                |
| Network            | Available                |
| Temperature        | Available when supported |
| Processes          | Available / evolving     |
| Uptime             | Planned                  |
| System Information | Available / evolving     |

---

## 🚨 Alerting

CyberPulse includes an alerting system that is being progressively expanded.

Planned alert types include:

* High CPU usage
* High memory usage
* High disk usage
* High temperature
* Device offline
* Anomalous behavior
* Other configurable conditions

Example rule:

```text
CPU > 90% for 5 minutes
```

Future alert rules will support:

```text
Metric
Operator
Threshold
Duration
Severity
Device / Group
Enabled / Disabled
```

Supported severity levels:

```text
INFO
WARNING
CRITICAL
```

---

## 🤖 Analytics & Machine Learning

CyberPulse includes analytics and Machine Learning capabilities for monitoring system behavior.

The goal is to provide useful insights rather than adding Machine Learning purely for complexity.

Planned capabilities include:

* Statistical analysis
* Anomaly detection
* Trend detection
* Usage forecasting
* Performance degradation detection
* Storage growth estimation

Example insight:

```text
Disk usage is increasing consistently and is expected
to reach 90% in approximately 12 days.
```

---

## 🏢 Multi-Tenancy

The planned platform architecture supports multiple organizations.

```text
Organization A
├── Server 01
├── Server 02
└── Development PC

Organization B
├── Server 01
└── Server 02
```

Users will belong to organizations through membership relationships.

Planned roles include:

| Role   | Responsibility                           |
| ------ | ---------------------------------------- |
| Owner  | Full organization control                |
| Admin  | Manage users, devices, and configuration |
| Member | Normal platform usage                    |
| Viewer | Read-only access                         |

Tenant isolation will be enforced by the backend rather than relying on frontend restrictions.

---

## 🔐 Security

Security is a core part of the architecture.

The project is being progressively improved to include:

* Password hashing
* Secure authentication
* JWT-based authentication
* HTTP-only cookies where appropriate
* Role-based access control
* Organization-level authorization
* Device-specific credentials
* Credential revocation
* Environment-based secrets
* Restricted CORS
* Input validation
* Rate limiting
* Security headers
* Audit logging
* Secure error handling
* HTTPS in production

Sensitive configuration should never be committed to the repository.

Use:

```text
.env.example
```

as the configuration template.

---

## 🐳 Development Environment

CyberPulse uses Docker for local infrastructure.

The development environment is designed around:

```text
Docker Compose
       │
       ├── Backend
       │
       └── PostgreSQL
```

The intended development workflow is:

```bash
docker compose up --build
```

Additional services such as Redis or background workers will only be introduced when there is a concrete architectural need.

---

## 🧪 Testing

The project contains automated tests covering different areas of the system.

Current test categories include:

```text
tests/
├── unit/
├── integration/
└── load_test/
```

The testing strategy is being expanded alongside the architecture.

When functionality changes, the goal is to:

1. Update existing tests.
2. Add tests for new behavior.
3. Run the test suite.
4. Fix regressions.
5. Commit the change only after validation.

---

## ⚙️ CI/CD

CyberPulse uses GitHub Actions for automated development workflows.

The CI/CD architecture is being progressively expanded toward:

```text
Pull Request
     ↓
Lint
     ↓
Unit Tests
     ↓
Integration Tests
     ↓
Docker Build
     ↓
Security Checks
     ↓
Deployment
```

The goal is to prevent critical failures from reaching production.

---

## ❤️ Health & Observability

CyberPulse will also monitor the health of its own infrastructure.

Planned capabilities include:

* Structured logging
* Health checks
* Readiness checks
* Liveness checks
* API metrics
* Error monitoring
* Operational logs

Planned endpoints include:

```text
GET /health
GET /ready
```

---

## 📁 Project Structure

The repository is currently being incrementally reorganized.

The target structure is approximately:

```text
CyberPulse/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── repositories/
│   │   └── main.py
│   │
│   ├── migrations/
│   ├── tests/
│   └── Dockerfile
│
├── agent/
│   ├── src/
│   │   ├── collector/
│   │   ├── client/
│   │   ├── config/
│   │   ├── security/
│   │   ├── scheduler/
│   │   └── main.py
│   │
│   ├── tests/
│   └── installers/
│
├── frontend/
│
├── infrastructure/
│   ├── docker/
│   └── cloud/
│
├── docs/
│   ├── architecture/
│   ├── api/
│   └── deployment/
│
├── tests/
│
├── docker-compose.yml
├── .env.example
├── README.md
├── CHANGELOG.md
└── LICENSE
```

This represents the target architecture and does not imply that every directory is currently implemented.

---

## 🗺️ Roadmap

### Phase 1 — Audit & Cleanup

* [x] Establish clean Git branch
* [ ] Audit current architecture
* [ ] Identify duplicated models
* [ ] Identify obsolete files
* [ ] Identify broken imports
* [ ] Identify API inconsistencies
* [ ] Document current architecture
* [ ] Clean repository artifacts

### Phase 2 — Backend Foundation

* [ ] Consolidate SQLAlchemy models
* [ ] Standardize PostgreSQL configuration
* [ ] Introduce Alembic
* [ ] Improve application configuration
* [ ] Introduce API versioning
* [ ] Implement health checks
* [ ] Improve backend structure

### Phase 3 — Authentication & Multi-Tenancy

* [ ] Consolidate authentication strategy
* [ ] Implement organizations
* [ ] Implement organization membership
* [ ] Implement RBAC
* [ ] Enforce tenant isolation
* [ ] Improve authorization

### Phase 4 — Device Management

* [ ] Introduce Device entity
* [ ] Device registration
* [ ] Installation credentials
* [ ] Device status
* [ ] Heartbeat
* [ ] Agent version tracking

### Phase 5 — CyberPulse Agent

* [ ] Create standalone Agent
* [ ] Implement system collectors
* [ ] Implement scheduler
* [ ] Implement API client
* [ ] Implement secure authentication
* [ ] Implement logging
* [ ] Implement Windows support
* [ ] Implement Linux support

### Phase 6 — Real Metrics

* [ ] Connect Agent to API
* [ ] Store device metrics
* [ ] Replace dashboard mock data
* [ ] Implement metric history
* [ ] Implement metric aggregation

### Phase 7 — Alerting

* [ ] Alert rules
* [ ] Threshold evaluation
* [ ] Device offline detection
* [ ] Alert resolution
* [ ] Alert history

### Phase 8 — Analytics & ML

* [ ] Improve anomaly detection
* [ ] Trend analysis
* [ ] Forecasting
* [ ] Storage growth prediction
* [ ] Performance insights

### Phase 9 — Real-Time Monitoring

* [ ] Polling-based updates
* [ ] Evaluate SSE/WebSockets
* [ ] Real-time dashboard updates

### Phase 10 — Cloud & Deployment

* [ ] Production Docker configuration
* [ ] Managed PostgreSQL
* [ ] Cloud deployment
* [ ] HTTPS
* [ ] CI/CD deployment
* [ ] Production monitoring

### Phase 11 — Production Hardening

* [ ] Rate limiting
* [ ] Audit logging
* [ ] Data retention
* [ ] Database backups
* [ ] Security hardening
* [ ] Agent credential rotation
* [ ] Error monitoring

---

## 🛠️ Technology Stack

### Backend

* Python
* FastAPI
* Pydantic
* SQLAlchemy
* Alembic
* PostgreSQL

### Frontend

* HTML
* CSS
* JavaScript

### Agent

* Python
* psutil

### Infrastructure

* Docker
* Docker Compose
* GitHub Actions

### Data & Machine Learning

* Pandas
* NumPy
* Scikit-learn

### Testing

* Pytest

> Technologies may evolve during development when there is a clear architectural or maintainability benefit.

---

## 📌 Engineering Principles

CyberPulse follows these principles:

### Incremental evolution

The project is evolved from the existing implementation rather than rewritten from scratch.

### Simplicity before scale

The architecture starts as a modular monolith.

Microservices and Kubernetes are intentionally avoided until there is a concrete need.

### Security by design

Authentication, authorization, tenant isolation, secrets management, and input validation are treated as architectural concerns.

### API-first communication

The frontend and Agent communicate with the backend through APIs.

### Database isolation

The frontend and Agent never access PostgreSQL directly.

### Test-driven evolution

Existing tests should be preserved and expanded as the architecture changes.

### Production-oriented engineering

The project prioritizes maintainability, observability, security, and deployment practices over simply adding technologies to the stack.

---

## 📖 Documentation

Project documentation is being progressively expanded.

Planned documentation:

```text
docs/
├── architecture/
├── api/
└── deployment/
```

Architecture diagrams and technical decisions will be documented as the platform evolves.

---

## 🤝 Development Workflow

Development follows a feature-oriented Git workflow.

Example:

```text
main
 │
 └── feature/device-management
          │
          ├── implementation
          ├── tests
          └── pull request
```

Commit messages follow a conventional format:

```text
feat: add device management
fix: enforce organization isolation
refactor: consolidate metric models
test: add device service tests
docs: update architecture documentation
ci: improve test workflow
security: restrict CORS configuration
chore: clean repository artifacts
```

---

## 📄 License

This project is licensed under the terms defined in the repository's `LICENSE` file.

---

## 👩‍💻 Author

**Laila de Araújo Mota**

CyberPulse is being developed as a portfolio project focused on practical Software Engineering, Backend Engineering, Cloud, DevOps, Observability, and Machine Learning.

---

> **CyberPulse — Monitor. Analyze. Understand.**

--- 
<p align="center"> ૮ ˙Ⱉ˙ ა ʙᴜɴxɪᴇ.ᴢɪᴘ </p>