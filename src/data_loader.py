import pandas as pd

COL_TIME = "Статистическое время"
COL_WIND = "Средняя скорость ветра(m/s)"
COL_POWER = "Нормализованная активная мощность"
COL_TEMP = "Средняя температура окружающей среды(°C)"

def load_turbine_history(path):
    df = pd.read_csv(path)
    df[COL_TIME] = pd.to_datetime(df[COL_TIME])
    df = df.sort_values(COL_TIME)
    df = df.rename(columns={
        COL_TIME: "timestamp",
        COL_WIND: "wind_speed",
        COL_POWER: "power",
        COL_TEMP: "temperature",
    })
    return df[["timestamp", "wind_speed", "power", "temperature"]]

def resample_hourly(df):
    df = df.set_index("timestamp").resample("1h").mean().reset_index()
    return df.dropna()
