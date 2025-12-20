import os
from pathlib import Path

# Core source directory
project_name = "src"

list_of_files = [

    # -------------------- Core Package --------------------
    f"{project_name}/__init__.py",

    # -------------------- Components --------------------
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",

    # -------------------- Pipelines --------------------
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",

    # -------------------- Feature Store --------------------
    f"{project_name}/feature_store/__init__.py",
    f"{project_name}/feature_store/demand_features.py",

    # -------------------- Data Access Layer --------------------
    f"{project_name}/data_access/__init__.py",
    f"{project_name}/data_access/data_loader.py",

    # -------------------- Experiment Tracking --------------------
    f"{project_name}/experiments/__init__.py",
    f"{project_name}/experiments/mlflow_tracking.py",

    # -------------------- Configuration --------------------
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/mongo_db_connection.py",
    f"{project_name}/configuration/aws_connection.py",

    # -------------------- Cloud Storage --------------------
    f"{project_name}/cloud_storage/__init__.py",
    f"{project_name}/cloud_storage/aws_storage.py",

    # -------------------- Entities --------------------
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/estimator.py",
    f"{project_name}/entity/s3_estimator.py",

    # -------------------- Utilities --------------------
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",

    # -------------------- Constants --------------------
    f"{project_name}/constants/__init__.py",

    # -------------------- Logging & Exception --------------------
    f"{project_name}/logger/__init__.py",
    f"{project_name}/exception/__init__.py",

    # -------------------- Notebooks (Exploration Phase) --------------------
    "notebooks/01_data_understanding.ipynb",
    "notebooks/02_eda.ipynb",
    "notebooks/03_prophet_forecasting.ipynb",
    "notebooks/04_xgboost_forecasting.ipynb",
    "notebooks/05_elasticity_causal.ipynb",

    # -------------------- Configuration Files --------------------
    "config/model.yaml",
    "config/schema.yaml",

    # -------------------- App & Deployment --------------------
    "app.py",
    "demo.py",
    "Dockerfile",
    ".dockerignore",

    # -------------------- Project Metadata --------------------
    "requirements.txt",
    "setup.py",
    "pyproject.toml",
    "README.md",
]

# Create directories and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = filepath.parent

    if filedir != Path(""):
        os.makedirs(filedir, exist_ok=True)

    if not filepath.exists():
        with open(filepath, "w") as f:
            pass
    else:
        print(f"File already exists: {filepath}")
