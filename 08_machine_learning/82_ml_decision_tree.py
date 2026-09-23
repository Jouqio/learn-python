"""
Topic: Decision Tree
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# A decision tree splits data on feature thresholds to make a series of yes/no decisions leading to a prediction.

# ============================================
# 2. EXAMPLE
# ============================================

from sklearn.tree import DecisionTreeClassifier

X = [[25, 1], [45, 0], [35, 1], [23, 0], [50, 1]]  # [age, has_experience]
y = [0, 1, 1, 0, 1]  # hired or not

model = DecisionTreeClassifier(random_state=0)
model.fit(X, y)
print("Prediction for [30, 1]:", model.predict([[30, 1]]))

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Train a decision tree classifier on a small labeled dataset.
# EXERCISE 2 (easy): Predict the class for a new, unseen data point.
# EXERCISE 3 (easy): Print the tree's feature importances.
# EXERCISE 4 (medium): Limit the tree depth using max_depth and observe the effect on predictions.
# EXERCISE 5 (medium): Explain (as prints) why deep, unrestricted trees tend to overfit.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that trains a decision tree on a given dataset and reports both training accuracy and test accuracy.


# ============================================
# 5. SUMMARY
# ============================================
# Decision trees are interpretable models that split data step by step based on feature values.
