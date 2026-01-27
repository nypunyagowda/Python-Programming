import pandas as pd

# 1) Create DataFrame from list of lists
data = [
    [101, "Alice", "CS", 85],
    [102, "Bob", "IT", 90],
    [103, "Charlie", "CS", 78],
    [104, "David", "IT", 92],
    [105, "Eva", "CS", 88]
]

df = pd.DataFrame(data, columns=["ID", "Name", "Dept", "Marks"])
print("Initial DataFrame:\n", df, "\n")

# 2) Set index
df.set_index("ID", inplace=True)
print("After setting ID as index:\n", df, "\n")

# 3) Rename column
df.rename(columns={"Marks": "Score"}, i
