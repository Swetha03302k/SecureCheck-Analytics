import pandas as pd
from sqlalchemy import text
from Python.db_connection import engine


def predict_violation(speeding, drugs_related, search_conducted):

    if drugs_related:
        return "Drug Related"

    elif speeding:
        return "Speeding"

    elif search_conducted:
        return "Equipment"

    else:
        return "Moving Violation"


def predict_stop_outcome(search_conducted, drugs_related):

    if drugs_related:
        return "Arrest Driver"

    elif search_conducted:
        return "Citation"

    else:
        return "Warning"


def save_record(data):

    query = text("""
        INSERT INTO traffic_stops
        (
            stop_date,
            stop_time,
            country_name,
            driver_gender,
            driver_age,
            driver_race,
            violation,
            search_conducted,
            search_type,
            stop_outcome,
            is_arrested,
            stop_duration,
            drugs_related_stop,
            vehicle_number
        )
        VALUES
        (
            :stop_date,
            :stop_time,
            :country_name,
            :driver_gender,
            :driver_age,
            :driver_race,
            :violation,
            :search_conducted,
            :search_type,
            :stop_outcome,
            :is_arrested,
            :stop_duration,
            :drugs_related_stop,
            :vehicle_number
        )
    """)

    with engine.begin() as conn:
        conn.execute(query, data)

