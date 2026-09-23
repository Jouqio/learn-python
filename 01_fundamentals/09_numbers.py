"""
Topic: Numbers (int, float, complex)
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Python supports int, float, and complex numbers, plus arithmetic operators and functions like round(), abs(), and pow().

# ============================================
# 2. EXAMPLE
# ============================================

price = 19.999
quantity = 3
total = round(price * quantity, 2)
print(f"Total: {total}")
print(abs(-total), pow(2, 10))

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Round 3.14159 to 2 decimal places.
# EXERCISE 2 (easy): Compute the absolute value of -42.
# EXERCISE 3 (easy): Compute 2 to the power of 8 using pow() and using **.
# EXERCISE 4 (medium): Convert a float to int and observe truncation behavior.
# EXERCISE 5 (medium): Write a program that calculates compound interest using floats.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a simple currency rounding utility that always rounds to 2 decimal places and never produces floating point artifacts visibly (use round() correctly).


# ============================================
# 5. SUMMARY
# ============================================
# Numbers in Python come in a few flavors; float precision quirks are common, so round() and formatting matter.
