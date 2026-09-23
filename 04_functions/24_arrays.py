"""
Topic: Arrays (via list / array module)
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Python's built-in 'array' is really the list type for general use; the `array` module provides typed arrays for numeric data.

# ============================================
# 2. EXAMPLE
# ============================================

from array import array

numbers = array("i", [1, 2, 3, 4, 5])
numbers.append(6)
print(numbers, numbers[2])
print(sum(numbers) / len(numbers))

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Create a typed array of floats and print its sum.
# EXERCISE 2 (easy): Access and modify an element by index in an array.
# EXERCISE 3 (easy): Convert an array to a regular list.
# EXERCISE 4 (medium): Compare memory efficiency conceptually between array and list (explain in prints, no need to measure).
# EXERCISE 5 (medium): Loop through an array and print each element with its index.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that computes the average of an array of integers without using sum().


# ============================================
# 5. SUMMARY
# ============================================
# For most everyday tasks, Python lists are used as 'arrays'; the array module is for compact typed numeric storage.
