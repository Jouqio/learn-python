"""
Topic: File Handling Overview
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Python reads/writes files using open() with modes like 'r', 'w', 'a', 'x', ideally inside a `with` block for automatic closing.

# ============================================
# 2. EXAMPLE
# ============================================

with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("Line 1\nLine 2\n")

with open("sample.txt", "r", encoding="utf-8") as f:
    print(f.read())

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Open a file in write mode and write 2 lines to it.
# EXERCISE 2 (easy): Open the same file in read mode and print its contents.
# EXERCISE 3 (easy): Open a file in append mode and add a third line.
# EXERCISE 4 (medium): Explain why `with open(...) as f:` is preferred over manual open()/close().
# EXERCISE 5 (medium): Handle a missing file gracefully using try/except FileNotFoundError.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `word_count(filepath)` that returns the number of words in a text file.


# ============================================
# 5. SUMMARY
# ============================================
# Always use `with` when working with files so they are closed automatically, even if an error occurs.
