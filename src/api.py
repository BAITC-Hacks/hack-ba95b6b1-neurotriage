from fastapi import FastAPI
import pandas as pd
import os

app = FastAPI(title="VES Forecast API", description="Прогноз почасовой выработки ВЭС")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/forecast")
def get_forecast(turbine_id: str = None, date: str = None):
    """
    Получить прогноз выработки.
    turbine_id: T1 или T2 (необязательно)
    date: дата в формате YYYY-MM-DD (необязательно)
    """
    path = "data/forecast_output.csv"
    if not os.path.exists(path):
        return {"error": "Прогноз ещё не построен. Запустите python -m src.main"}

    df = pd.read_csv(path)

    if turbine_id:
        df = df[df["turbine_id"] == turbine_id]
    if date:
        df = df[df["timestamp"].astype(str).str.startswith(date)]

    return df.to_dict(orient="records")

@app.get("/turbines")
def list_turbines():
    path = "data/forecast_output.csv"
    if not os.path.exists(path):
        return {"error": "Прогноз ещё не построен"}
    df = pd.read_csv(path)
    return {"turbines": df["turbine_id"].unique().tolist()}