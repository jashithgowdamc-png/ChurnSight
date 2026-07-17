import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder

st.set_page_config(
    page_title="ChurnSight - Predict Churn",
    page_icon="🎯",
    layout="wide"
)


#LOAD MODEL
model = joblib.load(r'C:\Users\jashi\OneDrive\Desktop\ChurnSight\models\logistic_regression.pkl')

st.title("🎯 ChurnSight — Live Churn Prediction")
st.markdown("Enter customer details below to predict churn risk.")
st.markdown("---")


#INPUT FORM
st.subheader("Customer Details")

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior_citizen = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure = st.slider("Tenure (Months)", 0, 72, 12)
    phone_service = st.selectbox("Phone Service", ["Yes", "No"])
    multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])

with col2:
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
    device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
    tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
    streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])

with col3:
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
    payment_method = st.selectbox("Payment Method", [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ])
    monthly_charges = st.slider("Monthly Charges ($)", 0, 150, 65)
    total_charges = st.slider("Total Charges ($)", 0, 9000, 1000)

st.markdown("---")


#FEATURE ENGINEERING
high_value = 1 if monthly_charges > 64.76 else 0
charge_ratio = total_charges / (tenure + 1)

service_list = [phone_service, online_security, online_backup,
                device_protection, tech_support, streaming_tv, streaming_movies]
service_count = sum(1 for s in service_list if s == "Yes")


#BUILD INPUT DATAFRAME
input_data = pd.DataFrame({
    'gender': [gender],
    'SeniorCitizen': [senior_citizen],
    'Partner': [partner],
    'Dependents': [dependents],
    'tenure': [tenure],
    'PhoneService': [phone_service],
    'MultipleLines': [multiple_lines],
    'InternetService': [internet_service],
    'OnlineSecurity': [online_security],
    'OnlineBackup': [online_backup],
    'DeviceProtection': [device_protection],
    'TechSupport': [tech_support],
    'StreamingTV': [streaming_tv],
    'StreamingMovies': [streaming_movies],
    'Contract': [contract],
    'PaperlessBilling': [paperless_billing],
    'PaymentMethod': [payment_method],
    'MonthlyCharges': [monthly_charges],
    'TotalCharges': [total_charges],
    'high_value': [high_value],
    'charges_ratio': [charge_ratio],
    'service_count': [service_count]
})


#ENCODE INPUT
le = LabelEncoder()
cat_cols = input_data.select_dtypes(include='object').columns.tolist()
for col in cat_cols:
    input_data[col] = le.fit_transform(input_data[col].astype(str))


#PREDICT BUTTON
if st.button("🎯 Predict Churn", use_container_width=True):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1] * 100

    st.markdown("---")
    st.subheader("Prediction Result")

    col1, col2 = st.columns(2)

    with col1:
        if prediction == 1:
            st.error(f"⚠️ Customer is likely to CHURN")
        else:
            st.success(f"✅ Customer is likely to STAY")

    with col2:
        st.metric("Churn Probability", f"{probability:.1f}%")

    st.markdown("---")

    # Risk Level
    if probability >= 70:
        st.error("🔴 Risk Level: HIGH — Immediate action needed")
    elif probability >= 40:
        st.warning("🟡 Risk Level: MEDIUM — Monitor this customer")
    else:
        st.success("🟢 Risk Level: LOW — Customer is stable")

st.markdown("---")
st.caption("ChurnSight — Built with Python & Streamlit")