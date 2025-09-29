import numpy as np
import matplotlib.pyplot as plt

# Function to read a point from user
def read_point(name):
    coords = input(f"Enter coordinates of {name} (x y z): ").split()
    return np.array(list(map(float, coords)))

# Input points
A = read_point("A")
B = read_point("B")
C = read_point("C")
D = read_point("D")

# Vectors
AB = B - A
CD = D - C

# Step 1: Angle between AB and CD
dot_product = np.dot(AB, CD)
norms = np.linalg.norm(AB) * np.linalg.norm(CD)
cos_theta = dot_product / norms
x = cos_theta*100
y = int(x)/100
theta_deg = np.degrees(np.arccos(y))

# Step 2: Rank method for collinearity
M = np.column_stack((AB, CD))   # Matrix with AB and CD as columns
rank = np.linalg.matrix_rank(M)

# Print results
print("\n--- Results ---")
print("Vector AB:", AB)
print("Vector CD:", CD)
print("Dot product =", dot_product)
print("cos(theta) =", y)
print("Angle between AB and CD =", theta_deg, "degrees")

if rank == 1:
    print("Vectors AB and CD are collinear.")
else:
    print("Vectors AB and CD are not collinear.")
