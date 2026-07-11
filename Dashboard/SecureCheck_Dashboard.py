import streamlit as st
import pandas as pd
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))


from Python.db_connection import engine
from helpers.charts import (
    violation_chart,
    gender_chart,
    traffic_trend_chart,
    country_chart,
    arrest_chart,
    search_chart
)

st.set_page_config(
    page_title="SecureCheck Dashboard",
    page_icon="🚔",
    layout="wide"
)

st.title("🚔 SecureCheck Dashboard")
st.write("Welcome to the Police Check Post Management System")

@st.cache_data(show_spinner="Loading data...")
def load_data():
    query = "SELECT * FROM traffic_stops"
    return pd.read_sql(query, engine)

df = load_data()
 
#Filtering options in the sidebar
st.sidebar.title("🚔 SecureCheck")

st.sidebar.markdown("---")

st.sidebar.subheader("Filters")

country = st.sidebar.multiselect(
    "Country",
    options=sorted(df["country_name"].unique()),
    default=sorted(df["country_name"].unique())
)

gender = st.sidebar.multiselect(
    "Driver Gender",
    options=sorted(df["driver_gender"].unique()),
    default=sorted(df["driver_gender"].unique())
)

violation = st.sidebar.multiselect(
    "Violation",
    options=sorted(df["violation"].unique()),
    default=sorted(df["violation"].unique())
)

filtered_df = df[
    (df["country_name"].isin(country)) &
    (df["driver_gender"].isin(gender)) &
    (df["violation"].isin(violation))
]
if filtered_df.empty:
    st.warning("No records found for the selected filters.")
    st.stop()

# Search functionality for vehicle number
vehicle = st.sidebar.text_input("🔍 Search Vehicle Number")

if vehicle:
    search_df = filtered_df[
        filtered_df["vehicle_number"].str.contains(
            vehicle,
            case=False,
            na=False
        )
    ]

    if search_df.empty:
        st.warning("⚠️ No matching vehicle found.")
    else:
        st.subheader("🚗 Vehicle Search Result")
        st.dataframe(search_df)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Stops", len(filtered_df))
col2.metric("Arrests", filtered_df["is_arrested"].sum())
col3.metric("Searches", filtered_df["search_conducted"].sum())
col4.metric("Average Driver Age", round(filtered_df["driver_age"].mean(), 1))

st.markdown("---")
st.subheader("📈 Business Intelligence Dashboard")

# Chart Selector
chart_option = st.selectbox(
    "Choose Analysis",
    [
        "Violation Distribution",
        "Driver Gender Distribution",
        "Traffic Stops Over Time",
        "Traffic Stops by Country",
        "Arrests by Violation",
        "Searches by Violation",
    ]
)



fig_bar = violation_chart(filtered_df)

fig_pie = gender_chart(filtered_df)

fig_line = traffic_trend_chart(filtered_df)

fig_country = country_chart(filtered_df)

fig_arrest = arrest_chart(filtered_df)

fig_search = search_chart(filtered_df)

# Display Selected Chart

if chart_option == "Violation Distribution":

    st.plotly_chart(
        fig_bar,
        width="stretch",
        key="violation_chart"
    )

elif chart_option == "Driver Gender Distribution":

    st.plotly_chart(
        fig_pie,
        width="stretch",
        key="gender_chart"
    )

elif chart_option == "Traffic Stops Over Time":

    st.plotly_chart(
        fig_line,
        width="stretch",
        key="trend_chart"
    )

elif chart_option == "Traffic Stops by Country":

    st.plotly_chart(
        fig_country,
        width="stretch",
        key="country_chart"
    )

elif chart_option == "Arrests by Violation":

    st.plotly_chart(
        fig_arrest,
        width="stretch",
        key="arrest_chart"
    )

elif chart_option == "Searches by Violation":

    st.plotly_chart(
        fig_search,
        width="stretch",
        key="search_chart"
    )

st.markdown("---")
st.subheader("📋 Traffic Stop Records")

st.dataframe(
    filtered_df,
    width="stretch",
    hide_index=True
)

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download CSV",
    csv,
    "traffic_stops.csv",
    "text/csv"
)

from datetime import datetime

st.caption(f"Last Updated: {datetime.now():%d-%m-%Y %H:%M:%S}")


