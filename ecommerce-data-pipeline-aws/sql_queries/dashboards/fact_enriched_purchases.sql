CREATE OR REPLACE VIEW ecommerce_analytics.fact_enriched_purchases AS
SELECT
    fp.*,
    c.category_code,
    c.main_category,
    c.sub_category,
    p.brand,
    t.year,
    t.month,
    t.day,
    t.hour,
    t.weekday,
    t.week,
    t.quarter,
    u.user_ltv,
    u.ltv_segment
FROM ecommerce_analytics.fact_purchases fp
LEFT JOIN ecommerce_analytics.dim_category c
  ON fp.category_id = c.category_id
LEFT JOIN ecommerce_analytics.dim_product p
  ON fp.product_id = p.product_id
LEFT JOIN ecommerce_analytics.dim_time t
  ON fp.event_time = t.event_time
LEFT JOIN ecommerce_analytics.user_ltv u
  ON fp.user_id = u.user_id