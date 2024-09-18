import pandas as pd

# Load a CSV file into a DataFrame (replace 'your_file.csv' with the actual file path)
df = pd.read_csv("your_file.csv")

# Display the first few rows of the DataFrame
print("First 5 rows of the DataFrame:")
print(df.head())

# Display the structure of the DataFrame
print("\nDataFrame Info:")
print(df.info())

# Display summary statistics
print("\nSummary statistics:")
print(df.describe())

# Selecting a specific column
print("\nDisplay a specific column (e.g., 'Name'):")
print(df["Name"])

# Filtering rows based on a condition
print("\nFilter rows where a numeric column (e.g., 'Age') is greater than 30:")
print(df[df["Age"] > 30])

# Adding a new column
df["New_Column"] = "Default Value"
print("\nDataFrame after adding a new column:")
print(df.head())

# Save the modified DataFrame to a new CSV file
df.to_csv("modified_file.csv", index=False)
