"""
Topic: Lists
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Lists are ordered, mutable collections. Support indexing, slicing, append/remove, and list comprehensions.

# ============================================
# 2. EXAMPLE
# ============================================

fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits.remove("banana")
print(fruits)
squares = [n ** 2 for n in range(1, 6)]
print(squares)

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Create a list of 5 numbers and print the sum using sum().
# EXERCISE 2 (easy): Add and remove an item from a list.
# EXERCISE 3 (easy): Sort a list of names alphabetically.
# EXERCISE 4 (medium): Use a list comprehension to filter even numbers from a range.
# EXERCISE 5 (medium): Reverse a list without using reverse().
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that removes duplicates from a list while preserving order.


# ============================================
# 5. SUMMARY
# ============================================
# Lists are the most common mutable sequence in Python; comprehensions make transformations concise.
