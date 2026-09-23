"""
Topic: Booleans
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Booleans (True/False) represent truth values and result from comparisons. Most objects have a truthiness value.

# ============================================
# 2. EXAMPLE
# ============================================

is_logged_in = True
has_permission = False
print(is_logged_in and has_permission)
print(bool(""), bool("text"), bool(0), bool([1]))

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Print the result of 5 > 3 and 2 == 2.
# EXERCISE 2 (easy): Check the truthiness of an empty list vs a non-empty list.
# EXERCISE 3 (easy): Combine two boolean variables with `and`, `or`, and `not`.
# EXERCISE 4 (medium): Write an expression that evaluates to True only if a number is between 1 and 10.
# EXERCISE 5 (medium): Write a function returning True/False for whether a year is a leap year.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `can_vote(age, is_citizen)` that returns a boolean using proper boolean logic (no magic numbers).


# ============================================
# 5. SUMMARY
# ============================================
# Booleans drive decision-making in Python; understanding truthiness avoids subtle bugs.
