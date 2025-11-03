import numpy as np

# Given points
A = np.array([3, -4, -5], dtype=float)
B = np.array([2, -3,  1], dtype=float)
P = np.array([1,  2,  3], dtype=float)
Q = np.array([4,  2, -3], dtype=float)
R = np.array([0,  4,  3], dtype=float)

# Direction vector of line
AB = B - A

# Normal vector of plane (cross product of PQ and PR)
n = np.cross(Q - P, R - P)

# Equation of plane: n · (X - P) = 0
# Substitute X = A + t*(B - A)
t = np.dot(n, P - A) / np.dot(n, AB)

# Intersection point
C = A + t * AB

print("Normal vector to plane:", n)
print("Intersection point C:", C)
