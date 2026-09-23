"""
Topic: Confusion Matrix
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# A confusion matrix summarizes classification results as true/false positives and negatives.

# ============================================
# 2. EXAMPLE
# ============================================

from sklearn.metrics import confusion_matrix, accuracy_score

y_true = [1, 0, 1, 1, 0, 1, 0, 0]
y_pred = [1, 0, 0, 1, 0, 1, 1, 0]

matrix = confusion_matrix(y_true, y_pred)
print("Confusion Matrix:\n", matrix)
print("Accuracy:", accuracy_score(y_true, y_pred))

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Build a confusion matrix from a small list of true/predicted labels.
# EXERCISE 2 (easy): Compute accuracy manually from the confusion matrix values.
# EXERCISE 3 (easy): Compute precision and recall using sklearn.metrics.
# EXERCISE 4 (medium): Explain the difference between a false positive and a false negative.
# EXERCISE 5 (medium): Visualize a confusion matrix using ConfusionMatrixDisplay and save it as an image.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `classification_report_summary(y_true, y_pred)` returning accuracy, precision, and recall in one dictionary.


# ============================================
# 5. SUMMARY
# ============================================
# A confusion matrix reveals what kind of mistakes a classifier makes, not just how often it's right.
