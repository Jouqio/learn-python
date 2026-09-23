"""
Topic: The None Type
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# None represents the absence of a value. Use `is None` / `is not None`, not `==`, for comparisons.

# ============================================
# 2. EXAMPLE
# ============================================

def find_user(user_id, users):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

result = find_user(99, [{"id": 1, "name": "Eka"}])
if result is None:
    print("User not found.")

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Write a function that returns None when a search fails.
# EXERCISE 2 (easy): Check a variable for None using `is None`.
# EXERCISE 3 (easy): Explain why `is None` is preferred over `== None` (as a print statement).
# EXERCISE 4 (medium): Use None as a default parameter value, then replace it inside the function body.
# EXERCISE 5 (medium): Write a function that filters out None values from a list.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `first_positive(numbers)` that returns the first positive number or None if none exist.


# ============================================
# 5. SUMMARY
# ============================================
# None is a real, singleton value in Python representing 'nothing here', distinct from 0, False, or an empty string.
