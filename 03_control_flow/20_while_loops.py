"""
Topic: While Loops
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# while loops repeat a block as long as a condition is True. Use break/continue to control flow.

# ============================================
# 2. EXAMPLE
# ============================================

count = 0
while count < 5:
    print(f"count = {count}")
    count += 1

n = 10
while n > 0:
    if n == 5:
        break
    n -= 1
print("Loop ended at", n)

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Print numbers 1 to 10 using a while loop.
# EXERCISE 2 (easy): Use `continue` to skip printing multiples of 3 in a while loop.
# EXERCISE 3 (easy): Write a while loop that keeps halving a number until it's less than 1.
# EXERCISE 4 (medium): Simulate a simple countdown timer (without real time delay).
# EXERCISE 5 (medium): Write a while True loop that breaks when a sentinel condition is met.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a number-guessing loop (no real input needed) that decreases a 'max attempts' counter and stops at 0 or on success.


# ============================================
# 5. SUMMARY
# ============================================
# while loops are best when the number of iterations is not known in advance.
