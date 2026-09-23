"""
Topic: NumPy (Numerical Python)
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
Covers: Introduction, Getting Started, Arrays, Indexing, Slicing, Data Types,
Copy vs View, Shape, Reshape, Iterating, Join, Split, Search, Sort, Filter, Random.
Install with: pip install numpy
"""
import numpy as np

# ============================================
# 1. INTRODUCTION & GETTING STARTED
# ============================================
# NumPy provides a fast, memory-efficient n-dimensional array (ndarray),
# much faster than plain Python lists for numeric work because operations
# run in optimized C code instead of a Python-level loop.

arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr, "| type:", type(arr))

# ============================================
# 2. ARRAY INDEXING & SLICING
# ============================================
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Element [1, 2]:", matrix[1, 2])
print("First row:", matrix[0, :])
print("Slice [0:2, 1:3]:\n", matrix[0:2, 1:3])

# ============================================
# 3. DATA TYPES
# ============================================
float_arr = np.array([1, 2, 3], dtype="f")
print("dtype:", float_arr.dtype)

# ============================================
# 4. COPY VS VIEW
# ============================================
original = np.array([10, 20, 30])
view = original.view()
copy = original.copy()
original[0] = 999
print("original:", original, "| view (changes with original):", view, "| copy (independent):", copy)

# ============================================
# 5. SHAPE & RESHAPE
# ============================================
flat = np.array([1, 2, 3, 4, 5, 6])
print("Shape:", flat.shape)
reshaped = flat.reshape(2, 3)
print("Reshaped:\n", reshaped)

# ============================================
# 6. ITERATING
# ============================================
for row in reshaped:
    for value in row:
        print("value:", value, end=" ")
print()

# ============================================
# 7. JOIN & SPLIT
# ============================================
a, b = np.array([1, 2]), np.array([3, 4])
joined = np.concatenate((a, b))
print("Joined:", joined)
split_result = np.array_split(joined, 2)
print("Split:", split_result)

# ============================================
# 8. SEARCH, SORT, FILTER
# ============================================
data = np.array([5, 2, 9, 1, 5, 6])
print("Index of value 9:", np.where(data == 9))
print("Sorted:", np.sort(data))
filtered = data[data > 4]
print("Filtered (>4):", filtered)

# ============================================
# 9. RANDOM
# ============================================
rng = np.random.default_rng(seed=42)
print("Random floats:", rng.random(3))
print("Random ints 1-10:", rng.integers(1, 11, size=5))

# ============================================
# PRACTICE
# ============================================
# EASY 1: Create a 1D array of 10 zeros using np.zeros().
# EASY 2: Create a 3x3 identity matrix using np.eye(3).
# EASY 3: Compute the mean and standard deviation of an array using .mean()/.std().
# MEDIUM 1: Reshape a 12-element array into a 3x4 matrix and print its transpose.
# MEDIUM 2: Given an array of exam scores, filter and count how many are >= 75.
#
# CHALLENGE: Write a function `normalize(arr)` that rescales a NumPy array so
# its values fall between 0 and 1 using min-max normalization.

# ============================================
# SUMMARY
# ============================================
# NumPy arrays are the foundation for numerical computing in Python and
# underpin pandas, scikit-learn, and most of the scientific Python stack.
