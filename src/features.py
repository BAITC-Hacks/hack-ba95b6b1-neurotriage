def build_features(df):
    df = df.copy()
    df["hour"] = df["timestamp"].dt.hour
    df["dayofweek"] = df["timestamp"].dt.dayofweek
    df["month"] = df["timestamp"].dt.month
    df["wind_speed_sq"] = df["wind_speed"] ** 2
    df["wind_speed_cube"] = df["wind_speed"] ** 3
    return df

FEATURE_COLS = ["wind_speed", "wind_speed_sq", "wind_speed_cube",
                 "temperature", "hour", "dayofweek", "month"]
