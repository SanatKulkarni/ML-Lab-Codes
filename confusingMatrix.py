import numpy as np

def confusion_matrix(y_true, y_pred):
    classes = np.unique(y_true)
    matrix = np.zeros((len(classes), len(classes)), dtype=int)
    for i in range(len(y_true)):
        matrix[classes == y_true[i], classes == y_pred[i]] += 1
    return matrix

def accuracy(y_true, y_pred):
    return np.mean(np.array(y_true) == np.array(y_pred))

def precision(y_true, y_pred):
    matrix = confusion_matrix(y_true, y_pred)
    return np.diag(matrix) / np.sum(matrix, axis=0)

def recall(y_true, y_pred):
    matrix = confusion_matrix(y_true, y_pred)
    return np.diag(matrix) / np.sum(matrix, axis=1)

def f1_score(y_true, y_pred):
    p, r = precision(y_true, y_pred), recall(y_true, y_pred)
    return 2 * (p * r) / (p + r)

y_true = list(map(int, input("Enter true labels: ").split(',')))
y_pred = list(map(int, input("Enter predicted labels: ").split(',')))

conf_matrix = confusion_matrix(y_true, y_pred)
acc = accuracy(y_true, y_pred)
prec = precision(y_true, y_pred)
rec = recall(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print(f"Confusion Matrix:\n{conf_matrix}")
print(f"Accuracy: {acc:.2f}")
print(f"Precision: {prec}")
print(f"Recall: {rec}")
print(f"F1 Score: {f1}")
