"""
Topic: Class Properties (Attributes)
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Attributes can be instance-level (unique per object) or class-level (shared across all instances).

# ============================================
# 2. EXAMPLE
# ============================================

class Employee:
    company = "PT Nusantara Tech"  # class attribute

    def __init__(self, name):
        self.name = name  # instance attribute

e1 = Employee("Dian")
e2 = Employee("Fikri")
print(e1.company, e2.company)
Employee.company = "PT Digital Prima"
print(e1.company, e2.company)

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Create a class attribute shared by all instances.
# EXERCISE 2 (easy): Create an instance attribute unique to each object.
# EXERCISE 3 (easy): Modify the class attribute and observe it affects all instances.
# EXERCISE 4 (medium): Modify an instance attribute and confirm it does not affect other instances.
# EXERCISE 5 (medium): Use the @property decorator to create a computed, read-only attribute.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Design a `BankAccount` class with a class attribute `bank_name` and a @property `formatted_balance` that returns a currency-formatted string.


# ============================================
# 5. SUMMARY
# ============================================
# Distinguish shared class-level state from per-object instance-level state to avoid subtle bugs.
