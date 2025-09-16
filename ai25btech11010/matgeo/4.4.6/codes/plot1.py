import numpy as np
from fractions import Fraction
import matplotlib.pyplot as plt
import os

# Create figs folder if it doesn't exist
os.makedirs("figs", exist_ok=True)

# Define points
A = np.array([2, 5, -3])
B = np.array([-2, -3, 5])
C = np.array([5, 3, -3])

# Coefficient matrix
M = np.array([A, B, C])
b = np.array([1, 1, 1])

# Solve for normal vector n (float)
n_float = np.linalg.solve(M, b)

# Convert to fractions
n_frac = [Fraction(x).limit_denominator() for x in n_float]

# Display normal vector as column matrix
print("Normal vector n (column matrix in fractions):")
for val in n_frac:
    print(f"| {val} |")

# Plane equation in fraction form
x, y, z = 'x', 'y', 'z'
eq_terms = [f"{val}*{var}" for val, var in zip(n_frac, [x, y, z])]
plane_eq = " + ".join(eq_terms) + " = 1"
print("\nEquation of the plane (n^T x = 1) in fractions:")
print(plane_eq)

# ----------------- Plotting -----------------
n1, n2, n3 = n_float  # Use float for plotting

# Create grid
xx = np.linspace(-5, 5, 20)
yy = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(xx, yy)

# Solve for Z from plane equation
Z = (1 - n1*X - n2*Y) / n3

# Plotting
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, alpha=0.5, color='cyan', rstride=1, cstride=1)

# Plot points
points = {'A': A, 'B': B, 'C': C}
colors = {'A': 'red', 'B': 'green', 'C': 'blue'}

for label, point in points.items():
    ax.scatter(*point, color=colors[label], s=50, label=label)
    # Annotate with coordinates
    ax.text(point[0], point[1], point[2], f'{label}{tuple(point)}', color=colors[label])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.title("Plane passing through points A, B, C")

# Save figure in figs folder
plt.savefig("../figs/plane_plot.png")
plt.show()
