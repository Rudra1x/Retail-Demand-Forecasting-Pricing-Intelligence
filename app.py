from fastapi import FastAPI
import mlflow
import mlflow.prophet

app = FastAPI(title="Retail Demand Forecasting API")

RUN_ID = "2ae36fc637bb4cdba50ee66ee6adc817"
MODEL_URI = f"runs:/{RUN_ID}/prophet_model"

@app.on_event("startup")
def load_model():
    global model
    model = mlflow.prophet.load_model(MODEL_URI)
    print("Prophet model loaded successfully")

@app.get("/")
def health():
    return {"status": "API is running"}

@app.get("/forecast")
def forecast(periods: int = 30):
    future = model.make_future_dataframe(periods=periods)
    forecast_df = model.predict(future)

    result = (
        forecast_df[["ds", "yhat"]]
        .tail(periods)
        .rename(columns={"ds": "date", "yhat": "forecast_demand"})
    )

    return result.to_dict(orient="records")
