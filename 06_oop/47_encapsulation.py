"""
Topic: Encapsulation
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Encapsulation restricts direct access to internal state using naming conventions (_protected, __private) and properties.

# ============================================
# 2. EXAMPLE
# ============================================

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # name-mangled 'private' attribute

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

acc = BankAccount(1000)
acc.deposit(500)
print(acc.balance)

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Create a class with a private attribute (double underscore) and a public getter method.
# EXERCISE 2 (easy): Use @property to expose a private attribute as read-only.
# EXERCISE 3 (easy): Add validation inside a setter method (or @x.setter) to reject invalid values.
# EXERCISE 4 (medium): Explain the difference between _protected and __private naming conventions.
# EXERCISE 5 (medium): Show what happens when you try to access a name-mangled attribute directly.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Design a `Password` class that stores a hashed value internally and only exposes a `check(guess)` method — never the raw password.


# ============================================
# 5. SUMMARY
# ============================================
# Encapsulation protects internal state, exposing only a controlled, validated interface to the outside.
