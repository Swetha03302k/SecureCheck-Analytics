import pandas as pd
from db_connection import engine

query = """
SELECT *
FROM traffic_stops
LIMIT 10;
"""

df = pd.read_sql(query, engine)

print(df)
