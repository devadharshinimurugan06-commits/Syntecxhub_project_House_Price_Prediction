import streamlit as st
import pandas as pd
import joblib

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# ============================================================
# LOAD TRAINED MODEL
# ============================================================

@st.cache_resource
def load_model():
    return joblib.load("house_price_model.pkl")

model = load_model()

# ============================================================
# TITLE
# ============================================================

st.title("🏠 House Price Prediction")

st.write(
    "Enter the property details below to estimate the house price "
    "using the trained Linear Regression model."
)

st.divider()

# ============================================================
# INPUTS
# ============================================================

st.subheader("🏡 Enter Property Details")

col1, col2 = st.columns(2)

with col1:

    area_sqft = st.number_input(
        "Area (Sqft)",
        min_value=100.0,
        max_value=20000.0,
        value=1200.0,
        step=50.0
    )

    bedrooms = st.number_input(
        "Bedrooms",
        min_value=1,
        max_value=10,
        value=3,
        step=1
    )

    bathrooms = st.number_input(
        "Bathrooms",
        min_value=1,
        max_value=10,
        value=2,
        step=1
    )

    age_years = st.number_input(
        "Age (Years)",
        min_value=0.0,
        max_value=100.0,
        value=5.0,
        step=1.0
    )

    location = st.selectbox(
        "Location",
        ["Urban", "Suburban", "Downtown", "Rural"]
    )

with col2:

    furnishing_status = st.selectbox(
        "Furnishing Status",
        ["Furnished", "Semi-Furnished", "Unfurnished"]
    )

    property_type = st.selectbox(
        "Property Type",
        ["Apartment", "Independent House", "Villa", "Studio"]
    )

    parking_spaces = st.number_input(
        "Parking Spaces",
        min_value=0,
        max_value=10,
        value=1,
        step=1
    )

    garden_available = st.selectbox(
        "Garden Available",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

    distance_to_city_center = st.number_input(
        "Distance to City Center (Km)",
        min_value=0.0,
        max_value=100.0,
        value=5.0,
        step=0.5
    )

st.divider()

# ============================================================
# PREDICTION
# ============================================================

if st.button("🔮 Predict House Price", use_container_width=True):

    input_data = pd.DataFrame({
        "Area_Sqft": [area_sqft],
        "Bedrooms": [bedrooms],
        "Bathrooms": [bathrooms],
        "Age_Years": [age_years],
        "Location": [location],
        "Furnishing_Status": [furnishing_status],
        "Property_Type": [property_type],
        "Parking_Spaces": [parking_spaces],
        "Garden_Available": [garden_available],
        "Distance_To_City_Center_Km": [distance_to_city_center]
    })

    prediction = model.predict(input_data)[0]

    st.success("Prediction generated successfully!")

    st.metric(
        "Estimated House Price",
        f"₹{prediction:,.2f}"
    )

    st.subheader("Entered Property Details")

    display_data = input_data.copy()

    display_data["Garden_Available"] = display_data[
        "Garden_Available"
    ].map({
        0: "No",
        1: "Yes"
    })

    st.dataframe(
        display_data,
        use_container_width=True,
        hide_index=True
    )

# ============================================================
# MODEL PERFORMANCE
# ============================================================

st.divider()

st.subheader("📊 Model Performance")

col1, col2 = st.columns(2)

with col1:
    st.metric("R² Score", "0.9351")

with col2:
    st.metric("RMSE", "₹35,131.15")

st.caption(
    "Model: Linear Regression | Test R²: 0.9351 | "
    "Test RMSE: ₹35,131.15"
)
