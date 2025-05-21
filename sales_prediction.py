# Simple Sales Prediction using Linear Regression
# Predict sales based on marketing budgets for TV, Radio, and Social Media

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Step 1: Load the dataset
# Make sure the CSV file "Dummy Data HSS.csv" is in the "data/" folder
data = pd.read_csv('data/Dummy Data HSS.csv')

# Step 2: Check the first few rows to understand the data
print("First 5 rows of the dataset:")
print(data.head())

# Step 3: Visualize the relationship between marketing budgets and sales
sns.pairplot(data, vars=['TV', 'Radio', 'Social Media', 'Sales'])
plt.suptitle('Marketing Budgets vs Sales', y=1.02)
plt.show()

# Step 4: Prepare data for modeling
# Features: TV, Radio, Social Media budgets
X = data[['TV', 'Radio', 'Social Media']]
# Target variable: Sales
y = data['Sales']

# Step 5: Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 7: Display the model parameters
print("\nModel Coefficients (impact of each marketing channel on sales):")
print(f"TV: {model.coef_[0]:.3f}")
print(f"Radio: {model.coef_[1]:.3f}")
print(f"Social Media: {model.coef_[2]:.3f}")
print(f"Intercept (baseline sales): {model.intercept_:.3f}")

# Step 8: Evaluate the model performance on test data
r_squared = model.score(X_test, y_test)
print(f"\nR-squared score on test data: {r_squared:.3f}")

# Step 9: (Optional) Plot actual vs predicted sales to visualize model accuracy
y_pred = model.predict(X_test)
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Sales')
plt.ylabel('Predicted Sales')
plt.title('Actual vs Predicted Sales')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'r--')  # diagonal line
plt.show()
