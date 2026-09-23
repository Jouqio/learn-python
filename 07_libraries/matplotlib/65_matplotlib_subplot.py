"""
Topic: Subplots
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# plt.subplot() / plt.subplots() place multiple charts within one figure.

# ============================================
# 2. EXAMPLE
# ============================================

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2)
axes[0].plot([1, 2, 3], [1, 2, 3])
axes[1].plot([1, 2, 3], [3, 2, 1])
fig.savefig("plot_subplot.png")
print("Saved plot_subplot.png")

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Create a figure with 2 side-by-side subplots.
# EXERCISE 2 (easy): Create a figure with a 2x2 grid of subplots.
# EXERCISE 3 (easy): Give each subplot its own title.
# EXERCISE 4 (medium): Share the y-axis between two subplots using sharey=True.
# EXERCISE 5 (medium): Adjust spacing between subplots using plt.tight_layout().
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that plots 4 related datasets as a 2x2 dashboard of subplots in one saved image.


# ============================================
# 5. SUMMARY
# ============================================
# Subplots let you compare multiple related charts within a single figure.
