import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Dataset: Experience (Years) vs Salary ($ in thousands)
X = np.array([[1.1], [1.3], [1.5], [2.0], [2.2], [2.9], [3.0], [3.2]])
y = np.array([39.3, 46.2, 44.3, 43.5, 39.8, 56.6, 60.1, 54.4])

# Initialize and train Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Retrieve learned slope (theta_1) and intercept (theta_0)
slope = model.coef_[0]
intercept = model.intercept_

# Make predictions on training set
y_pred = model.predict(X)

# Calculate performance metrics
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f"Learned Equation: Salary = {intercept:.2f} + {slope:.2f} * Experience")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared Score (R2): {r2:.2f}\n")

# Predict salary for a candidate with 2.5 years of experience
new_experience = np.array([[2.5]])
predicted_salary = model.predict(new_experience)[0]
print(f"Predicted Salary for {new_experience[0][0]} years of experience: ${predicted_salary:.2f}k")