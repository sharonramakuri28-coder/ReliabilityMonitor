import asyncio
import httpx
import time
from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="ReliabilityMonitor")

# Configuration: Endpoints to monitor
MONITOR_TARGETS = [
    "https://api.github.com",
    "https://www.google.com"
]

# Simple in-memory storage for monitoring logs
status_logs = []

async def check_health(url: str):
    start_time = time.time()
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=5.0)
            latency = (time.time() - start_time) * 1000
            return {
                "url": url,
                "status": response.status_code,
                "latency_ms": round(latency, 2),
                "timestamp": datetime.now().isoformat()
            }
    except Exception as e:
        return {"url": url, "status": "Error", "error": str(e), "timestamp": datetime.now().isoformat()}

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(run_periodic_checks())

async def run_periodic_checks():
    while True:
        for url in MONITOR_TARGETS:
            result = await check_health(url)
            status_logs.append(result)
            if len(status_logs) > 50: status_logs.pop(0) # Keep only last 50
        await asyncio.sleep(60) # Run every 60 seconds

@app.get("/health")
async def get_health():
    return {"status": "operational", "logs": status_logs}