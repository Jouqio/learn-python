"""
Topic: Dates and Times
Level: Beginner
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# The datetime module handles dates, times, and durations.

# ============================================
# 2. EXAMPLE
# ============================================

from datetime import datetime, timedelta

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M"))
next_week = now + timedelta(days=7)
print(next_week.strftime("%Y-%m-%d"))

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Print today's date formatted as DD/MM/YYYY.
# EXERCISE 2 (easy): Calculate the date 30 days from today.
# EXERCISE 3 (easy): Calculate the number of days between two given dates.
# EXERCISE 4 (medium): Parse a date string like '2026-01-15' into a datetime object.
# EXERCISE 5 (medium): Print the current day of the week as a name (e.g. 'Wednesday').
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `days_until_birthday(birth_month, birth_day)` that returns how many days remain until the next birthday.


# ============================================
# 5. SUMMARY
# ============================================
# datetime is the standard tool for date arithmetic and formatting in Python.
