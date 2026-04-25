import pandas as pd

# Create a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
# Display the DataFrame
print(df)

print(df.head())
print(df.info())

# # Accessing columns
# print(df["Name"])
# print(df["Age"])

# # Accessing rows
# print(df.loc[0])  # Access by index
# print(df.iloc[1])  # Access by position

# # Adding a new column
# df["Country"] = ["USA", "USA", "USA"]
# print(df)

# # Filtering data
# filtered_df = df[df["Age"] > 28]
# print(filtered_df)