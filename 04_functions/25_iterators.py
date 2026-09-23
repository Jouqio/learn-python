"""
Topic: Iterators
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# An iterator implements __iter__ and __next__. Lists, strings, and ranges are iterable; iter() and next() expose the protocol directly.

# ============================================
# 2. EXAMPLE
# ============================================

numbers = [10, 20, 30]
it = iter(numbers)
print(next(it))
print(next(it))
print(next(it))

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Create an iterator from a list and manually call next() 3 times.
# EXERCISE 2 (easy): Catch the StopIteration exception when an iterator is exhausted.
# EXERCISE 3 (easy): Write a custom class implementing __iter__ and __next__ for a countdown.
# EXERCISE 4 (medium): Use a generator expression to lazily produce squares.
# EXERCISE 5 (medium): Explain the difference between an iterable and an iterator in your own words (as prints).
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a custom iterator class `EvenNumbers(limit)` that yields even numbers up to `limit`.


# ============================================
# 5. SUMMARY
# ============================================
# Iterators provide a uniform lazy-access protocol behind Python's for loops.
