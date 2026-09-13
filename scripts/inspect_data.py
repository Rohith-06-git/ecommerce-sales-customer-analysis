import pandas as pd

file_path = "data/raw/amazon_ecommerce_1M.csv"

df = pd.read_csv(file_path, nrows=5)

print(df.shape)
print("----")
print(df.columns)
print("----")
print(df.info())
print("----")
print(df)