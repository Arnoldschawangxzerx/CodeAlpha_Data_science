# 1. Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 2. Load dataset
df = pd.read_csv("car_data.csv")   # change name if needed
df.head()

# 3. Basic exploration
print(df.info())
print(df.describe())

# 4. Data cleaning
df = df.dropna()   # remove missing values

# Convert categorical columns using one-hot encoding
df = pd.get_dummies(df, drop_first=True)

# 5. Define features and target
X = df.drop("Selling_Price", axis=1)  # Target column
y = df["Selling_Price"]

# 6. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 7. Train regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 8. Predictions
y_pred = model.predict(X_test)

# 9. Model evaluation
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# 10. Visualization
plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted Car Prices")
plt.show()
