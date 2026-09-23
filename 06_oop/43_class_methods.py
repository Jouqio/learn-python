"""
Topic: Instance, Class, and Static Methods
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Instance methods take self; classmethods take cls and can construct alternate instances; staticmethods take neither.

# ============================================
# 2. EXAMPLE
# ============================================

class Pizza:
    def __init__(self, size):
        self.size = size

    @classmethod
    def small(cls):
        return cls(size="small")

    @staticmethod
    def is_valid_size(size):
        return size in ("small", "medium", "large")

p = Pizza.small()
print(p.size, Pizza.is_valid_size("large"))

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Write a classmethod that creates an object with a preset configuration.
# EXERCISE 2 (easy): Write a staticmethod that performs a utility check unrelated to instance state.
# EXERCISE 3 (easy): Explain the difference between self, cls, and no implicit argument.
# EXERCISE 4 (medium): Add a classmethod alternate constructor that parses a string into an object.
# EXERCISE 5 (medium): Call a staticmethod both on the class and on an instance.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Design a `Temperature` class with classmethod `from_fahrenheit(cls, f)` and staticmethod `is_freezing(celsius)`.


# ============================================
# 5. SUMMARY
# ============================================
# Choose instance/class/static methods based on whether you need per-object data, the class itself, or neither.
