# importing necessary libraries
import pandas as pd

import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Reload the dataset

df = pd.read_csv(r'C:\Users\Abraham\Desktop\DOINGS\supermarket_sales - Sheet1.csv')

# Strip column names of any extra spaces
df.columns = df.columns.str.strip()

# Select numerical features for regression
features = ["Unit price", "Quantity", "Tax 5%"]  # Independent variables (X)
target = "Total"  # Dependent variable (y)

# Extract X and y
X = df[features]
y = df[target]

# Split into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction on the test set
y_pred = model.predict(X_test)

# Evaluating model performance
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Display results
print("\nregression result:")
print(mae, r2) 

from sklearn.metrics import mean_squared_error

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)

# Display evaluation metrics

print("\nevaluation metrics:")
print(mse, r2)
