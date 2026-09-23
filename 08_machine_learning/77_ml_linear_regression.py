"""
Topic: Linear Regression
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Linear regression fits a straight line (y = mx + b) that best predicts y from x.

# ============================================
# 2. EXAMPLE
# ============================================

from scipy import stats

hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [50, 55, 65, 70, 72, 80, 88, 92]

slope, intercept, r, p, std_err = stats.linregress(hours, scores)
predicted = slope * 6.5 + intercept
print(f"y = {slope:.2f}x + {intercept:.2f}, r={r:.3f}")
print("Predicted score for 6.5 hours studied:", round(predicted, 1))

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Fit a linear regression on a small custom dataset.
# EXERCISE 2 (easy): Print the slope and intercept of the fitted line.
# EXERCISE 3 (easy): Predict a new y value for an x not in the original data.
# EXERCISE 4 (medium): Interpret the r value (correlation coefficient) in your own words.
# EXERCISE 5 (medium): Plot the original points and the fitted regression line together.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `predict_score(hours_studied, hours_data, scores_data)` that fits a regression and returns a prediction.


# ============================================
# 5. SUMMARY
# ============================================
# Linear regression is the simplest predictive model, mapping one numeric input to one numeric output via a straight line.
