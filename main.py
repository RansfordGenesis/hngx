from fastapi import FastAPI
from datetime import datetime, timedelta
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)   


@app.get("/api/")
def get_details(slack_name: str, track: str):
    if not slack_name or not track:
        return {"error": "Both slack_name and track parameters are required."}, 400
    
    current_day = datetime.now().strftime("%A")
    utc_time = utc_time = datetime.utcnow() + timedelta(minutes=2)
    
    details = {
        
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": "https://github.com/RansfordGenesis/hngx/blob/main/main.py",
        "github_repo_url": "https://github.com/RansfordGenesis/hngx",
        "status_code": 200
        }
    
    return details