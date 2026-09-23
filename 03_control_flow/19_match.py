"""
Topic: Match Statement
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# The match statement (Python 3.10+) provides structural pattern matching, an alternative to long if/elif chains.

# ============================================
# 2. EXAMPLE
# ============================================

def describe_status(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500 | 502 | 503:
            return "Server Error"
        case _:
            return "Unknown"

print(describe_status(404))
print(describe_status(502))

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Write a match statement for days of the week returning 'Weekend' or 'Weekday'.
# EXERCISE 2 (easy): Use the `|` pattern to match multiple values in one case.
# EXERCISE 3 (easy): Use a wildcard `_` case as a default.
# EXERCISE 4 (medium): Match against a tuple pattern, e.g. (0, 0) meaning 'origin'.
# EXERCISE 5 (medium): Rewrite an existing if/elif chain from topic 18 using match instead.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a simple command dispatcher using match that maps string commands ('start','stop','pause') to actions.


# ============================================
# 5. SUMMARY
# ============================================
# match is useful when you have many discrete cases to compare against a single value.
