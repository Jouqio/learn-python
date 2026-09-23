"""
Topic: Tuples
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Tuples are ordered, immutable collections, often used for fixed groups of values or unpacking.

# ============================================
# 2. EXAMPLE
# ============================================

coordinates = (10, 20)
x, y = coordinates
print(f"x={x}, y={y}")
person = ("Dewi", 30, "Engineer")
print(person[1])

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Create a tuple with 3 values and unpack it into 3 variables.
# EXERCISE 2 (easy): Try to modify a tuple element and observe the error.
# EXERCISE 3 (easy): Convert a tuple to a list, modify it, then convert back.
# EXERCISE 4 (medium): Return multiple values from a function as a tuple.
# EXERCISE 5 (medium): Use tuple unpacking inside a for loop over a list of tuples.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that returns (min, max, average) of a list of numbers as a tuple.


# ============================================
# 5. SUMMARY
# ============================================
# Tuples signal 'this data shouldn't change' and are handy for multiple return values.
