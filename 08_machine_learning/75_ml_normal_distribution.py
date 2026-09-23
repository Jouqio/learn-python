"""
Topic: Normal Distribution
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# The normal (Gaussian) distribution is a common bell-shaped distribution defined by its mean and standard deviation.

# ============================================
# 2. EXAMPLE
# ============================================

import numpy as np

normal_data = np.random.default_rng(1).normal(loc=5.0, scale=1.0, size=1000)
print("Mean approx:", round(np.mean(normal_data), 2))
print("Std approx:", round(np.std(normal_data), 2))

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Generate 500 values from a normal distribution with mean=0, std=1.
# EXERCISE 2 (easy): Plot a histogram of normally distributed data.
# EXERCISE 3 (easy): Explain the 68-95-99.7 rule in your own words.
# EXERCISE 4 (medium): Generate two normal distributions with different means and compare them visually.
# EXERCISE 5 (medium): Check how close the sample mean/std get to the true parameters as sample size grows.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that generates normal data and reports what percentage of values fall within 1 standard deviation of the mean.


# ============================================
# 5. SUMMARY
# ============================================
# Many natural and measurement processes approximate a normal distribution, making it central to statistics and ML.
