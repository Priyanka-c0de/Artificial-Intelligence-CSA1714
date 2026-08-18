import numpy as np

# Sigmoid Activation Function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Input dataset (XOR Logic Gate)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Expected target output
y = np.array([[0], [1], [1], [0]])

# Set random seed for reproducibility
np.random.seed(42)

# Neural Network Architecture Parameters
input_nodes = 2
hidden_nodes = 2
output_nodes = 1
learning_rate = 0.5
epochs = 10000

# Weight and Bias Initialization
W1 = np.random.uniform(size=(input_nodes, hidden_nodes))
b1 = np.random.uniform(size=(1, hidden_nodes))
W2 = np.random.uniform(size=(hidden_nodes, output_nodes))
b2 = np.random.uniform(size=(1, output_nodes))

# Training Phase (Gradient Descent)
for epoch in range(epochs):
    # Forward Pass
    hidden_input = np.dot(X, W1) + b1
    hidden_output = sigmoid(hidden_input)
    
    final_input = np.dot(hidden_output, W2) + b2
    predicted_output = sigmoid(final_input)
    
    # Backpropagation
    error = y - predicted_output
    
    d_predicted_output = error * sigmoid_derivative(predicted_output)
    error_hidden = d_predicted_output.dot(W2.T)
    d_hidden_output = error_hidden * sigmoid_derivative(hidden_output)
    
    # Weight and Bias Updates
    W2 += hidden_output.T.dot(d_predicted_output) * learning_rate
    b2 += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate
    W1 += X.T.dot(d_hidden_output) * learning_rate
    b1 += np.sum(d_hidden_output, axis=0, keepdims=True) * learning_rate

# Testing Output
print("Trained Predictions for XOR Problem:")
for inputs, pred in zip(X, predicted_output):
    print(f"Input: {inputs} -> Predicted Output: {pred[0]:.4f} (Rounded: {round(pred[0])})")