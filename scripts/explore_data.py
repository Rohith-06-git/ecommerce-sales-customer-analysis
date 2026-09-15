import pandas as pd

file_path = "data/raw/amazon_ecommerce_1M.csv"

df = pd.read_csv(file_path, nrows=10000)

print(df.shape)
print(df.info())
print(df.describe())

print(df["category"].value_counts())
print(df["category"].nunique())
print(df.isna().sum())
print(df.duplicated().sum())
print(df["device"].unique())
print(df.dtypes)

df["purchase_date"] = pd.to_datetime(df["purchase_date"])

print("Earliest date:", df["purchase_date"].min())
print("Latest date:", df["purchase_date"].max())

print(df[["price", "discount", "final_price", "rating",
          "review_count", "stock", "shipping_time_days",
          "seller_rating"]].describe())

print(df[["price", "discount", "final_price"]].head(10))