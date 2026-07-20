# Thorogood Associates Technical Challenge

## Objective

Implement K-Means Clustering from scratch without using Scikit-learn.

---

## Technologies

- Python
- NumPy
- Pandas
- Matplotlib

---

## Dataset

2D customer coordinates.

---

## Methodology

1. Load dataset.
2. Remove duplicates and null values.
3. Randomly initialize K centroids.
4. Compute Euclidean distance.
5. Assign each point to nearest centroid.
6. Update centroids.
7. Repeat until convergence.
8. Visualize clusters.

---

## Output

- Final centroid coordinates
- Cluster visualization

---

## Complexity

Time:

O(i × n × k)

Space:

O(n + k)

where

- n = data points
- k = clusters
- i = iterations

---

## Architectural Design

```
Dataset
   ↓
Cleaning
   ↓
Initialize Centroids
   ↓
Distance Computation
   ↓
Cluster Assignment
   ↓
Centroid Update
   ↓
Convergence Check
   ↓
Visualization
```

---

## Libraries

- NumPy
- Pandas
- Matplotlib

(No Scikit-learn used.)
