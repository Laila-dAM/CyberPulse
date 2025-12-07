# Changelog
All notable changes to this project will be documented in this file.

The format is based on **Keep a Changelog** (https://keepachangelog.com/en/1.1.0/),  
and this project adheres to **Semantic Versioning** (https://semver.org/).

---

## [1.0.0] - 2025-12-07
### Added
- Initial complete version of **CyberPulse**.
- Full FastAPI backend with routes for:
  - `/metrics`
  - `/metrics/latest`
  - `/metrics/history`
  - `/alerts`
  - `/predict`
- SQL database integration supporting PostgreSQL, MySQL, SQLite and MongoDB.
- System metric collectors (Bash scripts) for:
  - CPU usage  
  - RAM usage  
  - Disk usage  
  - Network I/O  
  - Temperature  
  - System logs  
- Core anomaly detection and trend prediction module.
- Frontend dashboard using HTML, CSS, JavaScript and Chart.js.
- Neon Y2K / cyber aesthetic UI with real-time charts.
- Internal documentation and project architecture diagrams.
- Basic token-based security and CORS configuration.
- Project directory structure including:
  - `/frontend`  
  - `/backend`  
  - `/scripts`  
  - `/db`  
  - `/docs`  
  - `/art`  
  - `/tests`
- Installation guide and usage documentation.
- MIT License.

### Changed
- Improved global folder organization for readability and maintainability.

### Fixed
- Initial stability adjustments and route consolidation for backend endpoints.

---

## [Unreleased]
### Planned
- Advanced anomaly detection models.
- External log ingestion.
- Role-based access control (RBAC) system.
- Docker and Kubernetes deployment templates.
- Notification system (email, webhook, Slack).
- Responsive dashboard for mobile devices.