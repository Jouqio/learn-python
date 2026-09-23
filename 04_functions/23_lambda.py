"""
Topic: Lambda Functions
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Lambda functions are small, anonymous, single-expression functions, often used with sorted(), map(), and filter().

# ============================================
# 2. EXAMPLE
# ============================================

square = lambda x: x ** 2
print(square(5))

numbers = [5, 2, 8, 1, 9]
print(sorted(numbers, key=lambda n: -n))
print(list(filter(lambda n: n % 2 == 0, numbers)))

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Write a lambda that doubles a number.
# EXERCISE 2 (easy): Sort a list of tuples by their second element using a lambda key.
# EXERCISE 3 (easy): Use map() with a lambda to convert a list of strings to uppercase.
# EXERCISE 4 (medium): Use filter() with a lambda to keep only positive numbers.
# EXERCISE 5 (medium): Compare a lambda and an equivalent def function for the same logic.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Sort a list of dictionaries (representing products) by price using a lambda key function.


# ============================================
# 5. SUMMARY
# ============================================
# Lambdas are best for short, throwaway functions; use def for anything more complex.
