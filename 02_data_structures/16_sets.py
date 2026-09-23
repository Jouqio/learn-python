"""
Topic: Sets
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Sets are unordered collections of unique items, useful for membership tests and set algebra (union, intersection).

# ============================================
# 2. EXAMPLE
# ============================================

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b, a & b, a - b)
a.add(10)
print(a)

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Remove duplicates from a list using a set.
# EXERCISE 2 (easy): Find the intersection of two sets of student names.
# EXERCISE 3 (easy): Check membership of a value in a set with `in`.
# EXERCISE 4 (medium): Add and discard elements from a set.
# EXERCISE 5 (medium): Find items that are in set A but not in set B.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that, given two lists of email addresses, returns the ones that appear in both.


# ============================================
# 5. SUMMARY
# ============================================
# Sets are ideal for uniqueness checks and comparing collections quickly.
