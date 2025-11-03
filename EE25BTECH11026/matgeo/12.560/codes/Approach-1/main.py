import sympy as sp
import numpy as np
import ctypes
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL("./libmain.so")

# Function signature
lib.dir_vec.argtypes = (ctypes.c_double,ctypes.c_double,np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"))

# Given point
px, py = 3, 4

# Array to store gradient from C function
grad = np.empty(2, dtype=np.float64)

# Call C function to fill gradient
lib.dir_vec(px, py, grad)

# Normalize to get unit vector
norm_grad = np.linalg.norm(grad)
unit_grad = grad / norm_grad

# Sympy version for pretty print
unit_vec = sp.Matrix(unit_grad)
print("Unit vector along the direction of f:")
sp.pprint(unit_vec)

# Grid for contour plot
xx = np.linspace(-5, 5, 200)
yy = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(xx, yy)
Z = X**2 + Y**2

# Plot contours
plt.figure(figsize=(7,6))
contours = plt.contour(X, Y, Z, levels=20, cmap="viridis")
plt.clabel(contours, inline=True, fontsize=8)

# Mark point (3,4)
plt.scatter(px, py, color="red", label="Point (3,4)")

# Full gradient vector (blue)
plt.quiver(px, py, grad[0], grad[1],angles="xy", scale_units="xy", scale=1, color="blue", width=0.005,label="Full ∇f at (3,4)")

# Unit gradient vector (green)
plt.quiver(px, py, unit_grad[0], unit_grad[1],angles="xy", scale_units="xy", scale=1, color="green", width=0.005,label="Unit ∇f at (3,4)")

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Gradient and Unit Gradient at (3,4) for f(x,y) = x² + y²")
plt.legend()
plt.axis("equal")
plt.savefig("/home/user/Matrix Theory: workspace/Matgeo_assignments/12.560/figs/Figure_1.png")
plt.show()

