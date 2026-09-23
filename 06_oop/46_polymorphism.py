"""
Topic: Polymorphism
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Polymorphism lets different classes be used interchangeably through a shared interface (e.g. the same method name).

# ============================================
# 2. EXAMPLE
# ============================================

class Cat:
    def speak(self):
        return "Meow"

class Duck:
    def speak(self):
        return "Quack"

for animal in [Cat(), Duck()]:
    print(animal.speak())

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Create 2 unrelated classes with the same method name and loop over both, calling that method.
# EXERCISE 2 (easy): Write a function that accepts any object with a `.area()` method and prints the result.
# EXERCISE 3 (easy): Show how built-in polymorphism works with len() on a string, list, and dict.
# EXERCISE 4 (medium): Combine inheritance and polymorphism: subclasses overriding a shared parent method.
# EXERCISE 5 (medium): Explain in prints why polymorphism reduces the need for type-checking if/elif chains.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `total_area(shapes)` that sums the area of any list of shape objects, regardless of their concrete class.


# ============================================
# 5. SUMMARY
# ============================================
# Polymorphism lets you write code against a shared interface, not against specific concrete types.
