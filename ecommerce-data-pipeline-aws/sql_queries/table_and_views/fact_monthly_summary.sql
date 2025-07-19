CREATE OR REPLACE VIEW ecommerce_analytics.fact_monthly_summary AS
SELECT
  year(t.event_time)   AS year,
  month(t.event_time)  AS month,
  COUNT(*)             AS n_purchases,
  ROUND(SUM(t.price), 2) AS total_revenue,
  COUNT(DISTINCT t.user_id) AS unique_users,
  ROUND(SUM(t.price) / COUNT(DISTINCT t.user_id), 2) AS avg_order_value
FROM ecommerce_analytics.fact_purchases t
GROUP BY year(t.event_time), month(t.event_time)
ORDER BY year, month;