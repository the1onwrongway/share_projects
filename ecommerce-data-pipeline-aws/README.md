# E-commerce Analytics Pipeline on AWS

This project showcases a complete end-to-end data pipeline and analytics solution using AWS services. It analyzes customer behavior and purchase patterns from a multi-category e-commerce platform and visualizes meaningful business KPIs using Amazon QuickSight.

---

## 🚀 Objective

To build a scalable and insightful data pipeline that:
- Ingests raw e-commerce clickstream data
- Cleans and transforms it using AWS Glue & Spark
- Stores curated datasets on S3 in a dimensional model
- Surfaces actionable insights using Amazon QuickSight dashboards

---

## 🛠️ Tools & Services Used

| Layer          | Technology                           |
|----------------|---------------------------------------|
| Data Storage   | Amazon S3                             |
| ETL            | AWS Glue, PySpark                     |
| Data Catalog   | AWS Glue Data Catalog                 |
| Query Engine   | Amazon Athena                         |
| Dashboarding   | Amazon QuickSight                     |
| Project Hosting| GitHub                                |

---

## 📦 Dataset Used

Dataset Source: [Kaggle - E-Commerce Behavior Data from Multi Category Store](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store)

- Records ~2.8 million purchase events after filtering.
- Fields include: `event_time`, `user_id`, `product_id`, `price`, `category_id`, `user_session`, etc.
- This dataset is **static** and will not be updated — hence, no incremental ingestion logic was implemented.

---

## 🧱 Data Architecture

The data pipeline follows a **Dimensional Model** consisting of:

- `fact_purchases`: Filtered and cleaned purchase data.
- `dim_user`: User attributes derived from sessions.
- `dim_product`: Product details.
- `dim_category`: Category mappings.
- `dim_time`: Enriched time dimension from event timestamps.
- `fact_monthly_summary`: Pre-aggregated monthly metrics.
- `user_ltv`: View that computes total revenue per user.

All datasets are registered in Glue Data Catalog and queried using Amazon Athena or directly consumed in QuickSight.

---

## 📊 Dashboard Overview

Built in **Amazon QuickSight**, this dashboard presents key business insights:

### 1️⃣ KPI Summary Row
- **Lifetime Revenue**: Total cumulative revenue across all purchases.
- **Average Customer LTV**: The average lifetime value per customer.
- **Total Customers**: Unique count of users who made a purchase.
- **Repeat Customers**: Count of customers with more than one purchase, indicating engagement and loyalty.

### 2️⃣ Revenue Trend Analysis
- **Month-over-Month (MoM) Revenue**: Visualizes revenue evolution by month to identify seasonality or marketing impact.
- **MoM Weekday-wise Revenue**: Highlights purchase patterns across weekdays for each month, revealing user behavior trends (e.g. weekend spikes).

### 3️⃣ Product-Level Insights
- **Top 5 Brands by Revenue**: Bar chart showcasing brands generating highest revenue.
- **Top 5 Categories by Revenue**: Helps identify category-wise performance and popular verticals.

### 4️⃣ Customer Segmentation
- **Donut Chart – LTV Segmentation**: Customers are bucketed into LTV tiers (e.g., Low, Medium, High, VIP) to support strategic marketing and retention decisions.

---

## 🧠 Key Learnings

- Implemented real-world dimensional modeling using AWS Glue & Spark.
- Learned hands-on data transformation and cleaning using PySpark in Glue jobs.
- Mastered Amazon QuickSight for dashboard creation, KPI tracking, and calculated fields.
- Gained experience with Glue crawlers, Data Catalog, and performance optimization on AWS Athena.

---

## 📸 Dashboard Preview

> PDF version of the dashboard is available [here](/https://github.com/the1onwrongway/share_projects/blob/main/ecommerce-data-pipeline-aws/Dashboard.pdf).

---

## 🧳 Future Improvements

- Incorporate user journey analysis if click/view/cart data becomes available.
- Implement session-based tracking and cohort analysis.
- Introduce incremental data pipelines and scheduling using AWS Glue Workflows (for dynamic datasets).

---

## 👋 Author

**Milan Gabriel**  
*Sr. Team Leader – Pricing & Tenders*  
_"And yes, I’m still naming my spreadsheets like Bond films. ‘No Margin for Error’ drops next week."_

---

## 📁 Folder Structure

```
ecommerce-data-pipeline-aws/
│
├── glue_jobs/                # PySpark Glue jobs
├── notebooks/                # EDA Notebooks
├── scripts/                  # Sample Data
├── sql/                      # Athena DDLs and transformations
├── Dashborad.pdf             # Dashboard PDF
├── requirements.txt          # Python Requirements List
└── README.md                 # This file
```

---

## 📝 License

This project is for learning and demonstration purposes only.