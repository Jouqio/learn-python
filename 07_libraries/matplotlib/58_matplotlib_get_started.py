"""
Topic: Matplotlib Getting Started
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# A typical matplotlib workflow: import pyplot, plot data, customize, then show or save the figure.

# ============================================
# 2. EXAMPLE
# ============================================

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
plt.plot(x, y)
plt.savefig("plot_get_started.png")
print("Saved plot_get_started.png")

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Create x and y lists and plot them.
# EXERCISE 2 (easy): Save the figure instead of displaying it interactively.
# EXERCISE 3 (easy): Plot two different datasets in two separate saved images.
# EXERCISE 4 (medium): Explain when to use plt.show() vs plt.savefig().
# EXERCISE 5 (medium): Clear a figure with plt.clf() between two separate plots in one script.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a script that generates and saves 3 plots for 3 different simple datasets, named plot_1.png, plot_2.png, plot_3.png.


# ============================================
# 5. SUMMARY
# ============================================
# A consistent plot-customize-save workflow keeps matplotlib scripts predictable and reusable.
