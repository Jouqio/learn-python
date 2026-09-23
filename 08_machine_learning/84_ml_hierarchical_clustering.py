"""
Topic: Hierarchical Clustering
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Hierarchical clustering groups data points into nested clusters, visualized as a dendrogram.

# ============================================
# 2. EXAMPLE
# ============================================

from scipy.cluster.hierarchy import linkage, fcluster
import numpy as np

points = np.array([[4, 21], [5, 19], [10, 24], [4, 17], [3, 16], [11, 25], [14, 24]])
linkage_matrix = linkage(points, method="ward")
clusters = fcluster(linkage_matrix, t=2, criterion="maxclust")
print("Cluster assignments:", clusters)

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Run hierarchical clustering on a small set of 2D points.
# EXERCISE 2 (easy): Split the results into 2 clusters and print the assignment for each point.
# EXERCISE 3 (easy): Try 3 clusters instead of 2 and compare results.
# EXERCISE 4 (medium): Plot a dendrogram using scipy.cluster.hierarchy.dendrogram.
# EXERCISE 5 (medium): Explain (as prints) the difference between 'ward', 'single', and 'complete' linkage.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function that clusters a set of 2D points into a chosen number of clusters and returns the grouped points.


# ============================================
# 5. SUMMARY
# ============================================
# Hierarchical clustering builds a tree of nested groupings, useful when the number of clusters isn't known in advance.
