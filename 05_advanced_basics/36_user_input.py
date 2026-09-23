"""
Topic: User Input
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# input() reads a line of text from the user; the result is always a string, so cast it when you need a number.

# ============================================
# 2. EXAMPLE
# ============================================

name = input("What is your name? ") if False else "Simulated User"
print(f"Hello, {name}!")
# In an interactive run, use: name = input("What is your name? ")

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Ask the user for their age and print it back as an int.
# EXERCISE 2 (easy): Ask for two numbers and print their sum (cast both to float).
# EXERCISE 3 (easy): Validate input in a loop until the user enters a positive number.
# EXERCISE 4 (medium): Ask for a yes/no answer and normalize it to lowercase before checking.
# EXERCISE 5 (medium): Build a tiny interactive menu using input() and if/elif.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write an interactive program that keeps asking for numbers until the user types 'done', then prints their sum and average.


# ============================================
# 5. SUMMARY
# ============================================
# input() always returns a string; validating and casting user input safely is essential for robust programs.
