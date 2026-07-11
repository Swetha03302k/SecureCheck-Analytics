import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from helpers.prediction import (
    predict_violation,
    predict_stop_outcome,
    save_record
)

st.set_page_config(
    page_title="Prediction",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Prediction Analysis")

st.write(
    "Enter police stop details to predict the violation and stop outcome."
)

st.markdown("---")

with st.form("prediction_form"):

    stop_date = st.date_input("Stop Date")

    stop_time = st.time_input("Stop Time")

    country = st.selectbox(
        "Country",
        ["USA", "Canada", "India"]
    )

    driver_gender = st.selectbox(
        "Driver Gender",
        ["Male", "Female"]
    )

    driver_age = st.number_input(
        "Driver Age",
        min_value=16,
        max_value=100,
        value=25
    )

    driver_race = st.selectbox(
        "Driver Race",
        ["Asian", "Black", "White", "Hispanic", "Other"]
    )

    search_conducted = st.selectbox(
        "Search Conducted",
        ["Yes", "No"]
    )

    search_type = st.selectbox(
        "Search Type",
        ["None", "Vehicle Search", "Frisk"]
    )

    stop_duration = st.selectbox(
        "Stop Duration",
        ["0-15 Min", "16-30 Min", "30+ Min"]
    )

    drugs_related = st.selectbox(
        "Drug Related Stop",
        ["Yes", "No"]
    )

    vehicle_number = st.text_input(
        "Vehicle Number"
    )

    submit = st.form_submit_button("Predict Stop Outcome and Violation")
  
    
if submit:

    # Convert Yes/No to Boolean
    search_bool = (search_conducted == "Yes")
    drugs_bool = (drugs_related == "Yes")

    # Validate Vehicle Number
    if vehicle_number.strip():
        display_vehicle = vehicle_number
    else:
        display_vehicle = "***"

    # Simple rule to determine speeding
    speeding = (search_type == "Vehicle Search")

    # Predict values
    violation = predict_violation(
        speeding,
        drugs_bool,
        search_bool
    )

    outcome = predict_stop_outcome(
        search_bool,
        drugs_bool
    )

    st.success("✅ Prediction Completed Successfully!")

    st.markdown("---")

    st.subheader("🚓 Prediction Summary")

    st.markdown(f"""
- **Predicted Violation:** **{violation}**
- **Predicted Stop Outcome:** **{outcome}**
""")

    with st.container(border=True):

        search_text = (
            "A search was conducted"
            if search_conducted == "Yes"
            else "No search was conducted"
        )

        drug_text = (
            "the stop was drug-related."
            if drugs_related == "Yes"
            else "the stop was not drug-related."
        )

        st.markdown(f"""
📝 A **{driver_age}-year-old {driver_gender.lower()}** driver was stopped at **{stop_time.strftime('%I:%M %p')}** on **{stop_date}**.

{search_text}, and {drug_text}

**Stop Duration:** {stop_duration}  
**Vehicle Number:** {display_vehicle}
""")

    # Save Record to MySQL
    record = {
        "stop_date": stop_date,
        "stop_time": stop_time,
        "country_name": country,
        "driver_gender": driver_gender,
        "driver_age": driver_age,
        "driver_race": driver_race,
        "violation": violation,
        "search_conducted": search_bool,
        "search_type": search_type,
        "stop_outcome": outcome,
        "is_arrested": outcome == "Arrest Driver",
        "stop_duration": stop_duration,
        "drugs_related_stop": drugs_bool,
        "vehicle_number": vehicle_number
    }

    save_record(record)

    st.success("✅ Police log saved successfully to MySQL.")