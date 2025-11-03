import os
import numpy as np
import matplotlib.pyplot as plt

# for saving figure in figs folder
figs_folder = os.path.join("..", "figs")

# Define system of equations
# 5x - y + 4z = 5
# 2x + 3y + 5z = 2
# 5x - 2y + 6z = -1

A = np.array([[5, -1,  4],
              [2,  3,  5],
              [5, -2,  6]], dtype=float)

b = np.array([5, 2, -1], dtype=float)

# Solve using numpy
solution = np.linalg.solve(A, b)
x, y, z = solution
print("Solution from NumPy:", solution)

# Create meshgrid for plotting planes
x_vals = np.linspace(-10, 10, 100)
y_vals = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x_vals, y_vals)

# Plane 1: 5x - y + 4z = 5  ->  z = (5 - 5x + y)/4
Z1 = (5 - 5*X + Y) / 4

# Plane 2: 2x + 3y + 5z = 2 ->  z = (2 - 2x - 3y)/5
Z2 = (2 - 2*X - 3*Y) / 5

# Plane 3: 5x - 2y + 6z = -1 -> z = (-1 - 5x + 2y)/6
Z3 = (-1 - 5*X + 2*Y) / 6

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

# Plot the planes
ax.plot_surface(X, Y, Z1, alpha=0.5, color="red")
ax.plot_surface(X, Y, Z2, alpha=0.5, color="green")
ax.plot_surface(X, Y, Z3, alpha=0.5, color="blue")

# Plot the solution point
ax.scatter(x, y, z, color="black")
ax.text(x+0.5, y+0.5, z+0.5,
        f"P({x:.2f},{y:.2f},{z:.2f})",
        fontsize=10, color="black")

# Axes labels and title
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Intersection of Three Planes and Solution Point P")
ax.grid(True)

# Save figure
plt.tight_layout()
fig.savefig(os.path.join(figs_folder, "solution.png"))
plt.show()

