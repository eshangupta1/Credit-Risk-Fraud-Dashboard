import streamlit as st
import numpy as np
import pandas as pd
import joblib
import json

st.set_page_config(layout="centered")
st.title("💳 Credit Risk Prediction")

st.markdown("Fill out the details below to check if an applicant is high risk.")

# Load model and features
model = joblib.load("xgb_model.pkl")
with open("selected_features.json", "r") as f:
    features = json.load(f)

# Create a form
with st.form("input_form"):
    col1, col2 = st.columns(2)

    loan_amnt = col1.number_input("Loan Amount", value=10000)
    annual_inc = col2.number_input("Annual Income", value=50000)
    dti = col1.number_input("Debt-to-Income Ratio", value=15.0)
    fico_mean = col2.number_input("FICO Score (Average)", value=680)
    term = col1.selectbox("Loan Term (months)", [36, 60])
    emp_length = col2.slider("Employment Length (years)", 0, 40, 5)
    home_ownership = col1.selectbox("Home Ownership", ["RENT", "OWN", "MORTGAGE", "OTHER"])
    purpose = col2.selectbox("Loan Purpose", ["credit_card", "debt_consolidation", "home_improvement", "major_purchase", "small_business", "other"])

    submitted = st.form_submit_button("Predict")

    if submitted:
        # Encode categorical manually for demo (simplified)
        home_map = {"RENT": 0, "OWN": 1, "MORTGAGE": 2, "OTHER": 3}
        purpose_map = {
            "credit_card": 0,
            "debt_consolidation": 1,
            "home_improvement": 2,
            "major_purchase": 3,
            "small_business": 4,
            "other": 5
        }

        input_dict = {
            "loan_amnt": loan_amnt,
            "annual_inc": annual_inc,
            "dti": dti,
            "fico_mean": fico_mean,
            "term": term,
            "emp_length": emp_length,
            "home_ownership": home_map[home_ownership],
            "purpose": purpose_map[purpose]
        }

        input_df = pd.DataFrame([input_dict])
        pred = model.predict(input_df)[0]
        prob = model.predict_proba(input_df)[0][1]

        st.subheader("🔍 Prediction Result")
        st.write(f"**Default Probability:** {prob:.2f}")
        if prob > 0.7:
            st.error("⚠️ High Risk Applicant")
        else:
            st.success("✅ Low Risk Applicant")