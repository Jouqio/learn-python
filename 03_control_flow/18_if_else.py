"""
Topic: If...Else
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Conditional statements (if/elif/else) run different code blocks based on boolean conditions.

# ============================================
# 2. EXAMPLE
# ============================================

score = 78
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
else:
    grade = "C"
print(f"Grade: {grade}")

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Write an if/else that prints 'even' or 'odd' for a number.
# EXERCISE 2 (easy): Write an if/elif/else chain that classifies a temperature (cold/mild/hot).
# EXERCISE 3 (easy): Nest an if inside another if to check two conditions.
# EXERCISE 4 (medium): Use a ternary (conditional) expression to assign a value.
# EXERCISE 5 (medium): Write an if statement that checks multiple conditions using `and`/`or`.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that classifies a triangle (equilateral/isosceles/scalene) given 3 side lengths.


# ============================================
# 5. SUMMARY
# ============================================
# if/elif/else lets your program make decisions based on data at runtime.
