"""
Topic: Histograms
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# plt.hist() shows the distribution of a numeric dataset by grouping values into bins.

# ============================================
# 2. EXAMPLE
# ============================================

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

data = np.random.default_rng(1).normal(loc=70, scale=10, size=200)
plt.hist(data, bins=15)
plt.savefig("plot_histogram.png")
print("Saved plot_histogram.png")

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Create a histogram from a list of 20 numbers.
# EXERCISE 2 (easy): Change the number of bins and observe the effect.
# EXERCISE 3 (easy): Add axis labels describing what's being measured.
# EXERCISE 4 (medium): Overlay two histograms with transparency (alpha) to compare distributions.
# EXERCISE 5 (medium): Add a vertical line marking the mean using plt.axvline().
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that plots a histogram of exam scores and marks the passing threshold with a vertical line.


# ============================================
# 5. SUMMARY
# ============================================
# Histograms reveal the shape (spread, skew, peaks) of a numeric dataset's distribution.
