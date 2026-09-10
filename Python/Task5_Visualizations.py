import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned dataset
df = pd.read_csv("../Dataset/Superstore_Sales_Cleaned.csv")

# Create output folder
output_folder = "../Visualizations"
os.makedirs(output_folder, exist_ok=True)

# Convert Order Date
df["Order Date"] = pd.to_datetime(df["Order Date"])

# ==========================================================
# 1. MONTHLY SALES TREND
# ==========================================================

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
)

plt.figure(figsize=(12, 6))
plt.plot(
    monthly_sales.index.astype(str),
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    os.path.join(output_folder, "01_Monthly_Sales_Trend.png"),
    dpi=300
)
plt.close()

# ==========================================================
# 2. SALES BY REGION
# ==========================================================

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(9, 6))
plt.bar(region_sales.index, region_sales.values)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    os.path.join(output_folder, "02_Sales_by_Region.png"),
    dpi=300
)
plt.close()

# ==========================================================
# 3. SALES BY CATEGORY
# ==========================================================

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(9, 6))
plt.bar(category_sales.index, category_sales.values)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()

plt.savefig(
    os.path.join(output_folder, "03_Sales_by_Category.png"),
    dpi=300
)
plt.close()

# ==========================================================
# 4. PROFIT BY SUB-CATEGORY
# ==========================================================

subcategory_profit = (
    df.groupby("Sub-Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(11, 7))
plt.barh(
    subcategory_profit.index,
    subcategory_profit.values
)

plt.title("Profit by Sub-Category")
plt.xlabel("Total Profit")
plt.ylabel("Sub-Category")
plt.tight_layout()

plt.savefig(
    os.path.join(output_folder, "04_Profit_by_SubCategory.png"),
    dpi=300
)
plt.close()

# ==========================================================
# 5. CORRELATION HEATMAP
# ==========================================================

correlation = df[
    ["Sales", "Quantity", "Discount", "Profit"]
].corr()

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f"
)

plt.title("Correlation Heatmap")
plt.tight_layout()

plt.savefig(
    os.path.join(output_folder, "05_Correlation_Heatmap.png"),
    dpi=300
)
plt.close()

print("=" * 60)
print("TASK 5 - DATA VISUALIZATION")
print("=" * 60)

print("\n===== VISUALIZATIONS CREATED =====")

print("1. Monthly Sales Trend")
print("2. Sales by Region")
print("3. Sales by Category")
print("4. Profit by Sub-Category")
print("5. Correlation Heatmap")

print("\n===== OUTPUT FOLDER =====")
print(output_folder)

print("\n===== TASK 5 COMPLETED =====")