"""
Topic: Data Distribution
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Real datasets are often simulated or sampled from a distribution to test statistical methods before using real data.

# ============================================
# 2. EXAMPLE
# ============================================

import numpy as np

uniform_data = np.random.default_rng(0).uniform(0.0, 5.0, 250)
print("Sample mean:", round(np.mean(uniform_data), 3))
print("Sample min/max:", round(uniform_data.min(), 2), round(uniform_data.max(), 2))

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Generate 100 random uniform values between 0 and 10.
# EXERCISE 2 (easy): Compute the mean and range of the generated data.
# EXERCISE 3 (easy): Plot a histogram of the distribution (reuse matplotlib skills).
# EXERCISE 4 (medium): Generate two different distributions and compare their spreads.
# EXERCISE 5 (medium): Explain what 'random but reproducible' means using a random seed.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that generates n random samples from a uniform distribution and returns basic summary statistics as a dictionary.


# ============================================
# 5. SUMMARY
# ============================================
# Simulated data distributions let you practice statistics and ML techniques before working with real datasets.
