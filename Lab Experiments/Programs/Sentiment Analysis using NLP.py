from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Training data
texts = [
    "I love this movie",
    "This movie is excellent",
    "The product is amazing",
    "I really enjoyed this",
    "This is a wonderful experience",
    "I hate this movie",
    "This movie is terrible",
    "The product is bad",
    "I disliked this",
    "This is a horrible experience"
]

# Labels: 1 = Positive, 0 = Negative
labels = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

# Convert text into numerical features
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(texts)

# Train classifier
model = LogisticRegression()
model.fit(X, labels)

# Test sentences
test_texts = [
    "This movie was fantastic",
    "I hate this product",
    "The experience was wonderful"
]

# Transform test data
X_test = vectorizer.transform(test_texts)

# Predict sentiment
predictions = model.predict(X_test)

# Display results
for text, prediction in zip(test_texts, predictions):
    sentiment = "Positive" if prediction == 1 else "Negative"
    print(text, "->", sentiment)