from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Load standard Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Use binary classification for clear margin visualization (Classes 0 and 1)
X_binary = X[y != 2]
y_binary = y[y != 2]

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_binary, y_binary, test_size=0.3, random_state=42)

# Initialize Support Vector Classifier with Linear Kernel
svm_model = SVC(kernel='linear', C=1.0)

# Train the SVM model
svm_model.fit(X_train, y_train)

# Predict test set instances
y_pred = svm_model.predict(X_test)

# Calculate model accuracy
accuracy = accuracy_score(y_test, y_pred) * 100
print(f"SVM Accuracy: {accuracy:.2f}%")
print(f"Number of Support Vectors: {len(svm_model.support_vectors_)}")

# Predict a new test sample
sample = [[5.0, 3.4, 1.5, 0.2]]
prediction = svm_model.predict(sample)
print(f"Prediction for sample {sample[0]}: {iris.target_names[prediction[0]]}")
