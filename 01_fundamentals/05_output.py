"""
Topic: Output with print()
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# print() displays output to the console. It accepts multiple arguments, a `sep`, and an `end` parameter.

# ============================================
# 2. EXAMPLE
# ============================================

print("Python", "is", "fun", sep="-")
print("No newline here...", end=" ")
print("...continues on the same line.")

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Print three words separated by commas using sep.
# EXERCISE 2 (easy): Print two print() calls that end up on the same output line using end.
# EXERCISE 3 (easy): Print a formatted table-like row using sep='\t'.
# EXERCISE 4 (medium): Print the numbers 1 to 5 on the same line separated by spaces (without a loop first, then with one).
# EXERCISE 5 (medium): Print a multi-line string using triple quotes.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a program that prints a simple ASCII progress bar like [====------] using only print() and string multiplication.


# ============================================
# 5. SUMMARY
# ============================================
# print() is flexible: sep controls what goes between arguments, end controls what comes after the whole call.
