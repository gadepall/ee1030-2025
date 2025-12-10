import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL('./code.so')

# Define the argument and return types for the C function
# This ensures that Python passes data correctly to C
lib.find_optimal_x.restype = ctypes.c_double
lib.find_optimal_x.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C'),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C'),
    ctypes.c_int
]

# --- Main part of the script ---

# 1. Define vectors from the problem statement
# Use float64 to match the 'double' type in C
a = np.array([1.0, 1.0], dtype=np.float64)
b = np.array([0.0, 3 * np.sqrt(2)], dtype=np.float64)
vector_size = len(a)

# 2. Call the C function to find the value of x
x_opt = lib.find_optimal_x(a, b, vector_size)

print(f"The value of x calculated by the C function is: {x_opt}")

# 3. Use the result to plot the solution
proj_b_on_a = x_opt * a

plt.figure(figsize=(8, 8))
plt.plot([-a[0], 2*a[0]], [-a[1], 2*a[1]], 'r-', label='Line defined by vector a')
plt.quiver(0, 0, b[0], b[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector b')
plt.quiver(0, 0, proj_b_on_a[0], proj_b_on_a[1], angles='xy', scale_units='xy', scale=1, color='g', label='Projection ax')
plt.quiver(proj_b_on_a[0], proj_b_on_a[1], b[0] - proj_b_on_a[0], b[1] - proj_b_on_a[1], angles='xy', scale_units='xy', scale=1, color='purple', label='Residual r = b - ax')

plt.plot(b[0], b[1], 'bo')
plt.plot(proj_b_on_a[0], proj_b_on_a[1], 'go')
plt.text(b[0] + 0.1, b[1], f'b ({b[0]:.2f}, {b[1]:.2f})')
plt.text(proj_b_on_a[0] + 0.1, proj_b_on_a[1], f'ax ({proj_b_on_a[0]:.2f}, {proj_b_on_a[1]:.2f})')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()
plt.savefig('../figs/fig2.png')
