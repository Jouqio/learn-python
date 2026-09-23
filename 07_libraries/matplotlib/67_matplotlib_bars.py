"""
Topic: Bar Charts
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# plt.bar() (vertical) and plt.barh() (horizontal) compare quantities across categories.

# ============================================
# 2. EXAMPLE
# ============================================

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

categories = ["A", "B", "C"]
values = [3, 7, 5]
plt.bar(categories, values)
plt.savefig("plot_bars.png")
print("Saved plot_bars.png")

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Create a vertical bar chart from category labels and values.
# EXERCISE 2 (easy): Create a horizontal bar chart using plt.barh().
# EXERCISE 3 (easy): Change the bar color and width.
# EXERCISE 4 (medium): Add value labels above each bar.
# EXERCISE 5 (medium): Create a grouped bar chart comparing two series across the same categories.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that creates a bar chart comparing monthly sales for two years, side-by-side per month.


# ============================================
# 5. SUMMARY
# ============================================
# Bar charts are the clearest way to compare discrete category totals at a glance.
