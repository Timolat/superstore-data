#libaries needed
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Reload the dataset
df = pd.read_csv(r'C:\Users\Abraham\Desktop\DOINGS\supermarket_sales - Sheet1.csv')

# removing extra space(striping extra space)
df.columns = df.columns.str.strip()

#numerical features for regression
features = ["Unit price", "Quantity", "Tax 5%"]  # Independent variables (X)
target = "Total"  # Dependent variable (y)

# Extract X and y
X = df[features]
y = df[target]

# Split into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Create a scatter plot of actual vs. predicted values
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.7)
plt.xlabel("Actual Total Sales")
plt.ylabel("Predicted Total Sales")
plt.title("Actual vs. Predicted Total Sales")
plt.axline([0, 0], [1, 1], color="red", linestyle="--", linewidth=2)  # Perfect prediction line
plt.show()
