"""
Topic: Multiple Regression
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Multiple regression predicts one target using two or more input features.

# ============================================
# 2. EXAMPLE
# ============================================

# pip install scikit-learn
from sklearn import linear_model

X = [[0.9, 1600], [1.4, 1900], [2.0, 2200], [1.2, 1700]]  # [engine_size, weight]
y = [95, 110, 140, 100]  # CO2 emissions

model = linear_model.LinearRegression()
model.fit(X, y)
print("Coefficients:", model.coef_)
print("Prediction for [1.6, 1800]:", model.predict([[1.6, 1800]]))

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Fit a multiple regression model with 2 input features.
# EXERCISE 2 (easy): Print the model's coefficients and interpret their sign.
# EXERCISE 3 (easy): Predict a target value for a new set of feature inputs.
# EXERCISE 4 (medium): Add a third feature and refit the model.
# EXERCISE 5 (medium): Compare predictions before and after adding the third feature.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `fit_and_predict(X_train, y_train, X_new)` wrapping sklearn's LinearRegression for reuse.


# ============================================
# 5. SUMMARY
# ============================================
# Multiple regression extends linear regression to combine several features into one prediction.
