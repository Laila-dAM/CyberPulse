<h1 align="center">C Y B E R P U L S E</h1>

## What is it

**CyberPulse** is a lightweight **system monitoring and analytics platform** that collects system metrics (CPU, memory, processes) and displays them in a **real-time visual dashboard**.

This project was built to demonstrate **backend development, API design, and basic observability concepts**.

---

## Problem it solves

System monitoring tools are often complex and hard to understand for beginners.

CyberPulse provides:

* Centralized system metrics collection
* A clean REST API to access metrics
* A simple, visual dashboard for real-time monitoring
* An educational base to learn **monitoring and system analysis**

---

## What this project demonstrates

* REST API development with **FastAPI**
* System metrics collection using **psutil**
* Backend project organization and clean architecture
* Environment configuration with `.env`
* Automated testing with **pytest**
* Basic dashboard integration

Suitable for **IT / Software Engineering internship** portfolios.

---

## Tech stack

* Python
* FastAPI
* Uvicorn
* Psutil
* Pytest
* HTML / CSS / JavaScript

---

## How to run (copy & paste)

```bash
git clone https://github.com/Laila-dAM/CyberPulse.git
cd CyberPulse
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate     # Windows
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

Access:

* API: [http://localhost:8000](http://localhost:8000)
* Docs: [http://localhost:8000/docs](http://localhost:8000/docs)
* Dashboard: [http://localhost:8000/dashboard](http://localhost:8000/dashboard)

---

## Dashboard preview

> Add screenshots or a short GIF of the dashboard running here

---

## Environment variables (`.env.example`)

```env
APP_ENV=development
HOST=127.0.0.1
PORT=8000
LOG_LEVEL=info
```

---

## License

MIT License

--- 
<p align="center"> ૮ ˙Ⱉ˙ ა ʙᴜɴxɪᴇ.ᴢɪᴘ </p>
