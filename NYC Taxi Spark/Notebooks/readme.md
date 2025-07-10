# 🗽 NYC Taxi Data Engineering Project with Spark + Delta + Databricks

## 🚀 Overview

This project demonstrates a complete **batch data engineering pipeline** using Apache Spark on Databricks, working with real-world NYC Yellow Taxi data. The pipeline includes **data ingestion, cleaning, enrichment, transformation**, and **visualization**, all powered by **Delta Lake and Databricks SQL**.

> ✅ Currently Completed: Week 1 & Week 2  
> 🔜 Next: Automating with AWS & Databricks Jobs (Week 3–4)
---

## 🧱 Stack Used

- **Apache Spark** (PySpark)
- **Databricks (Community Edition)**
- **Delta Lake** format
- **Databricks SQL**
- (Upcoming) **AWS S3**, **Databricks Jobs**

---

## 📦 Dataset

- **Yellow Taxi Trip Data (May 2025)**:  
  Parquet format loaded from Databricks volume  
  Contains timestamped pickup/dropoff data, fares, tips, locations.

- **NYC TLC Zone Lookup Table**:  
  `/databricks-datasets/nyctaxi/taxizone/taxi_zone_lookup.csv`

---

## 🧪 Week 1: Core Pipeline (Ingestion → Clean → Enrich → Aggregate)

### ✅ Steps Done:
1. **Loaded Parquet data** into Spark DataFrame.
2. **Filtered out nulls/invalid records** (e.g., zero trip distance or negative fares).
3. Performed **Feature Engineering**:
   - `pickup_hour` → hour of day (for hourly analysis)
   - `pickup_dayofweek` → weekday/weekend trends
   - `trip_duration_minutes` → duration in minutes
   - `tip_percent` → (tip / fare) × 100
4. **Aggregated** hourly fare & tip percentages.

### 💾 Tables Saved to Delta Lake (Unity Catalog):
- `nyc_taxi.cleaned_data` → trip-level enriched data (silver table)
- `nyc_taxi.hourly_summary` → hourly aggregates (gold table)

---

## 📊 Week 2: SQL Querying + Visualizations

### 🔍 Analysis Performed (Databricks SQL):
- **Hourly Tip Percent**:
  ```sql
  SELECT pickup_hour, ROUND(AVG(tip_percent), 2) AS avg_tip_percent
  FROM nyc_taxi.hourly_summary
  GROUP BY pickup_hour
  ORDER BY pickup_hour;
  ```

- **Top Pickup Zones (joined with TLC metadata)**:
  ```sql
  SELECT z.Zone AS pickup_zone, COUNT(*) AS trips
  FROM nyc_taxi.cleaned_data AS t
  JOIN nyc_taxi_zone_lookup AS z ON t.PULocationID = z.LocationID
  GROUP BY z.Zone
  ORDER BY trips DESC
  LIMIT 10;
  ```

### 📈 Dashboard Created:
>  ✅ [**Live Databricks Dashboard →** View Here](https://dbc-b9df4b41-3fc1.cloud.databricks.com/dashboardsv3/01f05d58d53b16a493bcb79f5a2bbe8d/published?o=3150088754748561)
> - Hourly tipping behaviour
> - Top 10 pickup zones by trip count

---

## 📌 To-Do (Upcoming)

### Week 3 – Cloud Foundations (AWS)
- Learn IAM basics, access keys, and bucket permissions
- Create an S3 bucket
- Connect Databricks to S3 using `spark.conf.set(...)` and `s3a://` path

### Week 4 – Automate & Polish
- Automate pipeline using **Databricks Jobs**
- Schedule daily ingestion
- Push notebook to GitHub
- Add README.md (this file)
- Final resume line for job applications

---

## 💼 Resume Line (Preview)

> Built an end-to-end data pipeline using Spark + Delta on Databricks, processed NYC Taxi data, built SQL dashboards, and automated ingestion workflows (planned via AWS S3 & Jobs API).

---

## 🙌 Credits

- Dataset from NYC TLC Open Data  
- Databricks Community Datasets

---