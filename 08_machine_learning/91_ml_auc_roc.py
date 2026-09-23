"""
Topic: AUC - ROC Curve
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# The ROC curve plots true positive rate vs false positive rate across thresholds; AUC summarizes overall classifier quality as one number.

# ============================================
# 2. EXAMPLE
# ============================================

from sklearn.metrics import roc_auc_score
import numpy as np

y_true = [0, 0, 1, 1, 0, 1, 1, 0]
y_scores = [0.1, 0.4, 0.35, 0.8, 0.2, 0.7, 0.65, 0.3]

auc = roc_auc_score(y_true, y_scores)
print("AUC score:", round(auc, 3))

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Compute the AUC score for a small set of true labels and predicted probabilities.
# EXERCISE 2 (easy): Explain what an AUC of 0.5 vs 1.0 means.
# EXERCISE 3 (easy): Plot the ROC curve using sklearn.metrics.roc_curve and matplotlib.
# EXERCISE 4 (medium): Compare AUC for two different models on the same test data.
# EXERCISE 5 (medium): Explain (as prints) why AUC is useful even when classes are imbalanced.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `compare_models_auc(models, X_test, y_test)` that returns each model's AUC score for comparison.


# ============================================
# 5. SUMMARY
# ============================================
# AUC-ROC gives a threshold-independent summary of how well a classifier separates the two classes.
