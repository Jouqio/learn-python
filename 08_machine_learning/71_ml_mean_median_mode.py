"""
Topic: Mean, Median, Mode
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Mean, median, and mode are the three basic measures of central tendency in a dataset.

# ============================================
# 2. EXAMPLE
# ============================================

from statistics import mean, median, mode

scores = [70, 85, 90, 85, 60, 85]
print("Mean:", mean(scores))
print("Median:", median(scores))
print("Mode:", mode(scores))

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Compute the mean of a list of 10 numbers.
# EXERCISE 2 (easy): Compute the median of a list with an even number of elements.
# EXERCISE 3 (easy): Compute the mode of a dataset with a clear repeated value.
# EXERCISE 4 (medium): Explain when median is more useful than mean (e.g. with outliers).
# EXERCISE 5 (medium): Compute mean/median/mode using NumPy instead of the statistics module.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `central_tendency_report(numbers)` that returns a dictionary with mean, median, and mode.


# ============================================
# 5. SUMMARY
# ============================================
# Mean, median, and mode summarize a dataset's 'typical' value from different angles, each useful in different situations.
