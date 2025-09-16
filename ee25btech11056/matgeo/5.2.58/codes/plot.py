import os
import numpy as np
import matplotlib.pyplot as plt

# for saving figure in figs folder
figs_folder = os.path.join("..", "figs")

# Define system of equations
# 1*x -1*y +1*z = 4
# 2*x +1*y -3*z = 0
# 1*x +1*y +1*z = 2

A = np.array([[1, -1, 1],
              [2,  1, -3],
              [1,  1,  1]], dtype=float)

b = np.array([4, 0, 2], dtype=float)

# Solve using numpy
solution = np.linalg.solve(A, b)
x, y, z = solution
print("Solution from NumPy:", solution)

# Create meshgrid for plotting planes
x_vals = np.linspace(-10, 10, 100)
y_vals = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x_vals, y_vals)

# Plane 1: x - y + z = 4 -> z = 4 - x + y
Z1 = 4 - X + Y

# Plane 2: 2x + y - 3z = 0 -> z = (2x + y)/3
Z2 = (2*X + Y) / 3

# Plane 3: x + y + z = 2 -> z = 2 - x - y
Z3 = 2 - X - Y

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

