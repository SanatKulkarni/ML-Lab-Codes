import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv('employee_salary_dataset.csv')
X, y = df[['Years of Experience']].values, df['Salary'].values

for degree in range(1, 6):
    X_poly = PolynomialFeatures(degree).fit_transform(X)
    model = LinearRegression().fit(X_poly, y)
    y_pred = model.predict(X_poly)

    print(f'\nDegree {degree} | MSE: {mean_squared_error(y, y_pred):.2f}')
    print(f'Coefficients: {model.coef_}, Intercept: {model.intercept_}')
