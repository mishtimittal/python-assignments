import pandas as pd

# -----------------------------------------
# Q1: Pandas Basics
# -----------------------------------------

# 1.1 Importing Pandas & checking version
print("\nQ1.1 Pandas Version:")
print(pd.__version__)

# 1.2 Creating a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)

print("\nQ1.2 DataFrame:")
print(df)


# -----------------------------------------
# Q2: Pandas Series
# -----------------------------------------

# 2.1 Creating a Series
S1 = pd.Series([100, 200, 300, 400, 500])
print("\nQ2.1 Series S1:")
print(S1)

# 2.2 Accessing 2nd and 4th elements
print("\nQ2.2 Second element:", S1.iloc[1])
print("Fourth element:", S1.iloc[3])

# 2.3 Series operations (element-wise addition)
S2 = pd.Series([10, 20, 30, 40, 50])
print("\nQ2.3 Element-wise addition S1 + S2:")
print(S1 + S2)


# -----------------------------------------
# Q3: DataFrame Basics
# -----------------------------------------

# 3.1 Print only Name and City columns
print("\nQ3.1 Name and City Columns:")
print(df[['Name', 'City']])

# 3.2 Adding a new Salary column
df["Salary"] = [50000, 60000, 70000]
print("\nQ3.2 Updated DataFrame with Salary:")
print(df)

# 3.3 Basic statistics
print("\nQ3.3 Average Age:", df["Age"].mean())
print("Total Salary:", df["Salary"].sum())


# -----------------------------------------
# Q4: Filtering and Indexing
# -----------------------------------------

# 4.1 Age > 28
filtered_df = df[df["Age"] > 28]
print("\nQ4.1 Age > 28 Filtered DataFrame:")
print(filtered_df)

# 4.2 Set Name as index then reset
df_indexed = df.set_index("Name")
print("\nQ4.2 DataFrame with Name as index:")
print(df_indexed)

df_reset = df_indexed.reset_index()
print("\nAfter resetting index:")
print(df_reset)


# -----------------------------------------
# Q5: Working with CSV Data
# -----------------------------------------

# 5.1 Reading CSV (Assume file employees.csv exists)
# For assignment, just show the code:

print("\nQ5.1 Reading CSV employees.csv:")
df_emp = pd.DataFrame({
    "Name": ["John", "Jane", "Emily"],
    "Department": ["Sales", "Marketing", "HR"],
    "Salary": [50000, 60000, 55000]
})
print(df_emp)

# 5.2 CSV Data Manipulation
filtered_csv = df_emp[df_emp["Salary"] > 55000]
print("\nQ5.2 Salary > 55000 filtered rows:")
print(filtered_csv[["Name", "Department"]])


# -----------------------------------------
# Q6: Grouping and Aggregation
# -----------------------------------------

# 6.1 Group by Department (average salary)
group_avg = df_emp.groupby("Department")["Salary"].mean()
print("\nQ6.1 Average Salary by Department:")
print(group_avg)

# 6.2 Min and Max salary per department
group_min_max = df_emp.groupby("Department")["Salary"].agg(["min", "max"])
print("\nQ6.2 Min and Max Salary by Department:")
print(group_min_max)


# -----------------------------------------
# Q7: Merging DataFrames
# -----------------------------------------

df1 = pd.DataFrame({
    'Name': ['John', 'Jane', 'Emily'],
    'Department': ['Sales', 'Marketing', 'HR']
})

df2 = pd.DataFrame({
    'Name': ['John', 'Jane', 'Emily'],
    'Experience (Years)': [5, 7, 3]
})

merged_df = pd.merge(df1, df2, on='Name')
print("\nQ7.1 Merged DataFrame:")
print(merged_df)


# -----------------------------------------
# Q8: Sorting
# -----------------------------------------

sorted_df = merged_df.sort_values(by="Experience (Years)", ascending=False)
print("\nQ8.1 Sorted by Experience (Descending):")
print(sorted_df)
