"""
Topic: Writing and Creating Files
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# 'w' overwrites, 'a' appends, and 'x' creates exclusively (fails if the file exists).

# ============================================
# 2. EXAMPLE
# ============================================

with open("log.txt", "w", encoding="utf-8") as f:
    f.write("Log started\n")

with open("log.txt", "a", encoding="utf-8") as f:
    f.write("Another entry\n")

with open("log.txt", "r", encoding="utf-8") as f:
    print(f.read())

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Create a new file and write a header line to it.
# EXERCISE 2 (easy): Append 3 more lines to the same file without erasing the header.
# EXERCISE 3 (easy): Use mode 'x' to create a file only if it doesn't already exist, and handle the FileExistsError.
# EXERCISE 4 (medium): Write a list of strings to a file, one per line.
# EXERCISE 5 (medium): Write formatted data (e.g. f-strings) into a report file.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `append_log(filepath, message)` that appends a timestamped message to a log file, creating the file if needed.


# ============================================
# 5. SUMMARY
# ============================================
# Choosing the right file mode ('w' vs 'a' vs 'x') prevents accidental data loss.
