"""
Topic: Classes and Objects
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# A class is a blueprint; objects are instances created from it, each with their own attribute values.

# ============================================
# 2. EXAMPLE
# ============================================

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

car1 = Car("Toyota", 2020)
car2 = Car("Honda", 2022)
print(car1.brand, car1.year)
print(car2.brand, car2.year)

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Create a class Animal with a name attribute and instantiate 2 animals.
# EXERCISE 2 (easy): Print the type of an object using type().
# EXERCISE 3 (easy): Create a list of 3 objects of the same class and loop over them.
# EXERCISE 4 (medium): Add a method to compare two objects' attributes.
# EXERCISE 5 (medium): Use isinstance() to check an object's class.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Design a `Student` class with name and a list of grades, plus a method `average_grade()`.


# ============================================
# 5. SUMMARY
# ============================================
# Classes define structure; objects are the concrete instances that hold actual data.
