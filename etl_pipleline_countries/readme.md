# 🌍 Country Data ETL Pipeline (Python + PostgreSQL)

This project is a complete, modular ETL pipeline built in Python. It extracts real-time country data from the [REST Countries API](https://restcountries.com), transforms the data, and loads it into a PostgreSQL database.

---

## 🔄 ETL Workflow

- **Extract:**  
  Connects to the REST Countries API and retrieves fields like official name, region, and population.

- **Transform:**  
  Cleans and formats raw data by:
  - Selecting required fields
  - Handling edge cases or missing values
  - Structuring it for database loading

- **Load:**  
  Inserts transformed rows into a PostgreSQL table (`countries`) using `psycopg2`, with conflict handling to avoid duplicates.

- **Schedule:**  
  Uses Python’s `schedule` module to run the ETL automatically at defined intervals.

- **Logging:**  
  All actions and errors are logged to a file (`pipeline.log`) for traceability.

---

## 🛠️ Tech Stack

- **Language:** Python 3  
- **Database:** PostgreSQL  
- **Libraries:**  
  - `requests` – for API calls  
  - `psycopg2-binary` – for PostgreSQL connection  
  - `schedule` – for recurring tasks  
  - `logging` – for pipeline monitoring

---

## 📁 Project Structure
