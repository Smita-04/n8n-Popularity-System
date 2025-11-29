from fastapi import FastAPI, HTTPException
import json
import os

app = FastAPI(
    title="n8n Workflow Popularity API",
    description="API to retrieve popular n8n workflows from YouTube, Forum, and Google.",
    version="1.0.0"
)

DATA_FILE = "workflows_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"data": []}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

@app.get("/")
def home():
    return {"message": "Welcome to the n8n Popularity API. Go to /docs for Swagger UI."}

@app.get("/workflows")
def get_all_workflows():
    """Returns all collected workflows."""
    db = load_data()
    return db

@app.get("/workflows/platform/{platform_name}")
def get_workflows_by_platform(platform_name: str):
    """Filter by platform: YouTube, Forum, or Google Search."""
    db = load_data()
    filtered = [w for w in db['data'] if w['platform'].lower() == platform_name.lower()]
    return {"count": len(filtered), "results": filtered}

@app.get("/workflows/country/{country_code}")
def get_workflows_by_country(country_code: str):
    """Filter by country: US, IN, or Global."""
    db = load_data()
    filtered = [w for w in db['data'] if w['country'].lower() == country_code.lower()]
    return {"count": len(filtered), "results": filtered}