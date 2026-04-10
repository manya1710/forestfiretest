import streamlit as st
import pickle
import numpy as np

# Page configuration
st.set_page_config(page_title="Forest Fire Prediction", page_icon="🔥", layout="centered")

# Load models
# Using exception handling in case of case-sensitivity issues with 'ridge.pkl' vs 'Ridge.pkl'
try:
    ridge_model = pickle.load(open('ridge.pkl', 'rb'))
except FileNotFoundError:
    ridge_model = pickle.load(open('Ridge.pkl', 'rb'))

standard_scaler = pickle.load(open('scaler.pkl', 'rb'))

# Header
st.title("🔥 Algerian Forest Fire Prediction")
st.markdown("Enter the meteorological details below to predict the Fire Weather Index (FWI) or related target variable based on the Ridge Regression model.")

st.markdown("---")

# Layout with columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("Weather Metrics")
    Temperature = st.number_input("Temperature (°C)", min_value=-20.0, max_value=60.0, value=30.0, step=1.0)
    RH = st.number_input("Relative Humidity (%)", min_value=0.0, max_value=100.0, value=50.0, step=1.0)
    Ws = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=100.0, value=15.0, step=1.0)
    Rain = st.number_input("Rain (mm)", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    
with col2:
    st.subheader("Fire Indices & Meta")
    FFMC = st.number_input("FFMC Index", min_value=0.0, max_value=100.0, value=50.0, step=1.0)
    DMC = st.number_input("DMC Index", min_value=0.0, max_value=300.0, value=50.0, step=1.0)
    ISI = st.number_input("ISI Index", min_value=0.0, max_value=100.0, value=5.0, step=0.1)
    
    # Assuming standard encoding: Classes (0=Not Fire, 1=Fire) and Region (0=Bejaia, 1=Sidi Bel-abbes)
    Classes = st.selectbox("Classes", options=[0, 1], format_func=lambda x: "Not Fire (0)" if x == 0 else "Fire (1)")
    Region = st.selectbox("Region", options=[0, 1], format_func=lambda x: "Bejaia (0)" if x == 0 else "Sidi Bel-abbes (1)")

st.markdown("---")

# Prediction logic
if st.button("Predict Results", use_container_width=True):
    # The order must match exactly what was defined in the scaler and ridge model:
    # Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region
    features = [[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]]
    
    # Scale features
    new_data_scaled = standard_scaler.transform(features)
    
    # Predict
    result = ridge_model.predict(new_data_scaled)
    
    # Display result
    st.success(f"### Predicted Value : {result[0]:.4f}")
    st.balloons()
