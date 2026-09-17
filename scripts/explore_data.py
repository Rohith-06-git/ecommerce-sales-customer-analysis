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

print(df["subcategory"].value_counts())

print("Unique users:", df["user_id"].nunique())
print("Unique products:", df["product_id"].nunique())
print("Unique sellers", df["seller_id"].nunique())

#Check repeated purchases by the same customer
print(df["user_id"].value_counts().head(10))

print(df[df["user_id"] == "U387936"])

print(
    df.groupby(["user_id", "product_id"]).size().sort_values(ascending=False).head(10)
)

print(df["is_returned"].value_counts())
print(df.groupby("category")["is_returned"].mean())

#payment methods
print(df["payment_method"].value_counts())

# device usage
print(df["device"].value_counts())

# delivery status
print(df["delivery_status"].value_counts())

# how many repeated users + product combinations are there ?
print(df.duplicated(subset=["user_id","product_id"]).sum())

# location distribution 
print(df["location"].value_counts())

# Does final_price actually represent the price after applying the discount?
df["calculated_price"] = df["price"] * (1 - df["discount"] / 100)
print((df["calculated_price"] - df["final_price"]).abs().max())

# All about the pricing difference 
print((df["calculated_price"] - df["final_price"]).abs().describe())

# Finding the user who has large difference in pricing
df["calculated_price"] = df["price"] * ( 1 - df["discount"] / 100 )
df["price_diff"] = (df["calculated_price"] - df["final_price"]).abs()
print(df.loc[df["price_diff"].idxmax()] , ["price","discount","calculated_price","final_price","price_diff"])