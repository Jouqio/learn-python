"""
Topic: JSON
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# The json module converts between Python objects and JSON text, useful for config files and APIs.

# ============================================
# 2. EXAMPLE
# ============================================

import json

data = {"name": "Nadia", "age": 24, "skills": ["Python", "SQL"]}
json_text = json.dumps(data, indent=2)
print(json_text)

parsed = json.loads(json_text)
print(parsed["skills"])

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Convert a Python dictionary to a JSON string with indentation.
# EXERCISE 2 (easy): Parse a JSON string back into a Python dictionary.
# EXERCISE 3 (easy): Write a dictionary to a .json file using json.dump.
# EXERCISE 4 (medium): Read a .json file back into Python using json.load.
# EXERCISE 5 (medium): Handle a malformed JSON string with try/except json.JSONDecodeError.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a small 'settings manager' that loads settings from a JSON file if it exists, or creates one with defaults if it doesn't.


# ============================================
# 5. SUMMARY
# ============================================
# JSON is the most common data-interchange format; Python's json module makes round-tripping simple.
