"""
Topic: Data Types
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Python has built-in types: str, int, float, bool, list, tuple, dict, set, and more. Use type() to inspect a value's type.

# ============================================
# 2. EXAMPLE
# ============================================

values = ["text", 10, 3.14, True, [1, 2], (1, 2), {"a": 1}, {1, 2}]
for value in values:
    print(value, "->", type(value).__name__)

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Print the type of 5 different literals (string, int, float, bool, list).
# EXERCISE 2 (easy): Create one variable of each basic type and print them all.
# EXERCISE 3 (easy): Use isinstance() to check if a variable is an int.
# EXERCISE 4 (medium): Write a program that classifies a list of mixed values by type into a dictionary of counts.
# EXERCISE 5 (medium): Explain (via print statements) the difference between int and float using two examples.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that takes any value and returns a human-readable description of its type and value.


# ============================================
# 5. SUMMARY
# ============================================
# Knowing Python's core data types is the foundation for every data structure you will use later.
