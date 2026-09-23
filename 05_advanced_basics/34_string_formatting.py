"""
Topic: String Formatting
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Python offers f-strings, .format(), and %-formatting; f-strings are the modern, preferred style.

# ============================================
# 2. EXAMPLE
# ============================================

name = "Fajar"
score = 87.5
print(f"{name} scored {score:.1f} points")
print("{} scored {:.1f} points".format(name, score))
print("%s scored %.1f points" % (name, score))

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Format a float to 2 decimal places using an f-string.
# EXERCISE 2 (easy): Pad a number with leading zeros using an f-string (e.g. 007).
# EXERCISE 3 (easy): Right-align and left-align text within a fixed width using f-strings.
# EXERCISE 4 (medium): Format a number with thousands separators (e.g. 1,000,000).
# EXERCISE 5 (medium): Compare the same output built with f-string, .format(), and % styles.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that formats a currency amount as 'Rp 1.234.567' style output.


# ============================================
# 5. SUMMARY
# ============================================
# f-strings are the clearest, fastest, and most Pythonic way to format strings today.
