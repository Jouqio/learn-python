"""
Topic: Bootstrap Aggregation (Bagging)
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Bagging trains many models on random resampled subsets of data and averages their predictions to reduce overfitting.

# ============================================
# 2. EXAMPLE
# ============================================

from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

X = [[25, 1], [45, 0], [35, 1], [23, 0], [50, 1], [40, 0], [60, 1], [22, 0]]
y = [0, 1, 1, 0, 1, 0, 1, 0]

model = BaggingClassifier(DecisionTreeClassifier(), n_estimators=10, random_state=0)
model.fit(X, y)
print("Prediction for [30, 1]:", model.predict([[30, 1]]))

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Train a BaggingClassifier with 10 base estimators.
# EXERCISE 2 (easy): Compare predictions from a single decision tree vs the bagged ensemble.
# EXERCISE 3 (easy): Increase n_estimators and observe if predictions/scores change.
# EXERCISE 4 (medium): Explain (as prints) how bagging reduces variance compared to one tree.
# EXERCISE 5 (medium): Try RandomForestClassifier, which is bagging + random feature selection, and compare results.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that compares the cross-validated accuracy of a single DecisionTreeClassifier vs a BaggingClassifier on the same data.


# ============================================
# 5. SUMMARY
# ============================================
# Bagging combines many 'weak' models trained on resampled data into one more stable, less overfit prediction.
