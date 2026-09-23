"""
Topic: Line Styles
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Line style, width, and color can all be customized (linestyle, linewidth, color).

# ============================================
# 2. EXAMPLE
# ============================================

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], linestyle="dashed", color="red", linewidth=2)
plt.savefig("plot_line.png")
print("Saved plot_line.png")

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Plot a dashed line.
# EXERCISE 2 (easy): Plot a line with a custom color.
# EXERCISE 3 (easy): Plot a line with increased width.
# EXERCISE 4 (medium): Combine linestyle, color, and linewidth in one plot call.
# EXERCISE 5 (medium): Plot two lines with different styles on the same chart to compare them.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that plots actual vs predicted values using two distinct line styles for easy comparison.


# ============================================
# 5. SUMMARY
# ============================================
# Line style customization makes multi-series charts easier to read and compare.
