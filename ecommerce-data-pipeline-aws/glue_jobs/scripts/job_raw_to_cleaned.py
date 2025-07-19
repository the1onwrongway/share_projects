"""
Glue Job – Raw ➜ Cleaned Clickstream  (author: Milan Gabriel)
"""

from awsglue.context import GlueContext
from awsglue.job     import Job
from awsglue.utils   import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql.functions import col, to_timestamp, regexp_replace, year, month
import sys

args = getResolvedOptions(sys.argv, ["JOB_NAME"])

sc     = SparkContext()
glue   = GlueContext(sc)
spark  = glue.spark_session
job    = Job(glue)
job.init(args["JOB_NAME"], args)

# 1. Read & narrow columns early
raw_df = (
    spark.read.option("header", "true")
         .csv("s3://ecommerce-pipeline-milan/raw/clickstream/")
         .select("event_time", "event_type", "product_id",
                 "category_id", "category_code", "brand",
                 "price", "user_id", "user_session")
)

# 2. Transform
cleaned_df = (
    raw_df
      .filter(col("event_type") == "purchase")
      .withColumn("event_time",
                  to_timestamp(regexp_replace("event_time", " UTC", ""),
                               "yyyy-MM-dd HH:mm:ss"))
      .withColumn("product_id",  col("product_id").cast("bigint"))
      .withColumn("category_id", col("category_id").cast("bigint"))
      .withColumn("price",       col("price").cast("double"))
      .withColumn("user_id",     col("user_id").cast("bigint"))
      .withColumn("year", year("event_time"))
      .withColumn("month", month("event_time"))
      .drop("event_type")              # no longer needed
)

# 3. Write partitioned Parquet
(
    cleaned_df
      .write
      .mode("overwrite")               # change to "append" for incremental loads
      .option("compression", "snappy")
      .partitionBy("year", "month")
      .parquet("s3://ecommerce-pipeline-milan/clean/clickstream/purchases/")
)

job.commit()