"""
Topic: The Pyplot Module
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# pyplot provides a stateful, function-based interface (plt.plot, plt.xlabel, etc.) for building charts step by step.

# ============================================
# 2. EXAMPLE
# ============================================

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.xlabel("Index")
plt.ylabel("Value")
plt.savefig("plot_pyplot.png")
print("Saved plot_pyplot.png")

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Plot a list of values without specifying x (Matplotlib auto-generates indices).
# EXERCISE 2 (easy): Add xlabel and ylabel to a chart.
# EXERCISE 3 (easy): Chain multiple pyplot calls to build one figure step by step.
# EXERCISE 4 (medium): Explain (via prints) what 'state-based' plotting means.
# EXERCISE 5 (medium): Create a figure with 2 lines on the same axes using two plt.plot() calls.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `quick_plot(y_values, ylabel)` that plots values against their index with a labeled y-axis.


# ============================================
# 5. SUMMARY
# ============================================
# pyplot's step-by-step function calls make it quick to build charts without much boilerplate.
