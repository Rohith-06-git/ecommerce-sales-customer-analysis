import pandas as pd

filepath = "data/raw/amazon_ecommerce_1M.csv"

df = pd.read_csv(filepath, nrows=10000)

print(df.shape)
print(df.info())
print(df.describe())
print(df["category"].value_counts())
print(df["category"].unique())
print(df.isna().sum())
print(df.duplicated().sum())
print(df["device"].unique())
print(df.dtypes)

print(df["purchase_date"].head())
df["purchase_date"] = pd.to_datetime(df["purchase_date"])
print(df.dtypes)