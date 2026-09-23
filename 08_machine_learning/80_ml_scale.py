"""
Topic: Feature Scaling
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Scaling (e.g. StandardScaler) normalizes features to comparable ranges, which many ML algorithms require to perform well.

# ============================================
# 2. EXAMPLE
# ============================================

from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.array([[0.9, 1600], [1.4, 1900], [2.0, 2200], [1.2, 1700]])
scaler = StandardScaler()
scaled_X = scaler.fit_transform(X)
print("Scaled features:\n", scaled_X)

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Scale a small 2-column dataset with StandardScaler.
# EXERCISE 2 (easy): Print the mean and scale (std) learned by the scaler.
# EXERCISE 3 (easy): Scale a new data point using the already-fitted scaler.
# EXERCISE 4 (medium): Explain why features with very different ranges can bias some models.
# EXERCISE 5 (medium): Compare StandardScaler with MinMaxScaler on the same data.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that scales training data and applies the same transformation to new incoming data (fit on train, transform on both).


# ============================================
# 5. SUMMARY
# ============================================
# Scaling puts features on comparable footing so no single feature dominates a model just due to its numeric range.
