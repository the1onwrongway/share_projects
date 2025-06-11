import logging
from extract import extract_data
from transform import transform
from load import load
import schedule
import time

logging.basicConfig(filename='pipeline.log', level=logging.INFO)
logging.info("ETL started")

data = extract_data()
rows = transform(data)
load(rows)

logging.info("ETL finished ✅")

def run():
    data = extract_data()
    rows = transform(data)
    load(rows)

schedule.every().day.do(run)

while True:
    schedule.run_pending()
    time.sleep(60)