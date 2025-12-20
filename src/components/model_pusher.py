import mlflow

class ModelPusher:
    def push(self, model):
        mlflow.prophet.log_model(model, artifact_path="prophet_model")
