import streamlit as st
import joblib

model = joblib.load("fraud_model.pkl")

st.title("💳 Fraud Detection System")
st.write("Enter transaction details below to predict if it's fraud:")

# Input fields
customer_id = st.text_input("Customer ID")
terminal_id = st.text_input("Terminal ID")
tx_amount = st.number_input("Transaction Amount (₹)", min_value=0.0, step=0.01)
tx_time_seconds = st.number_input("Transaction Time (seconds)", min_value=0, step=1)
tx_time_days = st.number_input("Transaction Day (e.g., 159 means 159th day of year)", min_value=0, step=1)
tx_fraud_scenario = st.selectbox("Fraud Scenario", [0, 1])
extra_feature = st.number_input("Extra Feature", min_value=0.0, step=0.01)

# Safe conversion function
def convert_input(value, default=0.0):
    try:
        return float(value)
    except ValueError:
        return default  

if st.button("🔍 Predict Fraud"):
    # Convert inputs safely to float
    input_data = [[
        convert_input(customer_id),
        convert_input(terminal_id),
        convert_input(tx_amount),
        convert_input(tx_time_seconds),
        convert_input(tx_time_days),
        convert_input(tx_fraud_scenario),
        convert_input(extra_feature)
    ]]
    
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ Fraudulent Transaction Detected!")
    else:
        st.success("✅ Transaction is Safe.")
