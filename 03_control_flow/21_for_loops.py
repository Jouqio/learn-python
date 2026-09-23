"""
Topic: For Loops
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# for loops iterate over sequences (lists, strings, ranges, dicts). Combine with range(), enumerate(), and zip().

# ============================================
# 2. EXAMPLE
# ============================================

for i in range(1, 6):
    print(i)

names = ["Andi", "Bella", "Citra"]
for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Print the numbers 1 to 20 using range().
# EXERCISE 2 (easy): Loop over a string and print each character on its own line.
# EXERCISE 3 (easy): Use enumerate() to number items in a list starting at 1.
# EXERCISE 4 (medium): Use zip() to pair two lists (names and scores) together.
# EXERCISE 5 (medium): Sum all numbers from 1 to 100 using a for loop.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that prints a multiplication table (1-10) using nested for loops.


# ============================================
# 5. SUMMARY
# ============================================
# for loops are the most common way to process sequences item by item in Python.
