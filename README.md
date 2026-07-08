# ReliabilityMonitor

A production-oriented asynchronous monitoring service built with FastAPI and AsyncIO. This service tracks the health, latency, and availability of critical API endpoints through automated health checks.

## Key Features
- **Asynchronous Execution:** Uses `AsyncIO` and `httpx` to perform non-blocking health checks, ensuring high performance.
- **Telemetry Logging:** Tracks status codes and response latency (ms) for performance observability.
- **Modular Design:** Easily configurable list of target endpoints.
- **Health Endpoint:** Exposes a JSON API (`/health`) to retrieve recent monitoring logs.

## Tech Stack
- **Framework:** FastAPI
- **Concurrency:** AsyncIO
- **HTTP Client:** httpx

## Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `uvicorn main:app --reload`
