import numpy as np
import matplotlib.pyplot as plt

# Given points A and B
A = (5.0, 1.0)
B = (-1.0, 5.0)

# Midpoint of A and B
midpoint = ((A[0] + B[0]) / 2.0, (A[1] + B[1]) / 2.0)

# Function to check 3x = 2y
def is_on_bisector(x, y, tol=1e-9):
    return abs(3*x - 2*y) <= tol

# Points to check
points = [("A", A), ("B", B), ("Midpoint", midpoint)]

# Print results
print("Checking 3x=2y for points:")
for name, p in points:
    print(f"{name:9s}: {p} -> {is_on_bisector(p[0], p[1])}")

# Prepare the line y = (3/2)x
x_vals = np.linspace(-2, 6, 200)
y_vals = (3/2) * x_vals

# Plot the line and points
plt.figure(figsize=(6, 6))
plt.plot(x_vals, y_vals, 'g--', label='3x = 2y (Perp. Bisector)')

# Plot points with labels
for name, p in points:
    plt.scatter(p[0], p[1], label=f"{name} {p}")
    plt.text(p[0] + 0.1, p[1] + 0.1, name)

# Decorations
plt.title("Perpendicular Bisector 3x = 2y")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()

