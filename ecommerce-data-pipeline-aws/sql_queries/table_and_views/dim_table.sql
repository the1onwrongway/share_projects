
CREATE EXTERNAL TABLE IF NOT EXISTS dim_time (
  event_time timestamp,
  year       int,
  month      int,
  day        int,
  hour       int,
  weekday    int,
  week       int,
  quarter    int
)
STORED AS PARQUET
LOCATION 's3://ecommerce-pipeline-milan/dim/time/';

SELECT * FROM dim_time LIMIT 10;