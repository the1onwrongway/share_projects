import pandas as pd

SRC = "/kaggle/input/ecommerce-behavior-data-from-multi-category-store/2019-Oct.csv"
DEST = "sample_100k.csv"

df = pd.read_csv(SRC, nrows=100000)
df.to_csv(DEST, index=False)
print("Wrote", DEST)
