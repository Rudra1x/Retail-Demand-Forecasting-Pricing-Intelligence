class PredictionPipeline:
    def predict(self, model, periods=30):
        future = model.make_future_dataframe(periods=periods)
        forecast = model.predict(future)
        return forecast[["ds", "yhat"]]
