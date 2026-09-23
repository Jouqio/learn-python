"""
Topic: Deleting Files and Folders
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# The os module removes files (os.remove) and folders (os.rmdir / shutil.rmtree), and checks existence first to avoid errors.

# ============================================
# 2. EXAMPLE
# ============================================

import os

with open("temp.txt", "w", encoding="utf-8") as f:
    f.write("temporary")

if os.path.exists("temp.txt"):
    os.remove("temp.txt")
    print("Deleted temp.txt")
else:
    print("File does not exist.")

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Check if a file exists before attempting to delete it.
# EXERCISE 2 (easy): Delete a file using os.remove() safely inside a try/except.
# EXERCISE 3 (easy): Create and then delete an empty folder using os.mkdir()/os.rmdir().
# EXERCISE 4 (medium): Use shutil.rmtree() to delete a non-empty folder (explain the risk in a comment).
# EXERCISE 5 (medium): List all files in a directory using os.listdir() before deciding what to delete.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `cleanup_old_logs(folder, keep_latest=5)` that deletes all but the 5 most recently modified files in a folder.


# ============================================
# 5. SUMMARY
# ============================================
# Always confirm a file/folder exists (or catch the error) before deleting, since deletions are usually irreversible.
