from fastapi import FastAPI
from datetime import datetime, timedelta

app=FastAPI()


@app.get("/")
def get_details(slack_name: str, track: str):
    current_day = datetime.now().strftime("%A")
    utc_time = datetime.now() + timedelta(minutes=2)
    
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