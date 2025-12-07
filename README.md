<h1 align="center">C Y B E R P U L S E</h1>

# CyberPulse

CyberPulse is a full-stack monitoring and analytics system designed to collect system metrics, store them, analyze them, and present them through a futuristic cyber-style dashboard. It features a FastAPI backend, system metric collectors, a SQL-based database, and a fully customizable frontend interface.

------------------------------------------------------------
## Key Features


- System metric collection through Bash scripts (CPU, RAM, disk, network, temperature, logs).
- FastAPI backend with endpoints for metrics, alerts, predictions, and historical data.
- SQL-based database (PostgreSQL, MySQL, SQLite or MongoDB depending on configuration).
- Lightweight anomaly detection and trend prediction.
- Frontend dashboard in a neon Y2K / cyber aesthetic with real-time charts.
- Cloud deployment ready for AWS, Azure, GCP, Render, Railway, and others.
- Token-based security, CORS configuration, and environment-based settings.
- Internal documentation and automated tests.

------------------------------------------------------------
## Tech Stack

**Frontend:** HTML, CSS, JavaScript, Chart.js  
**Backend:** Python, FastAPI  
**Database:** PostgreSQL / MySQL / SQLite / MongoDB  
**System Scripts:** Bash  
**Deployment:** Any cloud provider or self-hosted  
**Analytics:** Python (optional ML libraries)

------------------------------------------------------------
## Project Structure

- /frontend - Dashboard UI, static files, scripts
- /backend - FastAPI application, routes, schemas, services
- /scripts - System metric collectors and utilities
- /db - Database schemas, migrations, exports
- /docs - Architecture diagrams, API documentation, installation notes
- /art - ASCII art, mockups, visual assets
- /tests - Unit tests, integration tests, load tests


------------------------------------------------------------
## Installation

1. Clone the repository:
```python
   git clone https://github.com/Laila-dAM/CyberPulse.git
```
2. Enter the project directory:
```python
   cd CyberPulse
```
3. Create a virtual environment and install dependencies:
```python
   python -m venv venv  
   source venv/bin/activate     (Windows: venv\Scripts\activate)  
   pip install -r requirements.txt
```
4. Configure environment variables:
```python
   Copy from .env.example if available, then adjust the values (database URL, secret keys, etc.)
```
5. Initialize the database:
```python
   python create_db.py
```
6. Run the backend:
```python
   uvicorn backend.main:app --reload
```
7. Access the dashboard:
```python
   Open http://localhost:8000 in the browser.
```
------------------------------------------------------------
## Usage

- Use the Bash scripts in /scripts to collect metrics at defined intervals.
- The backend exposes REST endpoints for real-time and historical data.
- The dashboard displays charts, tables, alerts, and analytic results.
- The system can be deployed locally or in cloud environments.

------------------------------------------------------------
## API Summary

Main endpoints include:

- GET /metrics  
- GET /metrics/latest  
- GET /metrics/history  
- GET /alerts  
- GET /predict  

API documentation is automatically generated at /docs and /openapi.json.

------------------------------------------------------------
## Testing

The project provides unit tests and integration tests that can be executed with:
```python
   pytest
```
Load and performance tests may require additional tools depending on the environment.

------------------------------------------------------------
## Contributing

Contributions are welcome.  
Submit pull requests for improvements, new features, bug fixes, or documentation updates.

------------------------------------------------------------
## License

In progress...

------------------------------------------------------------
## Roadmap

Planned or optional future enhancements:

- Advanced anomaly detection models
- Log ingestion from external applications or servers
- Role-based access control and authentication system
- Docker and Kubernetes deployment templates
- Notifications triggered by alerts (email, webhook, Slack)
- Responsive dashboard for mobile displays

