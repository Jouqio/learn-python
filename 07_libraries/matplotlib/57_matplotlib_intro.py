"""
Topic: Matplotlib Introduction
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Matplotlib is Python's most widely used plotting library, built around the pyplot module for MATLAB-like charting.

# ============================================
# 2. EXAMPLE
# ============================================

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [10, 20, 15])
plt.title("My First Plot")
plt.savefig("plot_intro.png")
print("Saved plot_intro.png")

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Install matplotlib and confirm the version with matplotlib.__version__.
# EXERCISE 2 (easy): Plot a simple list of numbers and save it as a PNG.
# EXERCISE 3 (easy): Add a title to a plot using plt.title().
# EXERCISE 4 (medium): Explain (via prints) the role of the pyplot module.
# EXERCISE 5 (medium): Create and save two separate plots in the same script.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `save_line_plot(x, y, filename)` that creates and saves a labeled line plot for any given data.


# ============================================
# 5. SUMMARY
# ============================================
# Matplotlib is the base plotting library most other Python visualization tools build on.
