"""
Topic: Regular Expressions
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# The re module matches text patterns: validation, searching, and substitution.

# ============================================
# 2. EXAMPLE
# ============================================

import re

text = "Contact: budi@email.com or 0812-3456-7890"
emails = re.findall(r"[\w.]+@[\w.]+", text)
print(emails)
cleaned = re.sub(r"\d", "#", text)
print(cleaned)

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Match a simple email pattern in a string.
# EXERCISE 2 (easy): Validate whether a string is a 5-digit number using re.fullmatch.
# EXERCISE 3 (easy): Replace all digits in a string with '#' using re.sub.
# EXERCISE 4 (medium): Split a sentence on multiple delimiters (comma, semicolon) using re.split.
# EXERCISE 5 (medium): Extract all hashtags from a sample social media caption.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that validates an Indonesian phone number format like 08xx-xxxx-xxxx using a regex.


# ============================================
# 5. SUMMARY
# ============================================
# Regex is powerful for pattern-based text processing but should be used carefully and tested well.
