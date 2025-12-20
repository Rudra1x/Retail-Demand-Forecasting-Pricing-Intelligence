import streamlit as st
import pandas as pd
import mlflow
import mlflow.prophet
import matplotlib.pyplot as plt

st.set_page_config(page_title="Retail Demand Forecasting", layout="wide")


# Load model

RUN_ID = "2ae36fc637bb4cdba50ee66ee6adc817"
MODEL_URI = f"runs:/{RUN_ID}/prophet_model"

@st.cache_resource
def load_model():
    return mlflow.prophet.load_model(MODEL_URI)

model = load_model()

st.title("📊 Retail Demand Forecasting & Pricing Intelligence")


# Sidebar

st.sidebar.header("Forecast Settings")
periods = st.sidebar.selectbox(
    "Forecast Horizon (days)",
    [7, 14, 30]
)


# Forecast Section

if st.sidebar.button("Generate Forecast"):
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)

    result = (
        forecast[["ds", "yhat"]]
        .tail(periods)
        .rename(columns={"ds": "Date", "yhat": "Forecasted Demand"})
    )

    st.subheader("📈 Forecasted Demand")
    st.line_chart(result.set_index("Date"))

    st.dataframe(result)

    st.download_button(
        label="Download Forecast CSV",
        data=result.to_csv(index=False),
        file_name="forecast.csv",
        mime="text/csv"
    )


# Business Explanation

st.markdown("---")
st.subheader("💡 How This Helps the Business")
st.write("""
- Forecasts future demand using historical sales patterns  
- Helps reduce stockouts and overstocking  
- Supports data-driven inventory and pricing decisions  
""")
