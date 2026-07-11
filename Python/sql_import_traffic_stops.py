import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# Read the CSV file
df = pd.read_csv(r"Data\traffic_stops_cleaned.csv")

# Create MySQL connection
connection_url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="SweRuk@1530",   # Replace with your MySQL password
    host="localhost",
    port=3306,
    database="securecheck"
)

engine = create_engine(connection_url)

try:
    # Import data into MySQL
    df.to_sql(
        name="traffic_stops",
        con=engine,
        if_exists="append",      # Appends to the existing table
        index=False,
        chunksize=1000
    )

    print("Data imported successfully!")

except Exception as e:
    print("\nImport Failed!")
    print(e)