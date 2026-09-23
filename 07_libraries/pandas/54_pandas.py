"""
Topic: Pandas (Data Analysis Library)
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
Covers: Introduction, Getting Started, Series, DataFrames, Read CSV/JSON,
Analyze Data, Cleaning Data (empty cells, wrong format, wrong data, duplicates),
Correlations, Plotting.
Install with: pip install pandas matplotlib
"""
import pandas as pd

# ============================================
# 1. SERIES
# ============================================
scores = pd.Series([80, 90, 75], index=["Ani", "Budi", "Citra"])
print("Series:\n", scores)

# ============================================
# 2. DATAFRAMES
# ============================================
data = {
    "name": ["Ani", "Budi", "Citra", "Dedi"],
    "score": [80, 90, 75, None],
    "attendance": [95, 88, 92, 70],
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# ============================================
# 3. READ CSV / JSON (created here for a self-contained example)
# ============================================
df.to_csv("students.csv", index=False)
loaded = pd.read_csv("students.csv")
print("\nLoaded from CSV:\n", loaded)

# ============================================
# 4. ANALYZE DATA
# ============================================
print("\nSummary stats:\n", df.describe())
print("\nFirst 2 rows:\n", df.head(2))

# ============================================
# 5. CLEANING DATA
# ============================================
# 5a. Empty cells
cleaned = df.dropna()  # or df.fillna(0)
print("\nAfter dropna():\n", cleaned)

# 5b. Wrong format (example: attendance stored as text)
df["attendance"] = pd.to_numeric(df["attendance"], errors="coerce")

# 5c. Duplicates
df_with_dupe = pd.concat([df, df.iloc[[0]]], ignore_index=True)
print("\nHas duplicates:", df_with_dupe.duplicated().any())
df_no_dupe = df_with_dupe.drop_duplicates()
print("Rows after drop_duplicates:", len(df_no_dupe))

# ============================================
# 6. CORRELATIONS
# ============================================
numeric_df = df.dropna()
print("\nCorrelation matrix:\n", numeric_df[["score", "attendance"]].corr())

# ============================================
# 7. PLOTTING (saved to file instead of shown interactively)
# ============================================
try:
    import matplotlib
    matplotlib.use("Agg")
    ax = numeric_df.plot(x="name", y="score", kind="bar", legend=False)
    ax.figure.savefig("score_plot.png")
    print("\nSaved score_plot.png")
except ImportError:
    print("\nInstall matplotlib to enable plotting: pip install matplotlib")

# ============================================
# PRACTICE
# ============================================
# EASY 1: Create a Series of 5 city temperatures with city names as the index.
# EASY 2: Create a DataFrame from a dictionary with at least 3 columns.
# EASY 3: Use .info() to inspect a DataFrame's columns and types.
# MEDIUM 1: Load a CSV, drop rows with missing values, and print the new shape.
# MEDIUM 2: Group a DataFrame by one column and compute the mean of another using .groupby().
#
# CHALLENGE: Write a function `clean_dataset(df)` that fills missing numeric
# values with the column mean and removes duplicate rows, returning the result.

# ============================================
# SUMMARY
# ============================================
# Pandas Series and DataFrames make loading, cleaning, analyzing, and
# visualizing tabular data dramatically easier than plain Python structures.
