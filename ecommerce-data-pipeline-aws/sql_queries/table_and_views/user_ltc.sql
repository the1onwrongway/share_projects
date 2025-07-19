CREATE OR REPLACE VIEW ecommerce_analytics.user_ltv AS
SELECT
  user_id,
  SUM(price) AS user_ltv,
  CASE
    WHEN SUM(price) < 100 THEN 'Low'
    WHEN SUM(price) BETWEEN 100 AND 499.99 THEN 'Mid'
    WHEN SUM(price) BETWEEN 500 AND 999.99 THEN 'High'
    ELSE 'Premium'
  END AS ltv_segment
FROM
  ecommerce_analytics.fact_purchases
GROUP BY
  user_id;
  
  select * from user_ltv limit 5