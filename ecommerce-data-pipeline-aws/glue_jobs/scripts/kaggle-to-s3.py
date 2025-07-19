# ──────────────────────────────────────────────────────────────
#  Glue Job : kaggle_to_s3_full.py
#  Author   : Milan Gabriel
#  Created  : 2025-07-14
#  Purpose  : Download Kaggle e-commerce clickstream dataset
#             and upload each CSV to S3 raw zone.
# ──────────────────────────────────────────────────────────────

# 0️⃣  Glue boilerplate (must be first)
import sys, os, zipfile
from pathlib import Path

from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from awsglue.job import Job
from pyspark.context import SparkContext

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc   = SparkContext()
glue = GlueContext(sc)
spark = glue.spark_session
job  = Job(glue)
job.init(args["JOB_NAME"], args)

# 1️⃣  Fix permissions & env for Kaggle API
os.environ["HOME"] = "/tmp"                               # Writable HOME
KAGGLE_USERNAME     = "milangabriel"                      # ← replace
KAGGLE_KEY          = "cbcd5766f1f04662ace25b55231a8d90"  # ← replace

kaggle_dir = Path("/tmp/.kaggle")
kaggle_dir.mkdir(parents=True, exist_ok=True)
with open(kaggle_dir / "kaggle.json", "w") as f:
    f.write(f'{{"username":"{KAGGLE_USERNAME}","key":"{KAGGLE_KEY}"}}')
os.chmod(kaggle_dir / "kaggle.json", 0o600)

# 2️⃣  Import extra libraries (available because of --additional-python-modules)
from kaggle.api.kaggle_api_extended import KaggleApi
from tqdm import tqdm
import boto3

# 3️⃣  Download dataset to /tmp
api = KaggleApi(); api.authenticate()
DATASET   = "mkechinov/ecommerce-behavior-data-from-multi-category-store"
LOCAL_DIR = Path("/tmp/ecom_raw")
LOCAL_DIR.mkdir(parents=True, exist_ok=True)

print("⬇️  Downloading Kaggle dataset …")
api.dataset_download_files(DATASET, path=LOCAL_DIR, unzip=True)
print("✅  Download done")

# 4️⃣  Upload each CSV to S3 raw zone
s3     = boto3.client("s3")
bucket = "ecommerce-pipeline-milan"
prefix = "raw/clickstream/"        # trailing slash important

csv_files = list(LOCAL_DIR.glob("*.csv"))
print(f"⬆️  Uploading {len(csv_files)} CSV files to s3://{bucket}/{prefix}")

for csv_path in tqdm(csv_files):
    s3.upload_file(
        Filename=str(csv_path),
        Bucket=bucket,
        Key=f"{prefix}{csv_path.name}"
    )

print("🎉  All CSVs uploaded to S3")

# 5️⃣  Clean up (optional)
# shutil.rmtree(LOCAL_DIR)  # uncomment if you want to free /tmp space

# 6️⃣  Finish
job.commit()