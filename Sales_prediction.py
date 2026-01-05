import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
# Load dataset
df = pd.read_csv("sales_data.csv")  # Change filename if needed
df.head()
df.info()
df.describe()
# Check missing values
df.isnull().sum()
# Fill numeric missing values with mean
df.fillna(df.mean(numeric_only=True), inplace=True)
# Convert categorical columns into numerical
df = pd.get_dummies(df, drop_first=True)
df.head()
# Separate features and target
X = df.drop("Sales", axis=1)
y = df["Sales"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error (MAE):", mae)
print("Root Mean Squared Error (RMSE):", rmse)
print("R2 Score:", r2)
impact = pd.DataFrame({
    "Feature": X.columns,
    "Impact": model.coef_
}).sort_values(by="Impact", ascending=False)

impact
plt.figure(figsize=(8,5))
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")
plt.show()
# Predict sales for a new advertising strategy (sample)
sample_input = X.iloc[:1]
future_sales = model.predict(sample_input)

print("Predicted Future Sales:", future_sales[0])


