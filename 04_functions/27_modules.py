"""
Topic: Modules
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Modules are .py files you can import to reuse code. Python also ships a large standard library of built-in modules.

# ============================================
# 2. EXAMPLE
# ============================================

import math
import random

print(math.sqrt(16))
print(random.randint(1, 6))

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Import the math module and use math.pi.
# EXERCISE 2 (easy): Import only a specific function using `from module import name`.
# EXERCISE 3 (easy): Create your own module file and import a function from it.
# EXERCISE 4 (medium): Use `import module as alias` and explain when that's useful.
# EXERCISE 5 (medium): List 3 standard library modules and what each is used for.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Create a small `string_utils.py` module with 2 helper functions, then import and use it from another file.


# ============================================
# 5. SUMMARY
# ============================================
# Modules let you organize and reuse code across files instead of duplicating logic.
