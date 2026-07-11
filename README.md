# SecureCheck-Analytics

# 🚔 SecureCheck - Police Check Post Management System

SecureCheck is a Police Check Post Management System built using **Python, Streamlit, MySQL, SQL, and Plotly**. The application helps law enforcement agencies manage traffic stop records, perform business analysis, visualize trends, and predict traffic violations and stop outcomes.

---

## 📌 Project Overview

SecureCheck digitizes police traffic stop records and provides an interactive dashboard for monitoring traffic activities. It combines data analytics, SQL querying, and predictive logic to assist officers in making data-driven decisions.

---

## ✨ Features

### 📊 Dashboard
- Interactive KPI Cards
- Vehicle Number Search
- Country Filter
- Driver Gender Filter
- Violation Filter
- Download Filtered Records (CSV)
- Interactive Plotly Charts

### 📈 Advanced Insights
Business questions answered using SQL:
- Top Violations
- Arrests by Country
- Searches by Violation
- Drug Related Stops
- Average Driver Age by Country
- Stop Outcome Distribution
- Driver Gender Distribution
- Traffic Stops by Country

### 🤖 Prediction Analysis
- Predict Traffic Violation
- Predict Stop Outcome
- Save New Police Log to MySQL
- Prediction Summary
- Police Log Summary

### 🗄 Database
- MySQL Integration
- SQL Queries
- Automatic Record Storage

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Data Processing |
| Streamlit | Web Application |
| MySQL | Database |
| SQL | Business Queries |
| Pandas | Data Analysis |
| Plotly | Interactive Charts |
| SQLAlchemy | Database Connection |

---

# 📂 Project Structure

```
SecureCheck-Police-Check-Post-Management-System
│
├── Dashboard
│   ├── helpers
│   │   ├── charts.py
│   │   ├── prediction.py
│   │   └── __init__.py
│   │
│   ├── pages
│   │   ├── 1_Advanced_Insights.py
│   │   ├── 2_Prediction.py
│   │   └── 3_About.py
│   │
│   └── SecureCheck_Dashboard.py
│
├── Data
│   ├── traffic_stops.xlsx
│   └── traffic_stops_cleaned.csv
│
├── Python
│   ├── cleaning.py
│   ├── analysis.py
│   ├── eda.py
│   ├── db_connection.py
│   └── sql_import_traffic_stops.py
│
├── SQL
│   └── queries.sql
│
├── requirements.txt
├── README.md
└── .gitignore
```





Create the database

```sql
CREATE DATABASE securecheck;
```

Import the dataset into MySQL using

```
Python/sql_import_traffic_stops.py
```

or execute the SQL scripts provided in

```
SQL/queries.sql
```

---

# 📊 Dashboard Preview

The application provides:

- KPI Cards
- Traffic Analysis Dashboard
- Interactive Charts
- Vehicle Search
- Downloadable Reports

---

# 📈 Advanced Insights

The application answers important business questions including:

- Which violations occur most frequently?
- Which country has the highest arrests?
- Which violations require searches?
- Drug-related stop analysis
- Average driver age by country
- Driver gender distribution
- Stop outcome distribution
- Traffic stops by country

---

# 🤖 Prediction Module

The Prediction page allows users to:

- Enter police stop details
- Predict likely violation
- Predict stop outcome
- Generate a prediction summary
- Save the police log directly into MySQL

---

# 📚 Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis (EDA)
- SQL Querying
- Database Design
- Streamlit Dashboard Development
- Data Visualization
- Python Programming
- MySQL Integration
- Interactive Dashboard Design
- Business Intelligence
- Predictive Logic

---

# 📌 Future Enhancements

- Machine Learning-based Prediction
- User Authentication
- Police Officer Login
- PDF Report Generation
- Live Dashboard Refresh
- Geographic Traffic Heat Maps
- Cloud Deployment

---

# 👩‍💻 Developed By

**Swetha K**

### Technologies

Python • SQL • MySQL • Streamlit • Plotly • Pandas

---

# ⭐ If you found this project useful, consider giving it a star!
