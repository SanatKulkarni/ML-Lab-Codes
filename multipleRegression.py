import numpy as np

def mul_regression_manual(X, y):
    X = np.column_stack((np.ones(len(X)), X))  
    X_transpose = X.T
    XTX = X_transpose @ X
    XTy = X_transpose @ y
    XTX_inv = np.linalg.pinv(XTX)
    B = XTX_inv @ XTy  
    return B, 

num_features = int(input())
X = [list(map(float, input().split())) for _ in range(num_features)]
X = np.array(X).T
y = np.array(list(map(float, input().split())))

B = mul_regression_manual(X, y)
print("Coefficients (B):")
print(B)

