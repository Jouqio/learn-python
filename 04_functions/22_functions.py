"""
Topic: Functions
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Functions group reusable code, accept parameters (including defaults and keyword args), and return values.

# ============================================
# 2. EXAMPLE
# ============================================

def calculate_total(price, quantity, discount=0.0):
    subtotal = price * quantity
    return subtotal - (subtotal * discount)

print(calculate_total(50000, 3))
print(calculate_total(50000, 3, discount=0.1))

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Write a function that adds two numbers and returns the result.
# EXERCISE 2 (easy): Write a function with a default parameter value.
# EXERCISE 3 (easy): Write a function that accepts keyword arguments explicitly.
# EXERCISE 4 (medium): Write a function using *args to sum any number of numbers.
# EXERCISE 5 (medium): Write a function using **kwargs to print all key-value pairs passed in.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `build_receipt(items)` where items is a list of (name, price, qty) tuples, returning a formatted receipt string.


# ============================================
# 5. SUMMARY
# ============================================
# Functions with clear names, single responsibilities, and defaults make code reusable and readable.
