"""
Topic: Train/Test Split
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Splitting data into training and test sets lets you evaluate a model on data it hasn't seen.

# ============================================
# 2. EXAMPLE
# ============================================

from sklearn.model_selection import train_test_split
import numpy as np

X = np.arange(20).reshape(-1, 1)
y = np.arange(20) * 2

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)
print("Train size:", len(X_train), "| Test size:", len(X_test))

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Split a dataset into 80% train / 20% test.
# EXERCISE 2 (easy): Set a random_state and confirm the split is reproducible.
# EXERCISE 3 (easy): Explain why testing on the training data gives a misleadingly good score.
# EXERCISE 4 (medium): Try a different test_size and observe how train/test sizes change.
# EXERCISE 5 (medium): Split a dataset with a target column into features (X) and labels (y) before splitting.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `evaluate_split(model, X, y, test_size=0.2)` that splits data, fits the model, and returns its test-set score.


# ============================================
# 5. SUMMARY
# ============================================
# Train/test splitting is essential to honestly measure how well a model generalizes to unseen data.
