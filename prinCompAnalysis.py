import numpy as np

X = np.array([
    [3.4, 2.1, 4.7, 6.5],
    [7.9, 1.4, 9.2, 5.8],
    [5.3, 8.8, 6.3, 7.4],
    [6.1, 3.7, 2.9, 8.3],
    [4.6, 7.2, 1.6, 9.1]
])

mean_vector = np.mean(X, axis=0)
X_centered = X - mean_vector
covariance_matrix = np.cov(X_centered.T)
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

sorted_indices = np.argsort(eigenvalues)[::-1]
selected_vector = eigenvectors[:, sorted_indices[0]].reshape(-1, 1)

X_pca_1d = X_centered @ selected_vector

print("1D Principal Component Projection Values:\n", X_pca_1d)
