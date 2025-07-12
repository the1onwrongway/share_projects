# 🗽 NYC Taxi Lakehouse Project – Spark + Delta on Databricks

A complete **batch data-engineering pipeline** that ingests, cleans, enriches and analyzes New-York-City yellow-taxi trips.  
Built on **Apache Spark** in Databricks and stored in **Delta Lake**.  
🚩 Phase 1 (Databricks-only) is finished and published – AWS integration coming next.

---

## 📂 Project Structure
| File / Notebook | Purpose |
|-----------------|---------|
| **`01_pipeline_etl.ipynb`** | Load Parquet → clean → feature-engineer → aggregate → save Delta tables |
| **`02_sql_dashboard.ipynb`** | SQL queries, joins with zone lookup, builds visualizations & dashboard |

---

## ⚡ Quick Start
1. Clone or import both notebooks into any Databricks workspace (Community Edition works).
2. Attach to a cluster (DBR 13+).
3. Run `01_pipeline_etl.ipynb` – it will create:
   - `nyc_taxi.cleaned_data`  (silver)
   - `nyc_taxi.hourly_summary` (gold)
4. Run `02_sql_dashboard.ipynb` to generate SQL visuals **or** view the live dashboard:

**🔗 Live dashboard:**  
<https://dbc-b9df4b41-3fc1.cloud.databricks.com/dashboardsv3/01f05d58d53b16a493bcb79f5a2bbe8d/published?o=3150088754748561>

---

## 🔧 Tech Stack
- **Apache Spark 3** (PySpark DataFrame API + SQL)
- **Delta Lake** for ACID tables
- **Databricks SQL** for visualization
- **Unity Catalog** (or Hive Metastore) for table storage
- *(Phase 2 planned)* **AWS S3** for raw & processed storage

---

## 📑 Pipeline Steps

| Stage | Details |
|-------|---------|
| **Ingest** | Read May 2025 Parquet file `yellow_tripdata_2025-05.parquet` |
| **Clean** | Drop trips with 0 distance/fare, null timestamps, passenger_count ≤ 0 |
| **Feature Engineering** | `pickup_hour`, `pickup_dayofweek`, `trip_duration_minutes`, `tip_percent` |
| **Aggregate** | Hour-level avg fare and avg tip % |
| **Persist** | Save cleaned and aggregated datasets to Delta tables |
| **Analyze** | SQL joins with TLC zone lookup → dashboards (tip % by hour, busiest pickup zones) |

---

## 📊 Key Visualizations
| Chart | Insight |
|-------|---------|
| **Avg Tip % by Hour** | Peak tipping between 1–2 a.m. and 8 p.m. |
| **Top 10 Pickup Zones** | JFK Airport, Times Sq/42 St, and Midtown dominate trip counts |

---

## ➕ Next Milestones
1. **AWS S3 integration** – move raw & enriched data to a bucket using secret scopes / IAM role.
2. **Databricks Jobs** – schedule daily ingestion.
3. **Performance tuning** – partition by pickup_month, cache heavy tables.
4. **Readme update** – document cloud version (“v2”).

---

## 💼 Project Highlights
> Built an end-to-end Lakehouse pipeline on Databricks (Spark + Delta) that cleans and aggregates 1.6 M NYC taxi trips, stores curated tables in Unity Catalog, and surfaces insights via live SQL dashboards.

---

## 🙌 Acknowledgements
NYC TLC Trip Records, Databricks public datasets.