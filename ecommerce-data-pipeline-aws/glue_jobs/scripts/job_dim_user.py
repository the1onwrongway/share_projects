"""
Glue Job – Create dim_user
Author  : Milan Gabriel
Date    : 2025-07-14
Desc    : Extract unique users from purchases data
          and store as a user dimension.
"""

from awsglue.context import GlueContext
from awsglue.utils   import getResolvedOptions
from awsglue.job     import Job
from pyspark.context import SparkContext
from pyspark.sql.functions import col
import sys

# ── Glue boilerplate ──────────────────────────────────────────
args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc   = SparkContext()
glue = GlueContext(sc)
spark = glue.spark_session
job  = Job(glue)
job.init(args["JOB_NAME"], args)

# 1️⃣  Read cleaned purchase data
fact_df = spark.read.parquet(
    "s3://ecommerce-pipeline-milan/clean/clickstream/purchases/"
)

# 2️⃣  Build user dimension
dim_user = (
    fact_df
      .select(col("user_id").cast("bigint"))
      .distinct()
)

# 3️⃣  Write to S3
dim_user.write.mode("overwrite").parquet(
    "s3://ecommerce-pipeline-milan/dim/user/"
)

job.commit()