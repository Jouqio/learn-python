"""
Topic: Markers
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Markers ('o', 's', '^', etc.) customize how individual data points are drawn.

# ============================================
# 2. EXAMPLE
# ============================================

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], marker="o")
plt.savefig("plot_markers.png")
print("Saved plot_markers.png")

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Plot data using a circle marker 'o'.
# EXERCISE 2 (easy): Plot data using a star marker '*'.
# EXERCISE 3 (easy): Combine a marker with a line style (e.g. '--o').
# EXERCISE 4 (medium): Change marker size using markersize.
# EXERCISE 5 (medium): Change marker color using markerfacecolor.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that plots the same dataset 3 times with 3 different markers side-by-side as subplots.


# ============================================
# 5. SUMMARY
# ============================================
# Markers help distinguish individual data points, especially on sparse or scattered datasets.
