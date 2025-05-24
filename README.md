# 💳 Credit Risk Predictor

A machine learning-powered web app that predicts whether a loan applicant is a high or low credit risk based on personal and financial attributes. Built using **Streamlit**, **Scikit-learn**, and **pandas** for end-to-end analysis and deployment.

## 🚀 Demo

[👉 Live Demo Link ](https://creditrisk-predictor.streamlit.app/)

## 📊 Features

- Predicts credit risk (default/no-default) using a trained **Random Forest Classifier**.
- Clean, interactive UI built with **Streamlit**.
- Handles categorical variables like loan intent, grade, and home ownership through custom encoding.
- Real-time prediction based on user input values.
- Data preprocessing: missing value handling, feature scaling, encoding.

## 🧠 Model Info

- **Algorithm:** Random Forest Classifier
- **Metrics Evaluated:** Accuracy, Precision, Recall
- **Preprocessing:** StandardScaler, One-hot encoding for categorical data

## 🏗 Tech Stack

- Python
- Scikit-learn
- Streamlit
- Pandas / NumPy
- Pickle

## 🛠 How to Run Locally

```bash
git clone https://github.com/your-username/credit-risk-predictor.git
cd credit-risk-predictor
pip install -r requirements.txt
streamlit run app/main.py
