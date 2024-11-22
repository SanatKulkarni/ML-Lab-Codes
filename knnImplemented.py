import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv('./irisDataset.csv')
X = data[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]
y = data['variety']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

best_k, best_accuracy = 0, 0
for k in range(1, 11):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    accuracy = accuracy_score(y_test, knn.predict(X_test))
    if accuracy > best_accuracy:
        best_accuracy, best_k = accuracy, k

print(f'Best K: {best_k}, Accuracy: {best_accuracy:.2f}')
