import plotly.express as px
import pandas as pd

def violation_chart(df):

    violation_counts = (
        df["violation"]
        .value_counts()
        .reset_index()
    )

    violation_counts.columns = ["violation", "count"]

    fig = px.bar(
        violation_counts,
        x="violation",
        y="count",
        text="count",
        title="Violation Distribution"
    )

    fig.update_traces(
        textposition="outside"
    )

    return fig

def gender_chart(df):

    fig = px.pie(
        df,
        names="driver_gender",
        title="Driver Gender Distribution"
    )

    fig.update_traces(
        textinfo="percent+label"
    )

    return fig

def traffic_trend_chart(df):

    temp_df = df.copy()

    temp_df["stop_date"] = pd.to_datetime(temp_df["stop_date"])

    temp_df["Month"] = (
        temp_df["stop_date"]
        .dt.to_period("M")
        .astype(str)
    )

    monthly = (
        temp_df.groupby("Month")
        .size()
        .reset_index(name="Stops")
    )

    fig = px.line(
        monthly,
        x="Month",
        y="Stops",
        markers=True,
        title="Traffic Stops Over Time"
    )

    return fig

def country_chart(df):

    country_counts = (
        df.groupby("country_name")
        .size()
        .reset_index(name="Stops")
    )

    fig = px.bar(
        country_counts,
        x="country_name",
        y="Stops",
        text="Stops",
        title="Traffic Stops by Country"
    )

    fig.update_traces(
        textposition="outside"
    )

    return fig

def arrest_chart(df):

    arrest_counts = (
        df[df["is_arrested"] == 1]
        .groupby("violation")
        .size()
        .reset_index(name="Arrests")
    )

    fig = px.bar(
        arrest_counts,
        x="violation",
        y="Arrests",
        text="Arrests",
        title="Arrests by Violation"
    )

    fig.update_traces(
        textposition="outside"
    )

    return fig

def search_chart(df):

    search_counts = (
        df[df["search_conducted"] == 1]
        .groupby("violation")
        .size()
        .reset_index(name="Searches")
    )

    fig = px.bar(
        search_counts,
        x="violation",
        y="Searches",
        text="Searches",
        title="Searches by Violation"
    )

    fig.update_traces(
        textposition="outside"
    )

    return fig


