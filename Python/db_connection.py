from sqlalchemy import create_engine
from sqlalchemy.engine import URL

connection_url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="SweRuk@1530",      # <-- your actual password
    host="localhost",
    port=3306,
    database="securecheck"
)

engine = create_engine(connection_url)