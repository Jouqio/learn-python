"""
Topic: Plotting X and Y Points
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# plt.plot(x, y) draws lines/points connecting the given coordinate pairs.

# ============================================
# 2. EXAMPLE
# ============================================

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

x_points = [1, 3, 5, 7]
y_points = [2, 6, 4, 8]
plt.plot(x_points, y_points)
plt.savefig("plot_xy.png")
print("Saved plot_xy.png")

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Plot 5 custom (x, y) pairs.
# EXERCISE 2 (easy): Plot only points (no connecting line) using a marker string.
# EXERCISE 3 (easy): Plot two datasets on the same chart with a legend.
# EXERCISE 4 (medium): Plot a single point using plt.plot(x, y, 'o').
# EXERCISE 5 (medium): Label each axis and add a title to your x-y plot.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that plots a mathematical function (e.g. y = x^2) over a given x range.


# ============================================
# 5. SUMMARY
# ============================================
# Understanding x/y point plotting is the foundation for every other chart type in matplotlib.
