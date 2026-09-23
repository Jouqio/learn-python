"""
Topic: Cross Validation
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Cross-validation repeatedly splits data into folds to get a more reliable estimate of model performance than a single train/test split.

# ============================================
# 2. EXAMPLE
# ============================================

from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
import numpy as np

X = np.random.default_rng(0).random((30, 2))
y = np.random.default_rng(1).integers(0, 2, 30)

scores = cross_val_score(DecisionTreeClassifier(random_state=0), X, y, cv=5)
print("Fold scores:", scores)
print("Average score:", scores.mean())

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Run 5-fold cross-validation on a decision tree.
# EXERCISE 2 (easy): Print the mean and standard deviation of the fold scores.
# EXERCISE 3 (easy): Try 10-fold cross-validation and compare the average score.
# EXERCISE 4 (medium): Explain (as prints) why cross-validation gives a more trustworthy score than one split.
# EXERCISE 5 (medium): Apply cross-validation to a different model (e.g. LogisticRegression) on the same data.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `cross_validate_model(model, X, y, folds=5)` returning the mean and std of cross-validation scores.


# ============================================
# 5. SUMMARY
# ============================================
# Cross-validation reduces the risk that a single lucky (or unlucky) train/test split misleads your model evaluation.
