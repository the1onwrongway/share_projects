
CREATE EXTERNAL TABLE IF NOT EXISTS dim_product (
  product_id    bigint,
  category_id   bigint,
  category_code string,
  brand         string
)
STORED AS PARQUET
LOCATION 's3://ecommerce-pipeline-milan/dim/product/';

SELECT brand, COUNT(*) AS n_products
FROM dim_product
GROUP BY brand
ORDER BY n_products DESC
LIMIT 10;