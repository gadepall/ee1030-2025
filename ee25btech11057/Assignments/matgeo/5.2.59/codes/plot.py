import os
import numpy as np
import matplotlib.pyplot as plt

# for saving figure in figs folder
figs_folder = os.path.join("..", "figs")

# Define system of equations
# 2*x +3*y +3*z = 5
# 1*x -2*y +1*z = -4
# 3*x -1*y -2*z = 3

A = np.array([[2, 3, 3],
              [1, -2, 1],
              [3, -1, -2]], dtype=float)

b = np.array([5, -4, 3], dtype=float)

# Solve using numpy
solution = np.linalg.solve(A, b)
x, y, z = solution
print("Solution from NumPy:", solution)

# Create meshgrid for plotting planes
x_vals = np.linspace(-10, 10, 100)
y_vals = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x_vals, y_vals)

# Plane 1: 2x + 3y + 3z = 5 -> z = (5 - 2x - 3y)/3
Z1 = (5 - 2*X - 3*Y)/3

# Plane 2: x - 2y + z = -4 -> z = (-4 -x + 2y)
Z2 =(-4 -X +2*Y)

# Plane 3: 3x - y - 2z = 3 -> z = (-3 + 3x - y )/2
Z3 = (-3 + 3*X - Y)/2

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

