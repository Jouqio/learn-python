"""
Topic: Standard Deviation
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Standard deviation measures how spread out values are around the mean.

# ============================================
# 2. EXAMPLE
# ============================================

import numpy as np

data = np.array([32, 111, 138, 28, 59, 77, 97])
print("Std Dev:", np.std(data))
print("Variance:", np.var(data))

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Compute the standard deviation of a small dataset.
# EXERCISE 2 (easy): Compute the variance of the same dataset and relate it to std dev (variance = std^2).
# EXERCISE 3 (easy): Compare the std dev of two datasets with the same mean but different spread.
# EXERCISE 4 (medium): Explain (via prints) what a low vs high standard deviation implies.
# EXERCISE 5 (medium): Compute std dev using the statistics module instead of NumPy.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that flags values in a dataset that are more than 2 standard deviations from the mean (simple outlier detection).


# ============================================
# 5. SUMMARY
# ============================================
# Standard deviation quantifies spread; low values mean data clusters near the mean, high values mean it's spread out.
