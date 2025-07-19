
CREATE EXTERNAL TABLE IF NOT EXISTS fact_purchases (
  event_time    timestamp,
  product_id    bigint,
  category_id   bigint,
  user_id       bigint,
  price         double,
  user_session  string
)
STORED AS PARQUET
LOCATION 's3://ecommerce-pipeline-milan/fact/purchases/';