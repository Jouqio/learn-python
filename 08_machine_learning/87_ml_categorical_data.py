"""
Topic: Categorical Data
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Categorical (non-numeric) features must be encoded into numbers before most ML algorithms can use them.

# ============================================
# 2. EXAMPLE
# ============================================

import pandas as pd

df = pd.DataFrame({"color": ["red", "blue", "green", "blue"]})
one_hot = pd.get_dummies(df, columns=["color"])
print(one_hot)

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): One-hot encode a categorical column with 3 categories.
# EXERCISE 2 (easy): Use pandas.Categorical to assign an explicit category order (ordinal encoding).
# EXERCISE 3 (easy): Compare one-hot encoding with simple label encoding.
# EXERCISE 4 (medium): Explain why label encoding can mislead a model into assuming order that doesn't exist.
# EXERCISE 5 (medium): Encode a categorical column using sklearn's OneHotEncoder instead of pandas.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `encode_categorical(df, column)` that one-hot encodes a given column and returns the updated DataFrame.


# ============================================
# 5. SUMMARY
# ============================================
# Categorical encoding translates human-readable labels into numeric form models can actually learn from.
