import pandas as pd
import matplotlib.pyplot as plt

# 1. Load CSV
df = pd.read_csv('sales.csv')

print("=== First 5 Rows ===")
print(df.head())

print("\n=== Data Information ===")
print(df.info())

print("\n=== Statistical Info ===")
print(df.describe())

# 2. Groupby Category
grouped = df.groupby('Category')['Sales'].sum()
print("\n=== Total Sales by Category ===")
print(grouped)

# 3. Plot the chart
grouped.plot(kind='bar')
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.title("Sales Analysis")
plt.show()