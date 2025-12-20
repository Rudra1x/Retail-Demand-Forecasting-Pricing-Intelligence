from prophet import Prophet
import mlflow

class ProphetTrainer:
    def train(self, df):
        prophet_df = df.rename(columns={"date": "ds", "units_sold": "y"})

        model = Prophet(
            yearly_seasonality=True,
            weekly_seasonality=True
        )

        model.fit(prophet_df)

        mlflow.log_param("model", "Prophet")
        mlflow.log_param("seasonality", "weekly + yearly")

        return model
