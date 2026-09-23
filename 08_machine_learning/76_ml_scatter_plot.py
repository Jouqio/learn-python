"""
Topic: Scatter Plot for ML
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Scatter plots reveal whether two variables have a linear, non-linear, or no visible relationship before modeling.

# ============================================
# 2. EXAMPLE
# ============================================

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

hours_studied = [1, 2, 3, 4, 5, 6, 7, 8]
exam_score = [50, 55, 65, 70, 72, 80, 88, 92]
plt.scatter(hours_studied, exam_score)
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.savefig("ml_scatter.png")
print("Saved ml_scatter.png")

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Plot hours studied vs exam score for 8 students.
# EXERCISE 2 (easy): Add axis labels describing each variable clearly.
# EXERCISE 3 (easy): Visually judge (via a comment) whether the relationship looks linear.
# EXERCISE 4 (medium): Add a second dataset (a different class) to the same scatter plot.
# EXERCISE 5 (medium): Color points by a pass/fail threshold.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that scatter-plots two numeric columns from a small dataset and saves the chart with labeled axes.


# ============================================
# 5. SUMMARY
# ============================================
# Scatter plots are the essential first step before choosing a regression or classification approach.
