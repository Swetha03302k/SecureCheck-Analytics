import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About SecureCheck")

st.write(
    """
    SecureCheck is a Police Check Post Management System developed to
    help law enforcement agencies efficiently manage, analyze, and
    predict traffic stop records.
    """
)

st.markdown("---")

st.header("🎯 Project Objectives")

st.markdown("""
- Digitize police traffic stop records.
- Store stop details securely in MySQL.
- Perform business analysis using SQL.
- Visualize traffic stop patterns.
- Predict traffic violations and stop outcomes.
- Improve decision making using interactive dashboards.
""")

st.markdown("---")

st.header("🚀 Key Features")

st.markdown("""
✅ Interactive Dashboard

✅ KPI Cards

✅ Vehicle Search

✅ Dynamic Filters

✅ Business Insights using SQL

✅ Interactive Charts

✅ Prediction Analysis

✅ MySQL Database Integration

✅ Download Filtered Records
""")

st.markdown("---")

st.header("🛠 Technologies Used")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
### Programming

- Python
- SQL

### Database

- MySQL

### Dashboard

- Streamlit
- Plotly
""")

with col2:

    st.markdown("""
### Libraries

- Pandas
- SQLAlchemy
- PyMySQL

### Development

- VS Code
- Git
- GitHub
""")

st.markdown("---")

st.header("📂 Dataset Information")

st.markdown("""
The project uses a traffic stop dataset containing information such as:

- Stop Date
- Stop Time
- Country
- Driver Gender
- Driver Age
- Driver Race
- Violation
- Search Conducted
- Search Type
- Stop Outcome
- Arrest Status
- Stop Duration
- Drug Related Stop
- Vehicle Number
""")

st.markdown("---")

st.header("📊 Project Workflow")

st.markdown("""
1. Data Cleaning using Python

2. Store Cleaned Data in MySQL

3. Perform SQL Analysis

4. Build Interactive Dashboard

5. Generate Business Insights

6. Predict Violation & Stop Outcome

7. Save New Police Logs
""")

st.markdown("---")

st.header("👩‍💻 Developer")

st.markdown("""
**Project:** SecureCheck – Police Check Post Management System

**Developed By:** Swetha K


**Tools Used:** Python, SQL, Streamlit, Plotly, MySQL
""")

st.markdown("---")

st.success("SecureCheck helps police departments manage traffic stop records efficiently through data analytics and predictive insights.")