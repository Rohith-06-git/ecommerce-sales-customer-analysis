import csv

file_path = "data/raw/amazon_ecommerce_1M.csv"

with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    header = next(reader)

    print("Number of columns:", len(header))
    print("\nColumns:")
    for column in header:
        print("-", column)