"""
Topic: Logistic Regression
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Logistic regression predicts the probability of a binary outcome using a sigmoid-shaped curve.

# ============================================
# 2. EXAMPLE
# ============================================

from sklearn.linear_model import LogisticRegression
import numpy as np

hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
passed = [0, 0, 0, 1, 1, 1, 1, 1]

model = LogisticRegression()
model.fit(hours_studied, passed)
print("Probability of passing at 3.5 hours:", model.predict_proba([[3.5]])[0][1])

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Fit a logistic regression model on a small pass/fail dataset.
# EXERCISE 2 (easy): Predict the probability (not just the class) for a new input.
# EXERCISE 3 (easy): Predict the class label directly using .predict().
# EXERCISE 4 (medium): Explain why logistic regression outputs are probabilities, not raw scores.
# EXERCISE 5 (medium): Plot the sigmoid-shaped predicted probability curve over a range of x values.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `predict_pass_probability(hours, hours_data, results_data)` returning the probability of passing for given study hours.


# ============================================
# 5. SUMMARY
# ============================================
# Logistic regression is the standard baseline for binary classification problems.
