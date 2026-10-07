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

# Check shipping time
print(df["shipping_time_days"].describe())

# Checking Seller rating
print(df["seller_rating"].describe())

# Checking rating
print(df["rating"].describe())

# Checking stock
print(df["stock"].describe())

# Records with zero stock
print((df["stock"] == 0).sum())

# stock analysis
print(df["stock"].describe())

# Check products with zero stock
print("Zero stock records:", (df["stock"] == 0).sum())

# Review count analysis
print(df["review_count"].describe())

print("Products with no reviews:", (df["review_count"] == 0).sum())

# Customer analysis

print("Unique customers:", df["customer_id"].nunique())
print("Repeated customers:", (df["customer_id"].value_counts() > 1).sum())

# Customer frequency analysis
customer_counts = df["customer_id"].value_counts()

print("Unique customers:", df["customer_id"].nunique())
print("Customers with multiple records:", (customer_counts > 1).sum())
print("Maximum records by one customer:", customer_counts.max())

# Cardinality check
print("Unique categories:", df["category"].nunique())
print("Unique subcategories:", df["subcategory"].nunique())
print("Unique locations:", df["location"].nunique())
print("Unique payment methods:", df["payment_method"].nunique())
print("Unique devices:", df["device"].nunique())
print("Unique delivery statuses:", df["delivery_status"].nunique())

# Check duplicate records
print("Duplicate full rows:", df.duplicated().sum())

# Missing value summary
print(df.isna().sum().sort_values(ascending=False))

# data validity
print("Negative prices :" , (df["price"] < 0).sum())
print("Negative discount :" , (df["discount"] < 0).sum())
print("Negative final price :" , (df["final_price"] < 0).sum())
print("Negative rating :" , (df["rating"] < 0).sum())
print("Negative review count :" , (df["review_count"] < 0).sum())
print("Negative stock:" , (df["stock"] < 0).sum())
print("Negative shipping days:" , (df["shipping_time_days"] < 0).sum())

print("Categories:", df["category"].unique())
print("Devices:", df["device"].unique())
print("Payment methods:", df["payment_method"].unique())
print("Delivery statuses:", df["delivery_status"].unique())
print("Returned values:", df["is_returned"].unique())
df["category"].value_counts()

# Range validation
print("Price Range :", df["price"].min(), "-", df["price"].max())
print("Discount Range :", df["discount"].min(), "-", df["discount"].max())
print("Rating Range :", df["rating"].min(), "-", df["rating"].max())
print("seller rating Range :", df["seller_rating"].min(), "-", df["seller_rating"].max())
print("shipping days Range :", df["shipping_time_days"].min(), "-", df["shipping_time_days"].max())

df["purchase_date"] = pd.to_datetime(df["purchase_date"])

print("Date dtype :" ,df["purchase_date"].dtype)
print("Missing Dates :" ,df["purchase_date"].isna().sum())
print("Earliest Date :" ,df["purchase_date"].min())
print("Latest Date :" ,df["purchase_date"].max())

# Logical relationship between delivery_status and is_returned

print( pd.crosstab(df["delivery_status"],df["is_returned"]))