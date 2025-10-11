import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL('./code.so')

# Tell Python about the argument and return types
lib.plane_equation.argtypes = (ctypes.c_double, ctypes.c_double, ctypes.c_double)
lib.plane_equation.restype = ctypes.c_double

# Example point (a,b,c) that lies on the plane
a, b, c = 2.0, 1.0,-3.0

# Use C function to calculate d = a+b+c
d = lib.plane_equation(a, b, c)
print(f"Plane equation: x + y + z = {d}")

# Define a meshgrid for x and y
x_vals = np.linspace(-5, 5, 50)
y_vals = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x_vals, y_vals)

# Solve for Z using x + y + z = d
Z = d - X - Y

# Plot the plane
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, alpha=0.7, color="lightblue", edgecolor='k')

# Plot the example point
ax.scatter(a, b, c, color='red', s=50, label=f'Point ({a},{b},{c})')

# Label axes
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title(f"Plane: x + y + z = {d}")

plt.legend()
plt.savefig("/home/arsh-dhoke/ee1030-2025/ee25btech11010/matgeo/4.5.12/figs/q7.png")
plt.show()
