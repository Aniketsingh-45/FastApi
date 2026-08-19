import streamlit as st
import requests

# Configure the page
st.set_page_config(
    page_title="Insurance Premium Predictor",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 Insurance Premium Predictor")
st.write("Enter the patient's details below to predict their estimated health insurance premium.")

st.markdown("---")

# Create a clean layout using columns
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=19, max_value=99, value=30, step=1, help="Must be between 19 and 99")
    bmi = st.number_input("BMI", min_value=18.1, max_value=99.9, value=25.0, step=0.1, help="Must be between 18.1 and 99.9")

with col2:
    smoker = st.selectbox("Smoker Status", options=["yes", "no"])
    # These are typical regions for the standard medical cost dataset, edit if your model expects different strings
    region = st.selectbox("Region", options=["southwest", "southeast", "northwest", "northeast"])

st.markdown("---")

# Prediction button
if st.button("Predict Premium", type="primary", use_container_width=True):
    # Prepare the payload for FastAPI
    payload = {
        "age": age,
        "bmi": bmi,
        "smoker": smoker,
        "region": region
    }
    
    try:
        # Make the POST request to the FastAPI backend
        with st.spinner("Calculating premium..."):
            response = requests.post("http://127.0.0.1:8000/predict", json=payload)
            
        # Check if the request was successful
        if response.status_code == 200:
            result = response.json()
            premium = result.get("premium", "Unknown")
            
            # Display the result prominently
            st.success("Prediction calculated successfully!")
            
            # Use st.metric for a beautiful UI component
            st.metric(
                label="Estimated Insurance Premium Category", 
                value=str(premium).title()
            )
            
            st.balloons() # Add a fun animation on success
            
        else:
            # Handle API errors gracefully
            st.error(f"Failed to get prediction (Status Code: {response.status_code})")
            st.json(response.json())
            
    except requests.exceptions.ConnectionError:
        # Handle the case where FastAPI is not running
        st.error("🚨 Could not connect to the backend API!")
        st.warning("Please ensure your FastAPI server is running. Open a terminal and run:\n`uvicorn ml:app --reload`")
