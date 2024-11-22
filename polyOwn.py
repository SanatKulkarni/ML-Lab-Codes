import numpy as np

def pl_regressor(X, y, degree):
    X_poly = np.vander(X, degree + 1, increasing=True)
    return np.linalg.pinv(X_poly) @ y

def main():
    X = np.array(list(map(float, input("Enter X values (comma-separated): ").split(','))))
    y = np.array(list(map(float, input("Enter y values (comma-separated): ").split(','))))
    if len(X) != len(y):
        raise ValueError("X and y must have the same length.")
    theta = pl_regressor(X, y, len(X) - 1)
    print(f"Polynomial coefficients: {theta}")

if __name__ == "__main__":
    main()
