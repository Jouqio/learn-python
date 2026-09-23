"""
Topic: The self Parameter
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# `self` refers to the current instance, letting methods access and modify that instance's own attributes.

# ============================================
# 2. EXAMPLE
# ============================================

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

c = Counter()
c.increment()
c.increment()
print(c.count)

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Write a method that uses self to read an attribute.
# EXERCISE 2 (easy): Write a method that uses self to modify an attribute.
# EXERCISE 3 (easy): Create two objects and show their `self` data stays independent.
# EXERCISE 4 (medium): Explain what happens if you forget `self` in a method definition (try it and read the error).
# EXERCISE 5 (medium): Write a method that calls another method on `self`.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Design a `Wallet` class with deposit(self, amount) and withdraw(self, amount) methods that both rely on self.balance.


# ============================================
# 5. SUMMARY
# ============================================
# `self` is how each object keeps track of and manipulates its own unique data.
