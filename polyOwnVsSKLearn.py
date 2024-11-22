import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load dataset
df = pd.read_csv('/content/emp.csv')
X = df['Years of Experience'].values
y = df['Salary'].values

# First Code: Manual Polynomial Regression
def pl_regressor(X, y, degree):
    X_poly = np.vander(X, degree + 1, increasing=True)
    return np.linalg.pinv(X_poly) @ y

print("Manual Polynomial Regression Results:")
for degree in range(1, 6):
    X_poly = np.vander(X, degree + 1, increasing=True)
    theta = pl_regressor(X, y, degree)
    y_pred = X_poly @ theta
    mse = mean_squared_error(y, y_pred)
    print(f'\nDegree {degree}')
    print(f'Coefficients: {theta[:-1]}, Intercept: {theta[-1]}')
    print(f'Mean Squared Error (MSE): {mse:.2f}')

# Second Code: Sklearn Polynomial Regression
print("\nScikit-learn Polynomial Regression Results:")
for degree in range(1, 6):
    X_reshaped = X.reshape(-1, 1)  # Reshape for sklearn
    X_poly = PolynomialFeatures(degree).fit_transform(X_reshaped)
    model = LinearRegression().fit(X_poly, y)
    y_pred = model.predict(X_poly)
    mse = mean_squared_error(y, y_pred)
    print(f'\nDegree {degree}')
    print(f'Coefficients: {model.coef_}, Intercept: {model.intercept_}')
    print(f'Mean Squared Error (MSE): {mse:.2f}')
