"""
Topic: Pie Charts
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# plt.pie() shows proportions of a whole as wedge-shaped slices.

# ============================================
# 2. EXAMPLE
# ============================================

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

labels = ["Rent", "Food", "Transport", "Savings"]
sizes = [40, 25, 15, 20]
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.savefig("plot_pie.png")
print("Saved plot_pie.png")

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Create a pie chart from 4 category values.
# EXERCISE 2 (easy): Show percentage labels on each slice using autopct.
# EXERCISE 3 (easy): Explode one slice to highlight it using the explode parameter.
# EXERCISE 4 (medium): Add a legend alongside the pie chart.
# EXERCISE 5 (medium): Change the color palette of the pie slices.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `budget_pie_chart(categories, amounts, filename)` that saves a labeled, percentage-annotated pie chart for any budget breakdown.


# ============================================
# 5. SUMMARY
# ============================================
# Pie charts work best for a small number of categories that clearly sum to a meaningful whole.
