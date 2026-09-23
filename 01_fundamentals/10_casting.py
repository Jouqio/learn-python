"""
Topic: Type Casting
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Casting converts a value from one type to another using int(), float(), str(), bool(), etc.

# ============================================
# 2. EXAMPLE
# ============================================

age_text = "25"
age_number = int(age_text)
print(age_number + 5)
print(str(age_number) + " years old")

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Convert the string '42' to an int and add 8 to it.
# EXERCISE 2 (easy): Convert a float to a string and concatenate it with text.
# EXERCISE 3 (easy): Convert '3.14' to a float, then to an int, and print both results.
# EXERCISE 4 (medium): Write code that safely casts user input to int using try/except.
# EXERCISE 5 (medium): Cast a list of number-strings into a list of ints using a loop.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `safe_int(value, default=0)` that tries to cast to int and returns a default if casting fails.


# ============================================
# 5. SUMMARY
# ============================================
# Casting bridges Python's dynamic types; always validate input before casting to avoid crashes.
