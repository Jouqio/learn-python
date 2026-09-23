"""
Topic: K-Nearest Neighbors (KNN)
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# KNN classifies a new point based on the majority class among its k closest neighbors in the training data.

# ============================================
# 2. EXAMPLE
# ============================================

from sklearn.neighbors import KNeighborsClassifier

X = [[4, 21], [5, 19], [10, 24], [4, 17], [3, 16], [11, 25]]
y = [0, 0, 1, 0, 0, 1]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)
print("Prediction for [8, 21]:", model.predict([[8, 21]]))

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Train a KNN classifier with k=3 on a small dataset.
# EXERCISE 2 (easy): Predict the class of a new point.
# EXERCISE 3 (easy): Try k=1 and k=5 and compare predictions.
# EXERCISE 4 (medium): Explain (as prints) why feature scaling matters a lot for KNN specifically.
# EXERCISE 5 (medium): Plot the training points colored by class, with the new point marked distinctly.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `find_best_k(X, y, X_test, y_test, k_range)` that tries several k values and returns the one with the best test accuracy.


# ============================================
# 5. SUMMARY
# ============================================
# KNN is a simple, intuitive 'learn by comparison' algorithm, but it can be slow and scaling-sensitive on large datasets.
