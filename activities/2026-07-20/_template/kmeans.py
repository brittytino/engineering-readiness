import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Load Dataset
# -----------------------------
# Example dataset (replace with your own CSV if provided)
data = np.array([
    [1,2],
    [2,1],
    [3,2],
    [8,8],
    [9,8],
    [8,9],
    [20,20],
    [21,19],
    [19,21]
])

K = 3
max_iterations = 100

# -----------------------------
# Initialize Centroids
# -----------------------------
np.random.seed(42)
indices = np.random.choice(len(data), K, replace=False)
centroids = data[indices]

# -----------------------------
# K-Means Algorithm
# -----------------------------
for iteration in range(max_iterations):

    # Distance calculation
    distances = np.sqrt(((data - centroids[:, np.newaxis])**2).sum(axis=2))

    # Assign clusters
    labels = np.argmin(distances, axis=0)

    # Compute new centroids
    new_centroids = np.array([
        data[labels == k].mean(axis=0)
        for k in range(K)
    ])

    # Stop if converged
    if np.allclose(centroids, new_centroids):
        break

    centroids = new_centroids

# -----------------------------
# Results
# -----------------------------
print("Final Centroids:\n")
print(centroids)

print("\nCluster Assignments:\n")
for k in range(K):
    print(f"Cluster {k+1}:")
    print(data[labels == k])

# -----------------------------
# Visualization
# -----------------------------
colors = ['red','blue','green','purple','orange']

for k in range(K):
    cluster = data[labels == k]
    plt.scatter(cluster[:,0], cluster[:,1],
                color=colors[k],
                label=f'Cluster {k+1}')

plt.scatter(centroids[:,0],
            centroids[:,1],
            marker='X',
            s=200,
            color='black',
            label='Centroids')

plt.title("K-Means Clustering From Scratch")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.legend()

plt.savefig("output.png")
plt.show()
