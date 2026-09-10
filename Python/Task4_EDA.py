import pandas as pd
import numpy as np

# Load cleaned dataset
file_path = "../Dataset/Superstore_Sales_Cleaned.csv"
df = pd.read_csv(file_path)

print("=" * 70)
print("TASK 4 - EXPLORATORY DATA ANALYSIS")
print("=" * 70)

# --------------------------------------------------
# 1. DATA INSPECTION
# --------------------------------------------------
print("\n===== DATASET SHAPE =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n===== FIRST 5 RECORDS =====")
print(df.head())

# --------------------------------------------------
# 2. DESCRIPTIVE STATISTICS
# --------------------------------------------------
print("\n===== DESCRIPTIVE STATISTICS =====")
print(df[["Sales", "Quantity", "Discount", "Profit"]].describe())

# --------------------------------------------------
# 3. TOTAL BUSINESS METRICS
# --------------------------------------------------
print("\n===== BUSINESS METRICS =====")
print("Total Sales:", round(df["Sales"].sum(), 2))
print("Total Profit:", round(df["Profit"].sum(), 2))
print("Total Quantity:", df["Quantity"].sum())
print("Average Sales:", round(df["Sales"].mean(), 2))
print("Average Profit:", round(df["Profit"].mean(), 2))

# --------------------------------------------------
# 4. SALES BY REGION
# --------------------------------------------------
print("\n===== SALES BY REGION =====")
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print(region_sales)

# --------------------------------------------------
# 5. PROFIT BY REGION
# --------------------------------------------------
print("\n===== PROFIT BY REGION =====")
region_profit = df.groupby("Region")["Profit"].sum().sort_values(ascending=False)
print(region_profit)

# --------------------------------------------------
# 6. SALES BY CATEGORY
# --------------------------------------------------
print("\n===== SALES BY CATEGORY =====")
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print(category_sales)

# --------------------------------------------------
# 7. PROFIT BY CATEGORY
# --------------------------------------------------
print("\n===== PROFIT BY CATEGORY =====")
category_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
print(category_profit)

# --------------------------------------------------
# 8. SALES BY SUB-CATEGORY
# --------------------------------------------------
print("\n===== SALES BY SUB-CATEGORY =====")
subcategory_sales = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False)
print(subcategory_sales)

# --------------------------------------------------
# 9. PROFIT BY SUB-CATEGORY
# --------------------------------------------------
print("\n===== PROFIT BY SUB-CATEGORY =====")
subcategory_profit = df.groupby("Sub-Category")["Profit"].sum().sort_values(ascending=False)
print(subcategory_profit)

# --------------------------------------------------
# 10. TOP 10 PRODUCTS
# --------------------------------------------------
print("\n===== TOP 10 PRODUCTS BY SALES =====")
top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print(top_products)

# --------------------------------------------------
# 11. MONTHLY SALES TREND
# --------------------------------------------------
df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
)

print("\n===== MONTHLY SALES TREND =====")
print(monthly_sales)

# --------------------------------------------------
# 12. CORRELATION ANALYSIS
# --------------------------------------------------
print("\n===== CORRELATION MATRIX =====")
correlation = df[["Sales", "Quantity", "Discount", "Profit"]].corr()
print(correlation.round(3))

# --------------------------------------------------
# 13. OUTLIER DETECTION USING IQR
# --------------------------------------------------
print("\n===== OUTLIER DETECTION =====")

Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["Sales"] < lower_limit) |
    (df["Sales"] > upper_limit)
]

print("Q1:", round(Q1, 2))
print("Q3:", round(Q3, 2))
print("IQR:", round(IQR, 2))
print("Lower Limit:", round(lower_limit, 2))
print("Upper Limit:", round(upper_limit, 2))
print("Number of Sales Outliers:", len(outliers))

# --------------------------------------------------
# 14. LOSS-MAKING TRANSACTIONS
# --------------------------------------------------
loss_transactions = df[df["Profit"] < 0]

print("\n===== LOSS-MAKING TRANSACTIONS =====")
print("Number of loss-making transactions:", len(loss_transactions))
print("Total loss:", round(loss_transactions["Profit"].sum(), 2))

# --------------------------------------------------
# 15. BEST AND WORST PERFORMING AREAS
# --------------------------------------------------
print("\n===== KEY FINDINGS =====")

print(
    "Best Region:",
    region_sales.idxmax(),
    "| Sales:",
    round(region_sales.max(), 2)
)

print(
    "Lowest Region:",
    region_sales.idxmin(),
    "| Sales:",
    round(region_sales.min(), 2)
)

print(
    "Best Category:",
    category_sales.idxmax(),
    "| Sales:",
    round(category_sales.max(), 2)
)

print(
    "Lowest Category:",
    category_sales.idxmin(),
    "| Sales:",
    round(category_sales.min(), 2)
)

print(
    "Top Product:",
    top_products.index[0],
    "| Sales:",
    round(top_products.iloc[0], 2)
)

print("\n===== TASK 4 EDA COMPLETED =====")