import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Dummy data
X = np.array([
    [25, 20000],
    [30, 25000],
    [35, 30000],
    [40, 40000],
    [45, 50000]
])

# Model
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Plot
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_)
plt.scatter(kmeans.cluster_centers_[:, 0],
            kmeans.cluster_centers_[:, 1],
            marker='X')

plt.xlabel("Age")
plt.ylabel("Income")
plt.title("K-Means Clustering")
plt.show()
