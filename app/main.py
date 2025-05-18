import streamlit as st
import numpy as np
import joblib

model = joblib.load("models/model.pkl")
scaler = joblib.load("models/scaler.pkl")

st.title("Credit Risk Prediction")
st.header("Enter the details of the customer")

age = st.slider("Age", 18, 100, 30)
income = st.number_input("Annual Income ($)", min_value=0)
home = st.selectbox("Home Ownership", ["OWN", "MORTGAGE", "RENT", "OTHER"])
emp_length = st.slider("Employement Length (years)", 0, 50, 5)
loan_amount = st.number_input("Loan Amount  ($)", min_value=500)
loan_int_rate = st.number_input("Interest Rate (%)", min_value=0.0)
loan_intent = st.selectbox(
    "Loan Purpose",
    [
        "EDUCATION",
        "MEDICAL",
        "VENTURE",
        "PERSONAL",
        "HOMEIMPROVEMENT",
        "DEBTCONSOLIDATION",
    ],
)

loan_grade = st.selectbox("Loan Grade", ["A", "B", "C", "D", "E", "F", "G"])
credit_history = st.selectbox("Previously Defaulted ?", ["Y", "N"])
cb_age = st.slider("Credit Bureau Age (months)", 0, 240, 50)
cb_score = st.number_input("Credit Bureau Score", min_value=300, max_value=850)


def preprocess_input():
    home_own = 1 if home == "OWN" else 0
    home_rent = 1 if home == "RENT" else 0
    home_other = 1 if home == "OTHER" else 0

    loan_intents = [
        "EDUCATION",
        "MEDICAL",
        "VENTURE",
        "PERSONAL",
        "HOMEIMPROVEMENT",
    ]

    intent_encoded = [1 if loan_intent == x else 0 for x in loan_intents]

    grade_list = ["B", "C", "D", "E", "F", "G"]
    grade_encoded = [1 if loan_grade == x else 0 for x in grade_list]

    default_flag = 1 if credit_history == "Y" else 0

    return np.array(
        [
            [
                age,
                income,
                emp_length,
                loan_amount,
                loan_int_rate,
                cb_age,
                cb_score,
                home_other,
                home_own,
                home_rent,
                *intent_encoded,
                *grade_encoded,
                default_flag,
            ]
        ]
    )


# Predict
if st.button("Check Risk"):
    X_input = preprocess_input()
    X_scaled = scaler.transform(X_input)
    prediction = model.predict(X_scaled)[0]

    if prediction == 1:
        st.error("❌ High Credit Risk (Likely to Default)")
    else:
        st.success("✅ Low Credit Risk (Likely to Repay)")
