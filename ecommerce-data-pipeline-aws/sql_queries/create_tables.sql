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