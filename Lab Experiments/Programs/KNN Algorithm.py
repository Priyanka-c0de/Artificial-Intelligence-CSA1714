import numpy as np
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

class KNNClassifier:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = np.array(X)
        self.y_train = np.array(y)

    def predict(self, X):
        X = np.array(X)
        return np.array([self._predict_single(x) for x in X])

    def _predict_single(self, x):
        # Calculate Euclidean distances to all training points
        distances = np.sqrt(np.sum((self.X_train - x) ** 2, axis=1))
        
        # Get indices of K smallest distances
        k_indices = np.argsort(distances)[:self.k]
        
        # Extract corresponding labels
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        
        # Return most common label
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]

# Load standard Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train custom KNN model
knn = KNNClassifier(k=3)
knn.fit(X_train, y_train)

# Predict test set
y_pred = knn.predict(X_test)

# Calculate accuracy
accuracy = np.mean(y_pred == y_test) * 100
print(f"KNN Accuracy (k=3): {accuracy:.2f}%")

# Predict a new sample
sample = [[5.1, 3.5, 1.4, 0.2]]
predicted_class = knn.predict(sample)[0]
print(f"Predicted Class Index for {sample[0]}: {predicted_class} ({iris.target_names[predicted_class]})")