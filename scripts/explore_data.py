import pandas as pd

filepath = "data/raw/amazon_ecommerce_1M.csv"

df = pd.read_csv(filepath, nrows=5)

print(df.describe())