import numpy as np

def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((np.array(point1) - np.array(point2))**2))

def manhattan_distance(point1, point2):
    return np.sum(np.abs(np.array(point1) - np.array(point2)))

def minkowski_distance(point1, point2, p):
    return np.sum(np.abs(np.array(point1) - np.array(point2))**p)**(1/p)

point1 = list(map(float, input("Enter the coordinates of point1 (comma-separated): ").split(',')))
point2 = list(map(float, input("Enter the coordinates of point2 (comma-separated): ").split(',')))
p = float(input("Enter the value of p for Minkowski distance: "))

print("Euclidean Distance:", euclidean_distance(point1, point2))
print("Manhattan Distance:", manhattan_distance(point1, point2))
print("Minkowski Distance:", minkowski_distance(point1, point2, p))
