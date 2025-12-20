import pandas as pd
import mlflow
import mlflow.prophet
from prophet import Prophet

# ---------------------------
# MLflow setup
# ---------------------------
mlflow.set_tracking_uri("file:./mlruns")
mlflow.set_experiment("retail_demand_forecasting")

# ---------------------------
# Load clean data
# ---------------------------
DATA_PATH = "data/clean_base_table.parquet"

df = pd.read_parquet(DATA_PATH)

# Aggregate to daily demand (store-level or overall)
daily = (
    df.groupby("date")["units_sold"]
      .sum()
      .reset_index()
)

# Prophet requires ds / y
prophet_df = daily.rename(
    columns={"date": "ds", "units_sold": "y"}
)

# ---------------------------
# Train & log model
# ---------------------------
with mlflow.start_run() as run:
    model = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=True
    )

    model.fit(prophet_df)

    mlflow.prophet.log_model(
        model,
        artifact_path="prophet_model"
    )

    print("RUN_ID:", run.info.run_id)
