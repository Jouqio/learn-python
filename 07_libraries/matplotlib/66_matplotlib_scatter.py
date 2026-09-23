"""
Topic: Scatter Plots
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# plt.scatter() plots individual (x, y) points without connecting lines, ideal for showing relationships/correlation.

# ============================================
# 2. EXAMPLE
# ============================================

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

x = [5, 7, 8, 7, 2, 17, 2, 9]
y = [99, 86, 87, 88, 100, 86, 103, 87]
plt.scatter(x, y)
plt.savefig("plot_scatter.png")
print("Saved plot_scatter.png")

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Create a scatter plot from two lists of numbers.
# EXERCISE 2 (easy): Color scatter points by a third variable using the c parameter.
# EXERCISE 3 (easy): Change the point size using the s parameter.
# EXERCISE 4 (medium): Add labeled axes and a title to a scatter plot.
# EXERCISE 5 (medium): Overlay two scatter datasets with different colors on the same chart.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that creates a scatter plot of study hours vs exam scores, colored by pass/fail status.


# ============================================
# 5. SUMMARY
# ============================================
# Scatter plots are the go-to chart for visually inspecting relationships between two numeric variables.
