"""
Topic: Adding Grid Lines
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# plt.grid() adds gridlines to make reading exact values off a chart easier.

# ============================================
# 2. EXAMPLE
# ============================================

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [3, 6, 9])
plt.grid(True)
plt.savefig("plot_grid.png")
print("Saved plot_grid.png")

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Add a basic grid to a plot.
# EXERCISE 2 (easy): Show only horizontal gridlines using axis='y'.
# EXERCISE 3 (easy): Show only vertical gridlines using axis='x'.
# EXERCISE 4 (medium): Customize gridline color and line style.
# EXERCISE 5 (medium): Compare a chart with and without a grid (2 saved images).
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that overlays a grid on any chart to help readers estimate values precisely.


# ============================================
# 5. SUMMARY
# ============================================
# Gridlines improve chart readability, especially for precise value estimation.
