"""
Title: Glue Job – Create dim_time from fact table
Author: Milan Gabriel
Created: 2025-07-14
Description:
    Builds a time dimension from distinct event_time values in the fact table.
    Outputs Parquet to S3 for Athena access.
"""

from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql.functions import (
    year, month, dayofmonth, hour, dayofweek, weekofyear, quarter
)
import sys

# Glue Job Params
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read cleaned purchases data
df = spark.read.parquet("s3://ecommerce-pipeline-milan/clean/clickstream/purchases/")

# Build time dimension
dim_time = (
    df.select("event_time").distinct()
      .withColumn("year", year("event_time"))
      .withColumn("month", month("event_time"))
      .withColumn("day", dayofmonth("event_time"))
      .withColumn("hour", hour("event_time"))
      .withColumn("weekday", dayofweek("event_time"))
      .withColumn("week", weekofyear("event_time"))
      .withColumn("quarter", quarter("event_time"))
)

# Write dim_time to S3
dim_time.write.mode("overwrite").parquet("s3://ecommerce-pipeline-milan/dim/time/")

job.commit()