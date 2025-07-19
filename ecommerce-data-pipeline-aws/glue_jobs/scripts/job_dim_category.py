"""
Glue Job – dim_category
Author : Milan Gabriel
Date   : 2025-07-14
Desc   : Build category dimension from category_code column.
"""

from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql.functions import col, split
import sys

# ── Glue setup ──
args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc   = SparkContext()
glue = GlueContext(sc)
spark = glue.spark_session
job  = Job(glue)
job.init(args["JOB_NAME"], args)

# 1️⃣ Load cleaned purchase data
df = spark.read.parquet("s3://ecommerce-pipeline-milan/clean/clickstream/purchases/")

# 2️⃣ Extract unique category codes
dim_category = (
    df
    .select("category_id", "category_code")
    .dropna(subset=["category_id", "category_code"])
    .dropDuplicates(["category_id"])
    .withColumn("main_category", split(col("category_code"), "\\.").getItem(0))
    .withColumn("sub_category",  split(col("category_code"), "\\.").getItem(1))
)

# 3️⃣ Write to S3
dim_category.write.mode("overwrite").parquet("s3://ecommerce-pipeline-milan/dim/category/")

job.commit()