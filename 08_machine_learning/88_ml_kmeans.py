"""
Topic: K-Means Clustering
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# K-Means partitions data into k clusters by iteratively assigning points to the nearest cluster center.

# ============================================
# 2. EXAMPLE
# ============================================

from sklearn.cluster import KMeans
import numpy as np

points = np.array([[4, 21], [5, 19], [10, 24], [4, 17], [3, 16], [11, 25], [14, 24]])
model = KMeans(n_clusters=2, random_state=0, n_init=10)
model.fit(points)
print("Cluster labels:", model.labels_)
print("Cluster centers:\n", model.cluster_centers_)

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Cluster a small 2D dataset into 2 clusters with KMeans.
# EXERCISE 2 (easy): Print each point's assigned cluster label.
# EXERCISE 3 (easy): Try k=3 and compare the resulting clusters.
# EXERCISE 4 (medium): Use the elbow method (plot inertia vs k) to help choose k.
# EXERCISE 5 (medium): Predict the cluster of a brand-new point using model.predict().
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Write a function `find_best_k(points, k_range)` that returns the inertia for each k in a range, to help visualize the elbow method.


# ============================================
# 5. SUMMARY
# ============================================
# K-Means is a fast, popular clustering algorithm, though it requires choosing k in advance.
