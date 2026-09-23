import pandas as pd
import matplotlib.pyplot as plt

def check_output(path="data/forecast_output.csv"):
    df = pd.read_csv(path)
    print("Всего строк:", len(df))
    print("Пропуски:", df.isnull().sum().to_dict())
    print("Отрицательные power_pred:", (df["power_pred"] < 0).sum())
    print("Диапазон power_pred:", df["power_pred"].min(), "-", df["power_pred"].max())
    print(df.groupby("turbine_id")["power_pred"].describe())
    return df

def plot_forecast(df, out_path="forecast_plot.png"):
<<<<<<< HEAD
    fig, axes = plt.subplots(2, 1, figsize=(14, 8), sharex=True)
    for ax, tid in zip(axes, df["turbine_id"].unique()):
        sub = df[df["turbine_id"] == tid]
        ax.plot(pd.to_datetime(sub["timestamp"]), sub["power_pred"], linewidth=0.8)
=======
    df = df.copy()
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["forecast_made_on"] = pd.to_datetime(df["forecast_made_on"])
    df = df.sort_values(["turbine_id", "forecast_made_on", "timestamp"])
    df = df.drop_duplicates(subset=["turbine_id", "timestamp"], keep="last")
    df = df.sort_values(["turbine_id", "timestamp"])

    fig, axes = plt.subplots(2, 1, figsize=(14, 8), sharex=True)
    for ax, tid in zip(axes, df["turbine_id"].unique()):
        sub = df[df["turbine_id"] == tid]
        ax.plot(sub["timestamp"], sub["power_pred"], linewidth=0.8)
>>>>>>> a2649bdabc2601e1bba920d24f5689fcfeeb85d3
        ax.set_title(f"Прогноз мощности — {tid}")
        ax.set_ylabel("power_pred")
        ax.grid(alpha=0.3)
    plt.xlabel("Время")
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    print(f"Сохранено: {out_path}")

<<<<<<< HEAD
if name == "__main__":
    df = check_output()
    plot_forecast(df)
=======
if __name__ == "__main__":
    df = check_output()
    plot_forecast(df)
>>>>>>> a2649bdabc2601e1bba920d24f5689fcfeeb85d3
