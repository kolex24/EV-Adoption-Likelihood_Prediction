import streamlit as st
import pandas  as pd
import joblib

st.set_page_config(
    page_title="EV Adoption Prediction",
    page_icon="🚗",
    layout="centered"
)

@st.cache_resource
def load_model():
    return joblib.load("ev_model/ev_adoption_model.pkl")

model = load_model()

st.title("EV Adoption Likelihood Predictor")
st.write(
    "Enter a customer profile below to predict how likely they are to "
    "adopt an Electric Vehicle (EV): **Low**, **Medium**, or **High**."
)

with st.form("prediction_form"):
    
    st.subheader("Demographics")
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=18, max_value=100, value=30)
        age_group = st.selectbox(
            "Age Group",
            ["18-24","25-34", "35-44","45-54", "55-64", "65+"])
        education_level = st.selectbox(
            "Education Level",
            ["High School","Bachelor", "Master", "PhD"]
        )
    with col2:
        annual_income = st.number_input(
            "Annual Income ($)", min_value=0, max_value=1000000, value=350000, step=1000)
        annual_icome_brac = st.selectbox(
            "Annual Income Bracket",
            ["Low", "Medium", "High"]
        )
        city_type = st.selectbox(
            "City Type",
            ["Urban", "Suburban", "Rural"]
        )
    st.subheader("Vehicle & Commute")
    col3, col4 = st.columns(2)
    with col3:
        current_vehicle_type = st.selectbox(
            "Current Vehicle Type",
            ["Sedan", "SUV", "Truck"]
        )
        vehicle_age_years = st.number_input(
            "Current Vehicle Age (Years)", min_value=0.0, value=7.5, step=0.5
        )
        daily_commute_km = st.number_input(
            "Daily Commute (km)", min_value=0.0, value=10.0, step=0.5
        )
    with col4:
        weekly_travel_distance_km = st.number_input(
            "Weekly Travel Distance (km)", min_value=0.0, value=50.0, step=0.5
        )
        commute_categories = st.selectbox(
            "Commute Categories",
            ["Very Short", "Short", "Medium", "Long", "Very Long"]
        )
        fuel_expense_per_month = st.number_input(
            "Fuel Expense per Month ($)", min_value=0.0, value=100.0, step=10.0
        )
    st.subheader("Charging Access & Cost")
    col5, col6 = st.columns(2)
    with col5:
        charging_station_accessibility = st.slider(
            "Charging Station Accessibility (1-5)",
            1.0, 5.0, 4.0
        )
        nearest_charging_station_km = st.number_input(
            "Nearest Charging Station (km)", min_value=0.0, value=55.0, step=0.5
        )
        home_charging_available = st.selectbox(
            "Home Charging Available",
            [1, 0]
        )
    with col6:
        electricity_cost_per_kwh = st.number_input(
            "Electricity Cost per kWh ($)", min_value=0.0, value=0.15, step=0.01
        )
        monthly_charging_cost = st.number_input(
            "Monthly Charging Cost ($)", min_value=0.0, value=50.0
        )
        monthly_energy_consumption_kwh = st.number_input(
            "Monthly Energy Consumption (kWh)", min_value=0.0, value=300.0
        )
    st.subheader("Attitudes & Knowledge (0-10 scale)")
    col7, col8 = st.columns(2)
    with col7:
        environmental_awareness_score = st.slider(
            "Environmental Awareness Score", 0.0, 10.0, 9.5
        )
        technology_affinity_score = st.slider(
            "Technology Affinity Score", 0.0, 10.0, 8.0
        )
        ev_knowledge_score = st.slider(
            "EV Knowledge Score", 0.0, 10.0, 7.0
        )
    with col8:
        range_anxiety_score = st.slider(
            "Range Anxiety Score", 0.0, 10.0, 6.5
        )
        battery_replacement_concern = st.slider(
            "Battery Replacement Concern", 0.0, 10.0, 5.0
        )
        government_incentive_awareness = st.slider(
            "Government Incentives Awareness", 0.0, 10.0, 7.5
        )
        previous_ev_experience = st.selectbox(
            "Previous EV Experience",[1, 0]
        )
        submitted = st.form_submit_button("Predict EV Adoption Likelihood")

if submitted:
    input_data = pd.DataFrame({
        "age": [age],
        "age_group": [age_group],
        "education_level": [education_level],
        "annual_income": [annual_income],
        "annual_icome_brac": [annual_icome_brac],
        "city_type": [city_type],
        "current_vehicle_type": [current_vehicle_type],
        "vehicle_age_years": [vehicle_age_years],
        "daily_commute_km": [daily_commute_km],
        "weekly_travel_distance_km": [weekly_travel_distance_km],
        "commute_categories": [commute_categories],
        "fuel_expense_per_month": [fuel_expense_per_month],
        "charging_station_accessibility": [charging_station_accessibility],
        "nearest_charging_station_km": [nearest_charging_station_km],
        "home_charging_available": [home_charging_available],
        "electricity_cost_per_kwh": [electricity_cost_per_kwh],
        "monthly_charging_cost": [monthly_charging_cost],
        "monthly_energy_consumption_kwh": [monthly_energy_consumption_kwh],
        "environmental_awareness_score": [environmental_awareness_score],
        "technology_affinity_score": [technology_affinity_score],
        "ev_knowledge_score": [ev_knowledge_score],
        "range_anxiety_score": [range_anxiety_score],
        "battery_replacement_concern": [battery_replacement_concern],
        "government_incentive_awareness": [government_incentive_awareness],
        "previous_ev_experience":[previous_ev_experience]
    })

    prediction = model.predict(input_data)[0]
    prediction_proba = model.predict_proba(input_data)

    class_labels = model.classes_

    st.subheader("📊 Prediction Result")
    st.success(f"**Predicted EV Adoption Likelihood: {prediction}**")

    prob_df = pd.DataFrame({

        "Likelihood Class": class_labels,
        "Probability": prediction_proba[0]
    }).set_index("Likelihood Class")
    st.bar_chart(prob_df)

    st.write("Prediction Probabilities:")
    st.write(pd.DataFrame(prediction_proba, columns=model.classes_))