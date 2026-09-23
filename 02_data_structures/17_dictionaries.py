"""
Topic: Dictionaries
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Dictionaries store key-value pairs. Keys must be unique and hashable; values can be any type.

# ============================================
# 2. EXAMPLE
# ============================================

student = {"name": "Bagas", "age": 22, "major": "Computer Science"}
student["gpa"] = 3.7
for key, value in student.items():
    print(f"{key}: {value}")

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Create a dictionary describing a book (title, author, year).
# EXERCISE 2 (easy): Update a value in a dictionary and add a new key.
# EXERCISE 3 (easy): Loop over a dictionary's keys, values, and items separately.
# EXERCISE 4 (medium): Use .get() with a default value to avoid a KeyError.
# EXERCISE 5 (medium): Merge two dictionaries into one.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that counts word frequency in a sentence using a dictionary.


# ============================================
# 5. SUMMARY
# ============================================
# Dictionaries are Python's core key-value structure and power much of real-world data handling.
