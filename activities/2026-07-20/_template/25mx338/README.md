# Thorogood Associates - Mission 3

## Problem Statement

Implement the K-Means Clustering algorithm from scratch without using Scikit-learn. The algorithm groups customer coordinates into K distinct clusters based on Euclidean distance.

---

## Technologies Used

- Python
- NumPy
- Matplotlib

---

## Architecture

1. Load the customer coordinate dataset.
2. Randomly initialize K centroids.
3. Compute Euclidean distance from every point to every centroid.
4. Assign each point to the nearest centroid.
5. Recalculate centroid positions.
6. Repeat until centroids no longer change.
7. Display the final clusters and visualize the result.

---

## Algorithm

```
Initialize K centroids

Repeat

    Calculate distance from every point to every centroid

    Assign each point to nearest centroid

    Compute new centroid of each cluster

Until convergence
```

---

## Time Complexity

Let

- N = number of data points
- K = number of clusters
- I = number of iterations

Distance computation

O(N × K)

Centroid update

O(N)

Overall Complexity

O(I × N × K)

Space Complexity

O(N + K)

---

## Output

The program prints

- Final centroid coordinates
- Cluster assignments

It also generates a visualization showing

- Clustered points
- Final centroids

---

## Trade-offs

Advantages

- Simple implementation
- Fast for medium-sized datasets
- Easy to visualize

Limitations

- Sensitive to centroid initialization
- May converge to a local optimum
- Requires choosing K beforehand

---

## Future Improvements

- K-Means++
- Elbow Method
- Silhouette Score
- CSV file input support
