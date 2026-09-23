"""
Topic: Grid Search (Hyperparameter Tuning)
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Grid search systematically tries combinations of hyperparameters to find the best-performing configuration.

# ============================================
# 2. EXAMPLE
# ============================================

from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier

X = [[25, 1], [45, 0], [35, 1], [23, 0], [50, 1], [40, 0]]
y = [0, 1, 1, 0, 1, 0]

param_grid = {"max_depth": [1, 2, 3], "criterion": ["gini", "entropy"]}
search = GridSearchCV(DecisionTreeClassifier(random_state=0), param_grid, cv=3)
search.fit(X, y)
print("Best params:", search.best_params_)

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Run a grid search over 2 hyperparameters for a decision tree.
# EXERCISE 2 (easy): Print the best combination of hyperparameters found.
# EXERCISE 3 (easy): Print the best cross-validated score achieved.
# EXERCISE 4 (medium): Add a third hyperparameter to the search grid.
# EXERCISE 5 (medium): Explain (as prints) why grid search can be computationally expensive.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `tune_model(model, param_grid, X, y)` that runs GridSearchCV and returns the best estimator.


# ============================================
# 5. SUMMARY
# ============================================
# Grid search automates the tedious trial-and-error of hyperparameter tuning using cross-validation.
