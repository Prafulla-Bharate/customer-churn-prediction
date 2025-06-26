import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the trained model
with open("churn_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

st.title("📊 Customer Churn Prediction")

# Collect user inputs
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", ["No", "Yes"])
partner = st.selectbox("Has Partner?", ["Yes", "No"])
dependents = st.selectbox("Has Dependents?", ["Yes", "No"])
tenure = st.number_input("Tenure (months)", min_value=0)
phone_service = st.selectbox("Phone Service", ["Yes", "No"])
multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
payment_method = st.selectbox("Payment Method", [
    "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
])
monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0)
total_charges = st.number_input("Total Charges ($)", min_value=0.0)

# Create DataFrame for model input
input_dict = {
    "gender": [gender],
    "SeniorCitizen": [1 if senior == "Yes" else 0],
    "Partner": [partner],
    "Dependents": [dependents],
    "tenure": [tenure],
    "PhoneService": [phone_service],
    "MultipleLines": [multiple_lines],
    "InternetService": [internet_service],
    "OnlineSecurity": [online_security],
    "OnlineBackup": [online_backup],
    "DeviceProtection": [device_protection],
    "TechSupport": [tech_support],
    "StreamingTV": [streaming_tv],
    "StreamingMovies": [streaming_movies],
    "Contract": [contract],
    "PaperlessBilling": [paperless_billing],
    "PaymentMethod": [payment_method],
    "MonthlyCharges": [monthly_charges],
    "TotalCharges": [total_charges]
}

input_df = pd.DataFrame(input_dict)

# Match training format (one-hot encoding)
input_encoded = pd.get_dummies(input_df)
# Add any missing columns that the model was trained on
model_features = model.feature_names_in_ if hasattr(model, 'feature_names_in_') else model.get_booster().feature_names
missing_cols = set(model_features) - set(input_encoded.columns)
for col in missing_cols:
    input_encoded[col] = 0
input_encoded = input_encoded[model_features]  # Ensure correct order

# Predict
if st.button("Predict Churn"):
    prediction = model.predict(input_encoded)
    if prediction[0] == 1:
        st.error("⚠️ Customer is likely to Churn!")
    else:
        st.success("✅ Customer is NOT likely to Churn!")
