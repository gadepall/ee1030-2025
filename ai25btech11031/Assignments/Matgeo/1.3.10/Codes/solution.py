import numpy as np

# Given points A and B
A = np.array([1, 2])
B = np.array([2, 3])

# Given x-coordinate of P
Px = 8

# Solve for Py using collinearity rank condition:
# (Px - Ax) - (Py - Ay) = 0 => Py = Px - Ax + Ay
Py = Px - A[0] + A[1]
P = np.array([Px, Py])

print(f"Calculated y-coordinate of P: {Py}")
# Calculate ratio k using vector formula
numerator = np.dot(A - P, P - B)
denominator = np.linalg.norm(P - B) ** 2
k = numerator / denominator

print(f"Ratio k in which P divides AB: {k}")