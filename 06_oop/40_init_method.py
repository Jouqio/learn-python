"""
Topic: The __init__() Method
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# __init__ is the constructor, automatically called when an object is created, used to set up initial attributes.

# ============================================
# 2. EXAMPLE
# ============================================

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

acc = Account("Rina")
print(acc.owner, acc.balance)

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Create a class where __init__ requires 2 parameters.
# EXERCISE 2 (easy): Give one parameter in __init__ a default value.
# EXERCISE 3 (easy): Add validation inside __init__ that raises an error for invalid input.
# EXERCISE 4 (medium): Create an object and immediately print an attribute set in __init__.
# EXERCISE 5 (medium): Explain (via prints) why __init__ is not the same as a class itself.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Design a `Rectangle` class whose __init__ validates that width and height are positive, raising ValueError otherwise.


# ============================================
# 5. SUMMARY
# ============================================
# __init__ is where you validate and set up an object's initial, consistent state.
