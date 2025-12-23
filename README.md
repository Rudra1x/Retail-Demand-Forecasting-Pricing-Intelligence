# Retail Demand Forecasting & Pricing Intelligence (MLOps Project)

## 📌 Overview
Retail businesses face persistent challenges such as demand uncertainty, stockouts, overstocking, and ineffective pricing decisions.  
This project delivers an **end-to-end retail demand forecasting and pricing intelligence system** that combines time-series modeling, machine learning, and industry-grade MLOps practices.

The solution is designed to be:
- Business-facing
- Interpretable
- Reproducible
- Production-ready

---

## 🎯 Business Objectives
- Forecast short- and medium-term product demand
- Reduce stockouts and excess inventory
- Enable data-driven pricing decisions
- Quantify revenue impact of pricing strategies

---

## 📊 Dataset
A curated subset of the **Walmart M5 Forecasting dataset** was used:
- Historical daily sales data
- Calendar and seasonal features
- Historical product pricing

To ensure realism and feasibility:
- Selected stores and product categories were used
- Full temporal history was preserved to capture seasonality
- Sparse demand behavior was intentionally retained

---

## 🧠 Modeling Approach

### Demand Forecasting
- **Model:** Prophet  
- **Rationale:**
  - Explicit modeling of trend and seasonality
  - Robust performance under missing or noisy data
  - Interpretable components for business stakeholders

- **Evaluation Metric:** SMAPE  
  (MAPE was avoided due to instability under zero or near-zero demand)

- **Result:** ~26% SMAPE on validation data

---

### Pricing & Elasticity Modeling
- Machine learning models were used to estimate **price elasticity of demand**
- Log-log regression and regularized models quantified demand sensitivity to price changes
- Pricing simulations were conducted to estimate revenue impact

- **Business Impact:**  
  Simulated pricing strategies indicated a potential **~9% revenue uplift**

---

## 🏗️ System Architecture

Raw Data
↓
Data Validation & Preparation
↓
Demand Forecasting (Prophet)
↓
MLflow Experiment Tracking
↓
Interactive ML Application (Streamlit)
↓
Inventory & Pricing Decisions


---

## ⚙️ MLOps & Productionization
This project follows real-world MLOps principles:

- **MLflow**
  - Experiment tracking
  - Model logging and versioning

- **Modular Pipelines**
  - Training pipeline
  - Prediction pipeline

- **FastAPI (Optional Backend)**
  - Programmatic access to forecasts

- **Streamlit Application**
  - Interactive UI for business users
  - Forecast visualization and CSV export

- **Docker**
  - Reproducible and portable deployment

---

## 🖥️ Interactive ML Application
The Streamlit-based application enables non-technical users to:
- Select forecast horizons (7 / 14 / 30 days)
- Visualize future demand trends
- Download forecast results
- Understand business impact without interacting with APIs

This design allows seamless adoption by partner companies and stakeholders.

---

## 📈 Key Metrics

| Metric | Value |
|------|------|
| Forecast Accuracy (SMAPE) | ~26% |
| Revenue Uplift (Simulated) | ~9% |
| Primary Use Case | Inventory & Pricing Decisions |

---

## 🚀 How to Run the Project

### Option 1: Run with Docker (Recommended)

```bash
docker build -t retail-forecast-app .
docker run -p 8501:8501 retail-forecast-app

Open in browser:

http://localhost:8501

Option 2: Run Locally (Without Docker)
pip install -r requirements.txt
streamlit run streamlit_app.py
```
## Project Structure
mlops_retail_demand/
│
├── src/
│   ├── components/
│   ├── pipeline/
│   └── utils/
│
├── data/
├── notebooks/
├── streamlit_app.py
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md

🧪 Key Learnings

Classical time-series models can outperform ML under strong seasonality

Metric choice is critical for sparse retail demand data

ML delivers maximum value in pricing and elasticity analysis rather than raw forecasting

Business usability is as important as model accuracy

📌 Future Improvements

Hierarchical forecasting across stores and categories

Automated retraining schedules

Data drift monitoring

Integration with inventory management systems

👤 Author 
Rudraksh Sharma
Developed as an industry-aligned MLOps portfolio project focused on solving real-world retail analytics problems.
