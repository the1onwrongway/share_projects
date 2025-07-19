
CREATE EXTERNAL TABLE IF NOT EXISTS dim_user (
  user_id bigint
)
STORED AS PARQUET
LOCATION 's3://ecommerce-pipeline-milan/dim/user/';

select * from dim_user limit 5