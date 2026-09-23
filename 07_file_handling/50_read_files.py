"""
Topic: Reading Files
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Files can be read fully with .read(), line by line with .readline()/for-loop, or all lines with .readlines().

# ============================================
# 2. EXAMPLE
# ============================================

with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("Satu\nDua\nTiga\n")

with open("sample.txt", "r", encoding="utf-8") as f:
    for line_number, line in enumerate(f, start=1):
        print(f"{line_number}: {line.strip()}")

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Read a file's entire content into one string.
# EXERCISE 2 (easy): Read a file line by line using a for loop.
# EXERCISE 3 (easy): Read only the first line of a file using .readline().
# EXERCISE 4 (medium): Read all lines into a list using .readlines().
# EXERCISE 5 (medium): Count the number of lines in a file.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `read_csv_like(filepath)` that reads a comma-separated text file and returns a list of row lists.


# ============================================
# 5. SUMMARY
# ============================================
# Choose the reading strategy (.read/.readline/.readlines/for-loop) based on file size and what you need.
