import pandas as pd

# Load dataset
file_path = "../Dataset/Superstore_Sales.csv"
df = pd.read_csv(file_path, encoding="latin1")

print("=" * 60)
print("SUPERSTORE SALES DATASET - DATA PREPARATION")
print("=" * 60)

# -------------------------------
# 1. ORIGINAL DATASET
# -------------------------------
print("\n===== ORIGINAL DATASET =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# -------------------------------
# 2. DATA TYPES
# -------------------------------
print("\n===== ORIGINAL DATA TYPES =====")
print(df.dtypes)

# -------------------------------
# 3. CONVERT DATE COLUMNS
# -------------------------------
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

print("\n===== DATE CONVERSION =====")
print("Order Date type:", df["Order Date"].dtype)
print("Ship Date type:", df["Ship Date"].dtype)

# -------------------------------
# 4. MISSING VALUES
# -------------------------------
print("\n===== MISSING VALUES BEFORE CLEANING =====")
print(df.isnull().sum())

# Remove rows with missing values
df = df.dropna()

print("\n===== MISSING VALUES AFTER CLEANING =====")
print(df.isnull().sum().sum())

# -------------------------------
# 5. DUPLICATES
# -------------------------------
duplicates = df.duplicated().sum()

print("\n===== DUPLICATES =====")
print("Duplicate rows found:", duplicates)

if duplicates > 0:
    df = df.drop_duplicates()

print("Duplicate rows after cleaning:", df.duplicated().sum())

# -------------------------------
# 6. CHECK INCORRECT VALUES
# -------------------------------
print("\n===== DATA VALIDATION =====")

print("Negative Sales:", (df["Sales"] < 0).sum())
print("Negative Quantity:", (df["Quantity"] < 0).sum())
print("Discount below 0:", (df["Discount"] < 0).sum())
print("Discount above 1:", (df["Discount"] > 1).sum())

# -------------------------------
# 7. REMOVE UNUSED COLUMN
# -------------------------------
# Row ID is only a sequential identifier
if "Row ID" in df.columns:
    df = df.drop(columns=["Row ID"])

print("\n===== COLUMNS AFTER CLEANING =====")
print(df.columns.tolist())

# -------------------------------
# 8. FINAL DATASET
# -------------------------------
print("\n===== FINAL DATASET =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n===== FINAL DATA TYPES =====")
print(df.dtypes)

# -------------------------------
# 9. SAVE CLEANED DATASET
# -------------------------------
output_file = "../Dataset/Superstore_Sales_Cleaned.csv"
df.to_csv(output_file, index=False)

print("\n===== CLEANED DATASET SAVED =====")
print("File:", output_file)

print("\n===== TASK 3 COMPLETED =====")