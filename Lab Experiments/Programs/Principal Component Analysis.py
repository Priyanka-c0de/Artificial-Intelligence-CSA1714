import numpy as np
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

# Load dataset with 4 feature dimensions
iris = load_iris()
X = iris.data
y = iris.target

print(f"Original Feature Shape: {X.shape}")

# Initialize PCA to reduce dimensions from 4 features down to 2 principal components
pca = PCA(n_components=2)

# Fit model and transform dataset
X_reduced = pca.fit_transform(X)

print(f"Reduced Feature Shape: {X_reduced.shape}\n")

# Calculate explained variance ratio
explained_variance = pca.explained_variance_ratio_
print(f"Variance explained by PC1: {explained_variance[0]*100:.2f}%")
print(f"Variance explained by PC2: {explained_variance[1]*100:.2f}%")
print(f"Total variance preserved: {sum(explained_variance)*100:.2f}%\n")

# Display first 3 transformed samples
print("Sample Transformed Points (PC1, PC2):")
for i in range(3):
    print(f"Sample {i+1}: {X_reduced[i]}")