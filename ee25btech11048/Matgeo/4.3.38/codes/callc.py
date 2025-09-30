import ctypes
import os
import numpy as np
import matplotlib.pyplot as plt

# for saving figure in figs folder
figs_folder = os.path.join("..", "figs")
os.makedirs(figs_folder, exist_ok=True)  # ensure folder exists

# loading the shared object
lib = ctypes.CDLL("./points.so")

# defining the return type and arg type
lib.gaussian_elimination.restype = ctypes.POINTER(ctypes.c_double)
lib.gaussian_elimination.argtypes = [((ctypes.c_double*4)*3)]

# defining the augmented matrix for your system
aug_matrix = ((ctypes.c_double*4)*3)()
aug_matrix[0][:] = [5, -1, 4, 5]
aug_matrix[1][:] = [2,  3, 5, 2]
aug_matrix[2][:] = [5, -2, 6, -1]

# calling the C function
sol = lib.gaussian_elimination(aug_matrix)
solution = [sol[i] for i in range(3)]
x, y, z = solution
print("Solution from C:", solution)  # should print [3.0, 2.0, -2.0]

# create meshgrid for plotting planes
x_vals = np.linspace(-10, 10, 100)
y_vals = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x_vals, y_vals)

# Plane 1 : 5x - y + 4z = 5 -> z = (5 - 5*X + Y)/4
Z1 = (5 - 5*X + Y) / 4

# Plane 2 : 2x + 3y + 5z = 2 -> z = (2 - 2*X - 3*Y)/5
Z2 = (2 - 2*X - 3*Y) / 5

# Plane 3 : 5x - 2y + 6z = -1 -> z = (-1 - 5*X + 2*Y)/6
Z3 = (-1 - 5*X + 2*Y) / 6

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

# Plot the planes
ax.plot_surface(X, Y, Z1, alpha=0.5, color="red")
ax.plot_surface(X, Y, Z2, alpha=0.5, color="green")
ax.plot_surface(X, Y, Z3, alpha=0.5, color="blue")

# Plot the solution point
ax.scatter(x, y, z, color="black", s=50)
ax.text(x+0.5, y+0.5, z+0.5, f"P({x:.2f},{y:.2f},{z:.2f})",
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

