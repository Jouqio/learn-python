"""
Topic: Polynomial Regression
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Polynomial regression fits a curved line by using powers of x, useful when the relationship isn't straight.

# ============================================
# 2. EXAMPLE
# ============================================

import numpy as np

x = np.array([1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13])
y = np.array([100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75])

coefficients = np.polyfit(x, y, 3)
model = np.poly1d(coefficients)
print("Predicted at x=9:", round(model(9), 1))

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Fit a degree-2 polynomial to a small dataset.
# EXERCISE 2 (easy): Fit a degree-3 polynomial and compare predictions with degree-2.
# EXERCISE 3 (easy): Plot the original data points and the polynomial curve together.
# EXERCISE 4 (medium): Explain the risk of overfitting with a very high polynomial degree.
# EXERCISE 5 (medium): Compute the R-squared value using numpy or sklearn.metrics.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that fits a polynomial of a given degree and returns predictions for a list of new x values.


# ============================================
# 5. SUMMARY
# ============================================
# Polynomial regression models curved relationships, but higher degrees risk overfitting to noise.
