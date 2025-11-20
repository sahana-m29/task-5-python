# task-5-python
# Sales Data Analysis Using Python

This project performs **basic data analysis on a sales dataset** using
**Pandas** and **Matplotlib**.

## 📌 Features

-   Load CSV file using Pandas
-   Display first 5 rows
-   Show dataset information
-   Generate statistical summary
-   Group data by *Category*
-   Visualize total sales using a bar chart

------------------------------------------------------------------------

## 🧪 Code Used

``` python
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load CSV
df = pd.read_csv('sales.csv')

print("=== First 5 Rows ===")
print(df.head())

print("
=== Data Information ===")
print(df.info())

print("
=== Statistical Info ===")
print(df.describe())

# 2. Groupby Category
grouped = df.groupby('Category')['Sales'].sum()
print("
=== Total Sales by Category ===")
print(grouped)

# 3. Plot the chart
grouped.plot(kind='bar')
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.title("Sales Analysis")
plt.show()
```

------------------------------------------------------------------------

## 📁 Requirements

Install dependencies:

    pip install pandas matplotlib

------------------------------------------------------------------------

## ▶️ How to Run

1.  Place **sales.csv** in the same folder as the script.

2.  Save the analysis script as:

        analysis.py

3.  Run:

        python analysis.py

------------------------------------------------------------------------

## 📊 Output

-   Displays dataset preview
-   Shows summary statistics
-   Prints category-wise total sales
-   Shows a bar chart of sales

------------------------------------------------------------------------

## 🎯 Outcome

You will understand: - Using Pandas for data analysis\
- Grouping & summarizing datasets\
- Plotting charts with Matplotlib

Perfect for beginners learning **data analysis**.
