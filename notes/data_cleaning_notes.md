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