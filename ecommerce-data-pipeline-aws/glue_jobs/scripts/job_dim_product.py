"""
Glue Job – Create dim_product
Author  : Milan Gabriel
Date    : 2025-07-14
Desc    : Extract unique product attributes from the cleaned
          purchases fact set and store as a dimension table.
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

# 1️⃣  Read cleaned fact data
fact_df = spark.read.parquet(
    "s3://ecommerce-pipeline-milan/clean/clickstream/purchases/"
)

# 2️⃣  Build product dimension
dim_product = (
    fact_df
      .select(
          col("product_id").cast("bigint"),
          col("category_id").cast("bigint"),
          col("category_code"),
          col("brand")
      )
      .distinct()
)

# 3️⃣  Write to S3
dim_product.write.mode("overwrite").parquet(
    "s3://ecommerce-pipeline-milan/dim/product/"
)

job.commit()