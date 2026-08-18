from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score

# Load standard Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Decision Tree Classifier (Criterion: Entropy, Max Depth: 3)
clf = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=42)

# Train the model
clf.fit(X_train, y_train)

# Predict test set
y_pred = clf.predict(X_test)

# Calculate accuracy score
accuracy = accuracy_score(y_test, y_pred) * 100
print(f"Decision Tree Accuracy: {accuracy:.2f}%\n")

# Display decision rules structure
print("Learned Decision Rules:")
tree_rules = export_text(clf, feature_names=iris.feature_names)
print(tree_rules)