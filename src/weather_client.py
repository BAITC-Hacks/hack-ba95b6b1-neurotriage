import requests
from datetime import datetime, timedelta

TURBINES = {
    "T1": {"lat": 43.645150, "lon": 78.535604},
    "T2": {"lat": 43.643198, "lon": 78.538828},
}

def get_forecast(lat, lon, start_date, hours=48):
    end_date = (datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=2)).strftime("%Y-%m-%d")
    url = "https://historical-forecast-api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": "temperature_2m,wind_speed_10m,wind_direction_10m",
        "timezone": "UTC",
    }
    r = requests.get(url, params=params, timeout=30)
    r.raise_for_status()
    return r.json()
