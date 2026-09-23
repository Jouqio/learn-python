"""
Topic: Getting Started (Running Python)
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Python code can run as a script (.py file) or interactively in a REPL. In VS Code, you run a file with the Play button or `python filename.py` in the terminal.

# ============================================
# 2. EXAMPLE
# ============================================

def main():
    print("If you can see this message, your Python setup works.")

if __name__ == "__main__":
    main()

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Create a new file called practice_hello.py and print 'It works!'.
# EXERCISE 2 (easy): Run this file from the VS Code terminal using `python 03_get_started.py`.
# EXERCISE 3 (easy): Print the Python version check hint: `python --version` (write the command as a comment, then explain in a print statement why version matters).
# EXERCISE 4 (medium): Write a program with a main() function that prints 3 separate lines.
# EXERCISE 5 (medium): Write a program that intentionally has a syntax error, run it, read the traceback, then fix it.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a small script that prints a 5-line ASCII banner using only print() statements.


# ============================================
# 5. SUMMARY
# ============================================
# Every Python file with `if __name__ == "__main__":` can be run directly or imported as a module without side effects.
