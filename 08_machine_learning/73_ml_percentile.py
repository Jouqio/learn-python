"""
Topic: Percentiles
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# A percentile indicates the value below which a given percentage of observations fall.

# ============================================
# 2. EXAMPLE
# ============================================

import numpy as np

ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]
print("75th percentile:", np.percentile(ages, 75))
print("Median (50th percentile):", np.percentile(ages, 50))

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Compute the 90th percentile of a dataset.
# EXERCISE 2 (easy): Compute the 25th and 75th percentiles (Q1 and Q3).
# EXERCISE 3 (easy): Compute the interquartile range (IQR = Q3 - Q1).
# EXERCISE 4 (medium): Explain what it means if someone's score is in the 95th percentile.
# EXERCISE 5 (medium): Use percentiles to identify potential outliers (below Q1-1.5*IQR or above Q3+1.5*IQR).
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `percentile_summary(data)` that returns the 25th, 50th, 75th percentiles and the IQR.


# ============================================
# 5. SUMMARY
# ============================================
# Percentiles describe relative standing within a dataset and are the basis for boxplots and outlier detection.
