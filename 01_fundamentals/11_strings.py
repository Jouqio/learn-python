"""
Topic: Strings
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Strings are immutable sequences of characters. They support slicing, methods like .upper(), .strip(), .split(), and f-string formatting.

# ============================================
# 2. EXAMPLE
# ============================================

greeting = "  Hello, Python learners!  "
print(greeting.strip().upper())
print(greeting.strip().split(","))
name = "Rafi"
print(f"Hi, {name}! Your name has {len(name)} letters.")

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Reverse a string using slicing.
# EXERCISE 2 (easy): Count how many times a letter appears in a string using .count().
# EXERCISE 3 (easy): Split a sentence into words and print the word count.
# EXERCISE 4 (medium): Check if a string starts and ends with specific characters using .startswith()/.endswith().
# EXERCISE 5 (medium): Build a formatted report line using an f-string with at least 2 variables.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that checks if a string is a palindrome, ignoring case and spaces.


# ============================================
# 5. SUMMARY
# ============================================
# Strings are one of the most-used types in Python; mastering slicing and string methods pays off constantly.
