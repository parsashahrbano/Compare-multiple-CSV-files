import pandas as pd

# Read the CSV files into DataFrames
df1 = pd.read_csv('file01.csv')
df2 = pd.read_csv('file02.csv')
df3 = pd.read_csv('file03.csv')
df4 = pd.read_csv('file04.csv')
df5 = pd.read_csv('file05.csv')

# Initialize an empty DataFrame with the same structure
max_df = pd.DataFrame(index=df1.index, columns=df1.columns)

# Iterate over each cell and find the maximum value
for row in df1.index:
    for col in df1.columns:
        max_df.at[row, col] = max(df1.at[row, col], df2.at[row, col], df3.at[row, col], df4.at[row, col], df5.at[row, col])

# Save the result to a new CSV file
max_df.to_csv('max_values.csv', index=False)
