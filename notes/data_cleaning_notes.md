# Data Cleaning Notes

## 1. Categorical Data Consistency

Categorical values can sometimes represent the same thing in different formats.

Example:

- Electronics
- electronics
- ELECTRONICS
- " Electronics "

These should be standardized before analysis.

### Standardizing text

```python
df["category"] = df["category"].str.strip().str.title()
```

- `.str.strip()` → removes leading/trailing spaces
- `.str.title()` → standardizes capitalization

Example:

```text
"electronics"    → "Electronics"
"ELECTRONICS"    → "Electronics"
" Electronics "  → "Electronics"
```

Then check:

```python
df["category"].value_counts()
```

---

## 2. Converting Yes/No to Boolean

Sometimes Boolean information is stored as text:

- Yes
- No

We can convert these values into:

- True
- False

### Example

```python
df["is_returned"] = (
    df["is_returned"]
    .str.strip()
    .str.lower()
    .map({
        "yes": True,
        "no": False
    })
)
```

### What happens?

```text
"Yes" → True
"No"  → False
" yes " → True
"NO" → False
```

- `.str.strip()` → removes extra spaces
- `.str.lower()` → converts text to lowercase
- `.map()` → maps `"yes"` and `"no"` to Boolean values

### Always inspect first

```python
df["is_returned"].unique()
```

If the column already contains:

```text
True
False
```

then no conversion is needed.

In our current dataset, `is_returned` is already Boolean.

---

## 3. Checking and Removing Extra Whitespace

Text values can sometimes contain unwanted spaces at the beginning or end.

Example:

```text
"Electronics"
"Electronics "
" Electronics"
```

These may look the same when displayed, but Pandas treats them as different string values.

### Checking for extra whitespace

We can use `.str.strip()` to remove leading and trailing spaces temporarily and compare the result with the original values.

```python
df["category"].str.strip().ne(df["category"]).sum()
```

### Understanding the code

#### `.str.strip()`

Removes spaces from the beginning and end of each string.

```text
" Electronics " → "Electronics"
"Electronics "  → "Electronics"
" Electronics"  → "Electronics"
```

It does **not** remove spaces between words.

```text
"Cash on Delivery" → "Cash on Delivery"
```

---

#### `.ne()`

`.ne()` means **"not equal"**.

```python
df["category"].str.strip().ne(df["category"])
```

It compares:

```text
cleaned value != original value
```

For example:

```text
Original        Stripped        Result

Electronics     Electronics     False
Electronics     Electronics     True
 Electronics    Electronics     True
```

So:

- `False` → no extra leading/trailing spaces
- `True` → extra whitespace exists

---

#### `.sum()`

Boolean values are treated as numbers by Pandas:

```text
True  = 1
False = 0
```

Therefore:

```python
df["category"].str.strip().ne(df["category"]).sum()
```

counts how many rows contain extra whitespace.

Example:

```text
False
True
False
True
False
```

The sum is:

```text
2
```

So there are **2 values containing extra whitespace**.

---

### Checking multiple categorical columns

We can check several columns:

```python
print(
    "Category values with spaces:",
    df["category"].str.strip().ne(df["category"]).sum()
)

print(
    "Device values with spaces:",
    df["device"].str.strip().ne(df["device"]).sum()
)

print(
    "Payment method values with spaces:",
    df["payment_method"].str.strip().ne(df["payment_method"]).sum()
)

print(
    "Delivery status values with spaces:",
    df["delivery_status"].str.strip().ne(df["delivery_status"]).sum()
)
```

If all results are `0`, there are no leading/trailing whitespace issues in those columns.

---

### Removing the whitespace

If whitespace is found, we can clean the column:

```python
df["category"] = df["category"].str.strip()
```

For multiple categorical columns:

```python
categorical_cols = [
    "category",
    "device",
    "payment_method",
    "delivery_status"
]

for col in categorical_cols:
    df[col] = df[col].str.strip()
```

---

## Important Rule

Always inspect the data before cleaning it.

Do not blindly apply cleaning operations to every column.

For example, standardizing capitalization may be appropriate for:

```text
Electronics
electronics
ELECTRONICS
```

but may be inappropriate for IDs, codes, or values where capitalization has meaning.

First inspect the values:

```python
df["column"].unique()
```

Then decide whether cleaning is necessary.

### Current Project Result

For our current dataset:

- No obvious capitalization inconsistencies were found.
- No obvious whitespace issues were found.
- `is_returned` is already stored as `True`/`False`.
- Therefore, no categorical cleaning is required at this stage.

---

## Quick Revision

```text
.str.strip()
→ removes leading/trailing spaces

.str.lower()
→ converts text to lowercase

.str.title()
→ converts text to title case

.map()
→ maps values to new values

.ne()
→ checks "not equal"

.sum()
→ counts True values because True = 1
```

### Useful Pattern

```python
df["column"].str.strip().ne(df["column"]).sum()
```

Meaning:

> Remove spaces temporarily → compare with the original → find differences → count them.

## 4. Numeric Range Validation

A value can be non-negative but still be invalid or suspicious.

For example:

```text
Rating = 8
```

is not negative, but if ratings are on a 0–5 scale, it is invalid.

Therefore, we should check the minimum and maximum values of important numeric columns.

### Checking ranges

```python
print("Price range:", df["price"].min(), "-", df["price"].max())
print("Discount range:", df["discount"].min(), "-", df["discount"].max())
print("Rating range:", df["rating"].min(), "-", df["rating"].max())
print("Seller rating range:", df["seller_rating"].min(), "-", df["seller_rating"].max())
print("Shipping days range:", df["shipping_time_days"].min(), "-", df["shipping_time_days"].max())
```

### Understanding `.min()` and `.max()`

`.min()` returns the smallest value:

```python
df["price"].min()
```

`.max()` returns the largest value:

```python
df["price"].max()
```

Together, they give us the range of a column.

Example:

```text
Price range: 200.14 - 79885.53
```

means the smallest price is `200.14` and the largest price is `79885.53`.

### Why range validation is useful

It helps identify values that may be:

- Impossible
- Outside the expected business range
- Data-entry errors
- Suspicious outliers

For example:

```text
Rating: 0 - 5       → expected
Rating: 2 - 5       → possible, depending on the dataset
Rating: 2 - 8       → suspicious
```

### Important

A large value is not automatically an error.

For example:

```text
Price = 79,885.53
```

may be expensive, but it is not necessarily invalid.

We should investigate unusual values before removing or changing them.

### Current Project Result

For our 10,000-row sample:

```text
Price:             200.14 - 79885.53
Discount:          5.01 - 69.96
Rating:            2.0 - 5.0
Seller rating:     2.5 - 5.0
Shipping days:     1 - 6
```

No obviously invalid ranges were found in these columns.

### Key Idea

```text
Negative-value check
        ↓
Catches impossible negative values

Range validation
        ↓
Catches values that are outside sensible boundaries
```

Both checks are useful during data cleaning.