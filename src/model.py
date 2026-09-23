from catboost import CatBoostRegressor
from src.features import build_features, FEATURE_COLS

def train_model(df, target_col="power"):
    df = build_features(df)
    X = df[FEATURE_COLS]
    y = df[target_col]
    model = CatBoostRegressor(
        iterations=500, learning_rate=0.05, depth=6,
        loss_function="RMSE", verbose=False
    )
    model.fit(X, y)
    return model

def save_model(model, path):
    model.save_model(path)

def load_model(path):
    model = CatBoostRegressor()
    model.load_model(path)
    return model

def predict(model, forecast_df):
    forecast_df = build_features(forecast_df)
    return model.predict(forecast_df[FEATURE_COLS])
    return preds.clip(0, 1)