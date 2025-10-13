import numpy as np
import ctypes
import matplotlib.pyplot as plt

# Load shared C library
lib = ctypes.CDLL("./libcode.so")

# Define argument types
lib.solve_planes.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS")
]

# Coefficient matrix and constants
A = np.array([[1, -1, 2],
              [2,  1, 4],
              [1,  3, 1]], dtype=np.double)
b = np.array([4, 8, 3], dtype=np.double)
x = np.zeros(3, dtype=np.double)

# Call C function
lib.solve_planes(A.ravel(), b, x)
print("Point of intersection (x1, x2, x3):", x)

# --- Plotting ---
x_vals = np.linspace(-5, 5, 30)
y_vals = np.linspace(-5, 5, 30)
X, Y = np.meshgrid(x_vals, y_vals)

# Plane equations rearranged for z
Z1 = (4 - X + Y) / 2
Z2 = (8 - 2*X - Y) / 4
Z3 = 3 - X - 3*Y

fig = plt.figure(figsize=(9, 7))
ax = plt.axes(projection='3d')

# Plot each plane
ax.plot_surface(X, Y, Z1, alpha=0.5, color='red')
ax.plot_surface(X, Y, Z2, alpha=0.5, color='green')
ax.plot_surface(X, Y, Z3, alpha=0.5, color='blue')

# Plot intersection point
ax.scatter(x[0], x[1], x[2], color='black', s=60)
ax.text(x[0], x[1], x[2]+0.3, f'({x[0]:.1f}, {x[1]:.1f}, {x[2]:.1f})', color='black')

# Labels and title
ax.set_xlabel('x₁')
ax.set_ylabel('x₂')
ax.set_zlabel('x₃')
ax.set_title('Intersection of Three Planes')

colors = ['red', 'green', 'blue', 'black']
labels = [
    'x₁ - x₂ + 2x₃ = 4',
    '2x₁ + x₂ + 4x₃ = 8',
    'x₁ + 3x₂ + x₃ = 3',
    'Intersection (2, 0, 1)'
]

handles = [plt.Line2D([0], [0], color=c, lw=4) for c in colors]
ax.legend(handles, labels)
plt.savefig("/mnt/c/Users/bharg/Documents/backupmatrix/ee25btech11013/matgeo/12.235/figs/Figure_1.png")
plt.show()
