import streamlit as st
import pandas as pd
import plotly.express as px
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from Python.db_connection import engine

st.set_page_config(
    page_title="Advanced Insights",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Advanced Insights")

st.write(
    "Answer business questions using SQL queries and interactive visualizations."
)

@st.cache_data
def load_data():
    query = "SELECT * FROM traffic_stops"
    return pd.read_sql(query, engine)

df = load_data()

st.markdown("---")

st.subheader("📌 Business Questions")

question = st.selectbox(
    "Select Business Question",
    [
        "Top 10 Most Frequent Violations",
        "Arrests by Country",
        "Searches by Violation",
        "Drugs Related Stops",
        "Average Driver Age by Country",
        "Stop Outcome Distribution",
        "Driver Gender Distribution",
        "Traffic Stops by Country"
    ]
)
st.success(f"Showing results for: {question}")
if question == "Top 10 Most Frequent Violations":

    query = """
        SELECT
            violation,
            COUNT(*) AS Total_Stops
        FROM traffic_stops
        GROUP BY violation
        ORDER BY Total_Stops DESC;
    """

    result = pd.read_sql(query, engine)

    st.subheader("Top Violations")

    st.dataframe(
        result,
        width="stretch",
        hide_index=True
    )

    fig = px.bar(
        result,
        x="violation",
        y="Total_Stops",
        text="Total_Stops",
        title="Top Violations"
    )

    fig.update_traces(textposition="outside")

    st.plotly_chart(
        fig,
        width="stretch"
    )
    st.markdown("---")

elif question == "Arrests by Country":

    query = """
    SELECT
        country_name,
        SUM(is_arrested) AS Total_Arrests
    FROM traffic_stops
    GROUP BY country_name
    ORDER BY Total_Arrests DESC;
    """

    result = pd.read_sql(query, engine)

    st.subheader("Arrests by Country")

    st.dataframe(
        result,
        width="stretch",
        hide_index=True
    )

    fig = px.bar(
        result,
        x="country_name",
        y="Total_Arrests",
        text="Total_Arrests",
        title="Arrests by Country"
    )

    fig.update_traces(textposition="outside")

    st.plotly_chart(fig, width="stretch")

    st.markdown("---")

elif question == "Searches by Violation":

    query = """
    SELECT
        violation,
        SUM(search_conducted) AS Searches
    FROM traffic_stops
    GROUP BY violation
    ORDER BY Searches DESC;
    """

    result = pd.read_sql(query, engine)

    st.subheader("Searches by Violation")

    st.dataframe(
        result,
        width="stretch",
        hide_index=True
    )

    fig = px.bar(
        result,
        x="violation",
        y="Searches",
        text="Searches",
        title="Searches by Violation"
    )

    fig.update_traces(textposition="outside")

    st.plotly_chart(fig, width="stretch")  

    st.markdown("---")

elif question == "Drugs Related Stops":

    query = """
    SELECT
        drugs_related_stop,
        COUNT(*) AS Total
    FROM traffic_stops
    GROUP BY drugs_related_stop;
    """

    result = pd.read_sql(query, engine)

    st.subheader("Drugs Related Stops")

    st.dataframe(
        result,
        width="stretch",
        hide_index=True
    )

    fig = px.pie(
        result,
        names="drugs_related_stop",
        values="Total",
        title="Drugs Related Stops"
    )

    st.plotly_chart(fig, width="stretch") 

    st.markdown("---")

elif question == "Average Driver Age by Country":

    query = """
    SELECT
        country_name,
        ROUND(AVG(driver_age),1) AS Average_Age
    FROM traffic_stops
    GROUP BY country_name;
    """

    result = pd.read_sql(query, engine)

    st.subheader("Average Driver Age by Country")

    st.dataframe(
        result,
        width="stretch",
        hide_index=True
    )

    fig = px.bar(
        result,
        x="country_name",
        y="Average_Age",
        text="Average_Age",
        title="Average Driver Age"
    )

    fig.update_traces(textposition="outside")

    st.plotly_chart(fig, width="stretch")

    st.markdown("---")

elif question == "Stop Outcome Distribution":

    query = """
    SELECT
        stop_outcome,
        COUNT(*) AS Total
    FROM traffic_stops
    GROUP BY stop_outcome;
    """

    result = pd.read_sql(query, engine)

    st.subheader("Stop Outcome Distribution")

    st.dataframe(
        result,
        width="stretch",
        hide_index=True
    )

    fig = px.pie(
        result,
        names="stop_outcome",
        values="Total",
        title="Stop Outcome Distribution"
    )

    st.plotly_chart(fig, width="stretch")

    st.markdown("---")

elif question == "Driver Gender Distribution":

    query = """
    SELECT
        driver_gender,
        COUNT(*) AS Total
    FROM traffic_stops
    GROUP BY driver_gender;
    """

    result = pd.read_sql(query, engine)

    st.subheader("Driver Gender Distribution")

    st.dataframe(
        result,
        width="stretch",
        hide_index=True
    )

    fig = px.pie(
        result,
        names="driver_gender",
        values="Total",
        title="Driver Gender Distribution"
    )

    st.plotly_chart(fig, width="stretch")

    st.markdown("---")

elif question == "Traffic Stops by Country":

    query = """
    SELECT
        country_name,
        COUNT(*) AS Stops
    FROM traffic_stops
    GROUP BY country_name
    ORDER BY Stops DESC;
    """

    result = pd.read_sql(query, engine)

    st.subheader("Traffic Stops by Country")

    st.dataframe(
        result,
        width="stretch",
        hide_index=True
    )

    fig = px.bar(
        result,
        x="country_name",
        y="Stops",
        text="Stops",
        title="Traffic Stops by Country"
    )

    fig.update_traces(textposition="outside")

    st.plotly_chart(fig, width="stretch")

    st.markdown("---")
