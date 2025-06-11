# 🌍 Country Data ETL Pipeline (Python + PostgreSQL)

This project is a simple, production-style ETL pipeline built with Python that extracts real-time country data from the [REST Countries API](https://restcountries.com), transforms it, and loads it into a PostgreSQL database.

---

## 🔄 ETL Workflow

- **Extract**  
  Retrieves country-level data (name, region, population) from the public REST API.

- **Transform**  
  Cleans and formats the raw JSON data:
  - Selects key fields (`official name`, `region`, `population`)
  - Handles missing values

- **Load**  
  Inserts the cleaned data into a PostgreSQL table (`countries`) using `psycopg2`.

- **Schedule**  
  Uses Python's `schedule` module to run the ETL job on a timed interval (e.g. hourly).

- **Logging**  
  Logs all key actions and errors to `pipeline.log`.

---

## 🛠️ Tech Stack

- Python 3.x  
- PostgreSQL  
- `requests` (for API calls)  
- `psycopg2-binary` (for DB connection)  
- `schedule` (for job scheduling)  
- `logging` (for pipeline visibility)

---

## 📂 Project Structure
