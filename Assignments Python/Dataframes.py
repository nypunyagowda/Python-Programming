import pandas as pd

# 1) Create DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [20, 22, 21],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data, index=["s1", "s2", "s3"])
print("Initial DataFrame:\n", df, "\n")

# 2) Access columns
print("Single column (Series):\n", df["Name"], "\n")
print("Multiple columns (DataFrame):\n", df[["Name", "Marks"]], "\n")

# 3) Access rows
print("Row using loc:\n", df.loc["s2"], "\n")
print("Row using iloc:\n", df.iloc[1], "\n")

# 4) Add new column
df["Passed"] = df["Marks"] > 85
print("After adding Passed column:\n", df, "\n")

# 5) Add new row
df.loc["s4"] = ["David", 23, 92, True]
print("After adding new row:\n", df, "\n")

# 6) Update a value
df.loc["s2", "Marks"] = 95
print("After updating Marks for s2:\n", df, "\n")

# 7) Drop a column and a row
df.drop("Age
