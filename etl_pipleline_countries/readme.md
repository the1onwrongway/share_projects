# 🌍 Country Data ETL Pipeline (Python + PostgreSQL)

This project is a complete ETL pipeline written in Python. It extracts real-time country data from the [REST Countries API](https://restcountries.com), transforms it, and loads it into a PostgreSQL database — with logging, modular structure, and scheduling.

---

## 🔄 ETL Workflow

- **Extract**  
  Pulls country data from the REST API using the `requests` library.

- **Transform**  
  Cleans and structures the data to select only the fields needed: official name, region, and population.

- **Load**  
  Inserts the cleaned data into a PostgreSQL table using `psycopg2`, with conflict handling for duplicate rows.

- **Schedule**  
  Uses Python’s `schedule` module to run the ETL job automatically on a defined interval.

- **Logging**  
  Logs all steps and errors to `pipeline.log` for traceability.

---

## 🛠️ Tech Stack

- Python 3.x  
- PostgreSQL  
- requests  
- psycopg2-binary  
- schedule  
- logging

---

## 📁 Project Structure

```text
etl_project/
├── etl.py             # Main controller script
├── extract.py         # Extracts data from the API
├── transform.py       # Transforms raw JSON into structured rows
├── load.py            # Loads rows into PostgreSQL
├── config.py          # DB and API configuration
├── test_transform.py  # Unit tests for transform logic
├── pipeline.log       # Log file generated during runs
```
---

## 🧪 Database Schema

Before running the pipeline, create this table in your PostgreSQL database:

```sql
CREATE TABLE countries (
    name TEXT PRIMARY KEY,
    region TEXT,
    population BIGINT
);
```
---

## ▶️ How to Run the Pipeline

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/etl_project.git
   cd etl_project
   ```
2.	Install required libraries:
   ```bash
  pip install -r requirements.txt
  ```
3.	Edit config.py and set your database credentials.
4.	Run the ETL script:
  ```bash
  python etl.py
  ```
---
## 🙌 About This Project

This project was part of my journey into data engineering. I built it to understand how to structure real-world ETL pipelines using Python and PostgreSQL — focusing on clean modular code, automation, and logging.

Feel free to fork, learn from it, or reach out if you’re working on something similar!
## ✅ Example Row in the Table
"Republic of India" | "Asia" | 1400000000
