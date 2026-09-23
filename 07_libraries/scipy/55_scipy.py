"""
Topic: SciPy (Scientific Python)
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
Covers: Introduction, Getting Started, Constants, Optimizers, Sparse Data,
Graphs, Spatial Data, Interpolation, Significance Tests.
Install with: pip install scipy
"""
from scipy import constants, optimize, sparse, interpolate, stats
import numpy as np

# ============================================
# 1. CONSTANTS
# ============================================
print("Speed of light:", constants.speed_of_light)
print("Gravitational constant:", constants.gravitational_constant if hasattr(constants, "gravitational_constant") else constants.g)

# ============================================
# 2. OPTIMIZERS
# ============================================
def f(x):
    return x ** 2 + 5 * x + 4

result = optimize.minimize(f, x0=0)
print("Minimum near x =", round(result.x[0], 3))

# ============================================
# 3. SPARSE DATA
# ============================================
dense = np.array([[0, 0, 3], [4, 0, 0], [0, 0, 5]])
sparse_matrix = sparse.csr_matrix(dense)
print("Sparse matrix representation:\n", sparse_matrix)

# ============================================
# 4. SPATIAL DATA
# ============================================
from scipy.spatial import distance
point_a, point_b = (0, 0), (3, 4)
print("Euclidean distance:", distance.euclidean(point_a, point_b))

# ============================================
# 5. INTERPOLATION
# ============================================
x_known = np.array([0, 1, 2, 3])
y_known = np.array([0, 1, 4, 9])
interp_func = interpolate.interp1d(x_known, y_known)
print("Interpolated value at x=1.5:", interp_func(1.5))

# ============================================
# 6. SIGNIFICANCE TESTS
# ============================================
group_a = [23, 25, 21, 22, 24]
group_b = [30, 28, 27, 29, 31]
t_stat, p_value = stats.ttest_ind(group_a, group_b)
print(f"t-statistic={t_stat:.3f}, p-value={p_value:.4f}")

# ============================================
# PRACTICE
# ============================================
# EASY 1: Print 3 physical constants from scipy.constants.
# EASY 2: Use optimize.minimize on a different quadratic function.
# EASY 3: Compute the Manhattan distance (cityblock) between two points.
# MEDIUM 1: Build an interpolation function and estimate 3 in-between values.
# MEDIUM 2: Run a t-test comparing two small sample groups of your own numbers.
#
# CHALLENGE: Write a function `find_root(func, guess)` using scipy.optimize
# to find where a given function crosses zero.

# ============================================
# SUMMARY
# ============================================
# SciPy builds on NumPy to add optimization, interpolation, spatial, and
# statistical tools needed for scientific and data-analysis work.
