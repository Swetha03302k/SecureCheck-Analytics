import plotly.express as px

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

    fig.update_traces(textposition="outside")

    return fig