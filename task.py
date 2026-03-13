import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Users\TOSHIB\Desktop\Bank_Task\bank.csv")

# =========================
# Part 1: Data Understanding
# =========================
print("First 5 rows:")
print(df.head())

print("\nShape of dataset:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nDataset info:")
print(df.info())

# =========================
# Part 2: Data Type Checking
# =========================
num_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
cat_cols = df.select_dtypes(include=['object', 'string', 'str']).columns.tolist()

print("\nNumerical columns:")
print(num_cols)

print("\nCategorical columns:")
print(cat_cols)

# =========================
# Part 3: Missing Values Analysis
# =========================
print("\nMissing values in each column:")
print(df.isnull().sum())

missing_table = pd.DataFrame({
    "Column": df.columns,
    "Null Count": df.isnull().sum().values,
    "Null Percentage": (df.isnull().mean() * 100).values
})

print("\nMissing Values Table:")
print(missing_table)

# =========================
# Part 4: Handling Missing Values
# =========================

# Method 1: Drop columns with more than 40% missing values
df_drop_col = df.loc[:, df.isnull().mean() <= 0.40]
print("\nShape after dropping columns with >40% missing:")
print(df_drop_col.shape)

# Method 2: Drop rows containing null values
before_rows = df.shape
df_drop_rows = df.dropna()
after_rows = df_drop_rows.shape

print("\nDataset shape before dropping rows:")
print(before_rows)

print("\nDataset shape after dropping rows:")
print(after_rows)

# Method 3: Imputation
df_imputed = df.copy()

for col in num_cols:
    df_imputed[col] = df_imputed[col].fillna(df_imputed[col].mean())

for col in cat_cols:
    if df_imputed[col].isnull().sum() > 0:
        df_imputed[col] = df_imputed[col].fillna(df_imputed[col].mode()[0])

print("\nMissing values after imputation:")
print(df_imputed.isnull().sum())

# =========================
# Part 5: Basic Visualization
# =========================

# 1. Histogram of age
plt.figure(figsize=(8,5))
sns.histplot(df_imputed["age"], bins=20)
plt.title("Histogram of Age")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# 2. Boxplot of balance
plt.figure(figsize=(8,5))
sns.boxplot(x=df_imputed["balance"])
plt.title("Boxplot of Balance")
plt.xlabel("Balance")
plt.show()

# 3. Distribution of duration
plt.figure(figsize=(8,5))
sns.histplot(df_imputed["duration"], bins=20)
plt.title("Distribution of Duration")
plt.xlabel("Duration")
plt.ylabel("Count")
plt.show()

# 4. Bar chart of job
plt.figure(figsize=(12,6))
sns.countplot(data=df_imputed, x="job", order=df_imputed["job"].value_counts().index)
plt.title("Bar Chart of Job")
plt.xlabel("Job")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# 5. Bar chart of deposit
plt.figure(figsize=(6,4))
sns.countplot(data=df_imputed, x="deposit")
plt.title("Bar Chart of Deposit")
plt.xlabel("Deposit")
plt.ylabel("Count")
plt.show()

# 6. Count plot of deposit vs housing
plt.figure(figsize=(8,5))
sns.countplot(data=df_imputed, x="deposit", hue="housing")
plt.title("Count Plot of Deposit vs Housing")
plt.xlabel("Deposit")
plt.ylabel("Count")
plt.savefig("age_histogram.png")
plt.show()
