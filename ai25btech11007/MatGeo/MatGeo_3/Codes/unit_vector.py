import numpy as np

# Define vectors
a = np.array([1, -7, 7])
b = np.array([3, -2, 2])

# Cross product
n = np.cross(a, b)

# Normalize
unit_n = n / np.linalg.norm(n)

print("Cross product vector n:", n)
print("Unit vector perpendicular to both a and b:", unit_n)
