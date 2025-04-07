import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open('linear_model.pkl', 'rb'))

st.title("NYC Taxi Fare Predictor 🚖")

st.markdown("Enter trip details to predict the total fare amount.")

# Input fields (fare_amount removed)
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=10, value=1)
trip_distance = st.number_input("Trip Distance (in miles)", min_value=0.0, value=1.0, step=0.1)
extra = st.number_input("Extra Charges ($)", min_value=0.0, value=0.5, step=0.1)
mta_tax = st.number_input("MTA Tax ($)", min_value=0.0, value=0.5, step=0.1)
tip_amount = st.number_input("Tip Amount ($)", min_value=0.0, value=1.0, step=0.5)
tolls_amount = st.number_input("Tolls Amount ($)", min_value=0.0, value=0.0, step=0.5)
improvement_surcharge = st.number_input("Improvement Surcharge ($)", min_value=0.0, value=0.3, step=0.1)
congestion_surcharge = st.number_input("Congestion Surcharge ($)", min_value=0.0, value=2.5, step=0.5)
trip_duration = st.number_input("Trip Duration (in seconds)", min_value=0, value=600, step=30)

# Predict
if st.button("Predict Total Amount"):
    features = np.array([[trip_distance, extra, mta_tax, tip_amount, tolls_amount,
                          improvement_surcharge, congestion_surcharge, trip_duration, passenger_count]])
    prediction = model.predict(features)
    st.success(f"Predicted Total Amount: ${prediction[0]:.2f}")
