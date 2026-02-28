import streamlit as st
import pickle
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Smart House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
}

/* Full page background gradient */
.stApp {
    background: linear-gradient(135deg, #84b179, #a2cb8b, #c7eabb, #e8f5bd);
}

/* Main card container */
.main-card {
    background: rgba(255, 255, 255, 0.85);
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

/* Title */
.title {
    font-size: 42px;
    font-weight: 600;
    text-align: center;
    color: #2f5233;
}

.subtitle {
    text-align: center;
    color: #4f6f52;
    margin-bottom: 30px;
}

/* Section Headers */
.section-header {
    font-size: 22px;
    font-weight: 600;
    color: #2f5233;
    margin-bottom: 15px;
}

/* Button styling */
.stButton>button {
    background: linear-gradient(90deg, #84b179, #2f5233);
    color: white;
    font-size: 18px;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.03);
    background: linear-gradient(90deg, #2f5233, #84b179);
}

/* Prediction box */
.result-box {
    background: #ffffff;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    font-size: 24px;
    font-weight: 600;
    color: #2f5233;
    box-shadow: 0 5px 20px rgba(0,0,0,0.1);
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.markdown('<div class="title">🏠 Smart House Price Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered intelligent real estate valuation</div>', unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("Model/best_model.pkl", "rb"))

# ---------------- LAYOUT ----------------
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section-header">📋 Property Details</div>', unsafe_allow_html=True)
    area = st.number_input("Area (sqft)", 500, 10000, 1500)
    bedrooms = st.number_input("Bedrooms", 1, 10, 3)
    bathrooms = st.number_input("Bathrooms", 1, 10, 2)
    floors = st.number_input("Floors", 1, 5, 1)

with col2:
    st.markdown('<div class="section-header">🏘 Additional Features</div>', unsafe_allow_html=True)
    age = st.number_input("Age of House (Years)", 0, 100, 5)
    garage = st.selectbox("Garage Available?", ["No", "Yes"])
    location_score = st.slider("Location Score (1-10)", 1, 10, 5)

garage_value = 1 if garage == "Yes" else 0

st.write("")

# ---------------- PREDICTION ----------------
if st.button("🚀 Predict House Price"):
    input_data = np.array([[area, bedrooms, bathrooms, floors, age, garage_value, location_score]])
    prediction = model.predict(input_data)

    st.markdown(
        f'<div class="result-box">💰 Estimated Price: ₹ {prediction[0]:,.2f}</div>',
        unsafe_allow_html=True
    )
    st.balloons()

st.markdown('</div>', unsafe_allow_html=True)