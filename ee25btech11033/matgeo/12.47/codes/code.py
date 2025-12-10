

import ctypes
import os
import numpy as np
import matplotlib.pyplot as plt

# --- Step 1: Load C library and prepare the function call ---


c_lib = ctypes.CDLL('./code.so')

# Get the function from the library
solve_k_func = c_lib.solve_for_k_in_pos33

# Define the data types for the function's arguments (8 doubles)
solve_k_func.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                       ctypes.c_double, ctypes.c_double, ctypes.c_double,
                       ctypes.c_double, ctypes.c_double]

# Define the function's return type
solve_k_func.restype = ctypes.c_double

# --- Step 2: Define inputs and call the C function ---

# [cite_start]Define the 8 constant coefficients from the problem matrix [cite: 5, 6, 7]
# | 1  1  1 | -> a, b, c
# | 1  2  3 | -> d, e, f
# | 1  4  k | -> g, h
a, b, c = 1.0, 1.0, 1.0
d, e, f = 1.0, 2.0, 3.0
g, h    = 1.0, 4.0

# Call the C function with the matrix coefficients as input
k = solve_k_func(a, b, c, d, e, f, g, h)

print(f"Value of k (calculated in C with inputs from Python): {k}")


# --- Step 3: Plot the planes using the returned value of k ---

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

x_range = np.linspace(-5, 10, 50)
y_range = np.linspace(-5, 10, 50)
X, Y = np.meshgrid(x_range, y_range)

# [cite_start]Define the three planes from the source document [cite: 5, 6, 7]
Z1 = (3 - X - Y)
Z2 = (4 - X - 2*Y) / 3
if k != 0:
    Z3 = (6 - X - 4*Y) / k
else:
    Z3 = np.zeros_like(X)

# Plot the surfaces
ax.plot_surface(X, Y, Z1, alpha=0.6, color='skyblue')
ax.plot_surface(X, Y, Z2, alpha=0.6, color='salmon')
ax.plot_surface(X, Y, Z3, alpha=0.6, color='lightgreen')

# Plot the line of intersection
t = np.linspace(-5, 5, 100)
x_line = 2 + t
y_line = 1 - 2 * t
z_line = t
ax.plot(x_line, y_line, z_line, color='black', linewidth=3)

# Formatting
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.view_init(elev=20, azim=-50)

plt.show()
