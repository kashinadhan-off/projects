import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:/Users/Kashi/DS_Projects/datasets/sales_data_sample.csv", encoding="latin1")
# 1️⃣ Sales by Product Line
df.groupby("PRODUCTLINE")["SALES"].sum().sort_values().plot(
    kind="barh", title="Total Sales by Product Line"
)
plt.xlabel("Total Sales")
plt.show()

# 2️⃣ Year-wise Sales Trend
df.groupby("YEAR_ID")["SALES"].sum().plot(
    marker="o", title="Year-wise Sales Trend"
)
plt.xlabel("Year")
plt.ylabel("Sales")
plt.show()

# 3️⃣ Sales by Deal Size
df.groupby("DEALSIZE")["SALES"].sum().plot(
    kind="bar", title="Sales by Deal Size"
)
plt.ylabel("Total Sales")
plt.show()
