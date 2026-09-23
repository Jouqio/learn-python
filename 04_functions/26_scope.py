"""
Topic: Variable Scope
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Variables defined inside a function are local by default; `global` and `nonlocal` allow modifying outer scopes explicitly.

# ============================================
# 2. EXAMPLE
# ============================================

counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print(counter)

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Write a function with a local variable that does not affect an outer variable of the same name.
# EXERCISE 2 (easy): Use the `global` keyword to modify a module-level variable from inside a function.
# EXERCISE 3 (easy): Write a nested function that uses `nonlocal` to modify the enclosing function's variable.
# EXERCISE 4 (medium): Explain (with prints) why relying on global state can cause bugs.
# EXERCISE 5 (medium): Refactor a global-variable-based counter into a class or closure instead.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a closure-based counter() function that returns increment/decrement/get functions sharing private state (no globals).


# ============================================
# 5. SUMMARY
# ============================================
# Understanding local vs global scope prevents subtle bugs; prefer passing values explicitly over using globals.
