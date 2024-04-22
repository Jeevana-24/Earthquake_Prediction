import requests
import json
from datetime import datetime, timedelta

def fetch_earthquake_data():
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&limit=50&orderby=time"
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None

def fetch_earthquake_data_last_30_days():
    date_30_days_ago = datetime.now() - timedelta(days=30)
    start_time = date_30_days_ago.strftime("%Y-%m-%d")
    url = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&limit=5&orderby=magnitude&starttime={start_time}"
    response = requests.get(url)
    return json.loads(response.text) if response.status_code == 200 else None

