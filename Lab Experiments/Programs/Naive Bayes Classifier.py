from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

# Sample synthetic dataset: [Height (cm), Weight (kg), Foot Size (cm)]
X = [
    [180, 85, 28], [175, 75, 26], [170, 65, 25], [165, 60, 24],
    [160, 55, 23], [155, 50, 22], [185, 90, 29], [178, 80, 27]
]
# Labels: 0 = Female, 1 = Male
y = [1, 1, 1, 0, 0, 0, 1, 1]

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Initialize Gaussian Naive Bayes model
model = GaussianNB()

# Train the model
model.fit(X_train, y_train)

# Predict test set results
y_pred = model.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")

# Predict a new sample: [Height=172, Weight=70, Foot Size=25]
sample = [[172, 70, 25]]
prediction = model.predict(sample)
gender = "Male" if prediction[0] == 1 else "Female"

print(f"Prediction for sample {sample[0]}: {gender}")