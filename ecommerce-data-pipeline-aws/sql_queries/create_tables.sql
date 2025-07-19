
-- raw_clickstream external table (CSV)
CREATE EXTERNAL TABLE IF NOT EXISTS raw_clickstream (
  event_time string,
  event_type string,
  product_id bigint,
  category_id bigint,
  category_code string,
  brand string,
  price double,
  user_id bigint,
  user_session string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = ',',
  'field.delim' = ','
)
LOCATION 's3://ecommerce-pipeline-milan/raw/clickstream/'
TBLPROPERTIES ('skip.header.line.count'='1');

-- clean_clickstream table (Parquet)
CREATE TABLE clean_clickstream
WITH (
  format = 'PARQUET',
  external_location = 's3://ecommerce-pipeline-milan/clean/purchases/'
) AS
SELECT *
FROM raw_clickstream
WHERE event_type = 'purchase';


-- Athena External Table: cleaned purchase events
CREATE EXTERNAL TABLE IF NOT EXISTS clean_clickstream_purchases (
  event_time   timestamp,
  product_id   bigint,
  category_id  bigint,
  category_code string,
  brand        string,
  price        double,
  user_id      bigint,
  user_session string
)
PARTITIONED BY (year int, month int)
STORED AS PARQUET
LOCATION 's3://ecommerce-pipeline-milan/clean/clickstream/purchases/';


--Create dim_time table

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

--Create dim_product table
USE ecommerce_analytics;

CREATE EXTERNAL TABLE IF NOT EXISTS dim_product (
  product_id    bigint,
  category_id   bigint,
  category_code string,
  brand         string
)
STORED AS PARQUET
LOCATION 's3://ecommerce-pipeline-milan/dim/product/';