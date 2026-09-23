import pandas as pd
from datetime import datetime, timedelta
from src.data_loader import load_turbine_history, resample_hourly
from src.model import train_model, save_model, predict
from src.weather_client import get_forecast, TURBINES

TURBINE_FILES = {
    "T1": "data/turbine_1.csv",
    "T2": "data/turbine_2.csv",
}

def weather_json_to_df(forecast_json):
    hourly = forecast_json["hourly"]
    return pd.DataFrame({
        "timestamp": pd.to_datetime(hourly["time"]),
        "wind_speed": hourly["wind_speed_10m"],
        "temperature": hourly["temperature_2m"],
    })

def run_agent(start="2026-01-31", end="2026-02-28"):
    models = {}
    for tid, path in TURBINE_FILES.items():
        print(f"[agent] обучение модели для {tid}")
        hist = load_turbine_history(path)
        hourly = resample_hourly(hist)
        models[tid] = train_model(hourly)
        save_model(models[tid], f"models/catboost_{tid}.cbm")

    results = []
    current = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")

    while current <= end_date:
        date_str = current.strftime("%Y-%m-%d")
        print(f"[agent] прогноз на {date_str}")
        for tid, coords in TURBINES.items():
            fjson = get_forecast(coords["lat"], coords["lon"], date_str)
            df = weather_json_to_df(fjson)
            df["power_pred"] = predict(models[tid], df)
            df["turbine_id"] = tid
            df["forecast_made_on"] = date_str
            results.append(df)
        current += timedelta(days=1)

    final = pd.concat(results)
    final.to_csv("data/forecast_output.csv", index=False)
    print("Готово: data/forecast_output.csv")
    return final

if __name__ == "__main__":
    run_agent()
