"""
Topic: Exception Handling
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# try/except/else/finally handles runtime errors gracefully instead of crashing the program.

# ============================================
# 2. EXAMPLE
# ============================================

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None
    else:
        return result
    finally:
        print("Division attempt finished.")

print(safe_divide(10, 2))
print(safe_divide(10, 0))

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Catch a ZeroDivisionError and print a friendly message.
# EXERCISE 2 (easy): Catch a ValueError when converting invalid text to int.
# EXERCISE 3 (easy): Use finally to always print a closing message regardless of errors.
# EXERCISE 4 (medium): Raise a custom exception using `raise ValueError('message')`.
# EXERCISE 5 (medium): Catch multiple exception types in one except clause using a tuple.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `parse_age(text)` that raises a custom `InvalidAgeError` if the age is negative or not a number.


# ============================================
# 5. SUMMARY
# ============================================
# Exception handling keeps programs robust; catch specific exceptions rather than bare `except:`.
