"""
Topic: Labels and Titles
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# xlabel, ylabel, and title annotate a chart so it's understandable without extra explanation.

# ============================================
# 2. EXAMPLE
# ============================================

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [10, 20, 25])
plt.title("Monthly Growth")
plt.xlabel("Month")
plt.ylabel("Growth (%)")
plt.savefig("plot_labels.png")
print("Saved plot_labels.png")

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Add a title to a chart.
# EXERCISE 2 (easy): Add x and y axis labels.
# EXERCISE 3 (easy): Change the font size of the title.
# EXERCISE 4 (medium): Add a legend describing what the line represents.
# EXERCISE 5 (medium): Position the title with custom padding.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `labeled_plot(x, y, title, xlabel, ylabel)` that returns a fully-labeled saved chart file.


# ============================================
# 5. SUMMARY
# ============================================
# Clear labels and titles turn a plain chart into a self-explanatory visualization.
