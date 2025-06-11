import psycopg2
import logging
from config import DB_CONFIG

def load(data):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        for row in data:
            try:
                cursor.execute("""
                    INSERT INTO countries (name, region, population)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (name) DO NOTHING
                """, row)
                logging.info(f"Row inserted: {row}")
            except Exception as e:
                logging.error(f"Row failed: {row} | {e}")
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        logging.error(f"Database connection failed: {e}")