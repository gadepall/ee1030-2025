import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load C library
lib = ctypes.CDLL("./libcurve_solver.so")

# Function signatures
lib.curve.restype = ctypes.c_double
lib.curve.argtypes = [ctypes.c_double]
lib.tangent.restype = ctypes.c_double
lib.tangent.argtypes = [ctypes.c_double]
lib.normal.restype = ctypes.c_double
lib.normal.argtypes = [ctypes.c_double]
lib.print_equations.restype = None

# Print equations once
lib.print_equations()

# Define helper wrappers for numpy arrays
def curve(x):
    return np.array([lib.curve(float(val)) for val in x])

def tangent(x):
    return np.array([lib.tangent(float(val)) for val in x])

def normal(x):
    return np.array([lib.normal(float(val)) for val in x])

# Split domain around asymptotes
x_vals1 = np.linspace(-2, 1.9, 200)
x_vals2 = np.linspace(2.1, 2.9, 200)
x_vals3 = np.linspace(3.1, 12, 200)

y_vals1 = curve(x_vals1)
y_vals2 = curve(x_vals2)
y_vals3 = curve(x_vals3)

# Tangent & normal
x0, y0 = 7, 0
x_line = np.linspace(4, 10, 200)
y_tan = tangent(x_line)
y_norm = normal(x_line)

# Plot
plt.figure(figsize=(8,6))
plt.plot(x_vals1, y_vals1, 'b')
plt.plot(x_vals2, y_vals2, 'b')
plt.plot(x_vals3, y_vals3, 'b', label="Curve y=(x-7)/((x-2)(x-3))")
plt.plot(x_line, y_tan, 'r--', label="Tangent at (7,0)")
plt.plot(x_line, y_norm, 'g--', label="Normal at (7,0)")
plt.scatter([x0], [y0], color='k', zorder=5)
plt.text(x0+0.2, y0+0.2, "(7,0)")
plt.axhline(0, color='gray', lw=1)
plt.axvline(0, color='gray', lw=1)
plt.ylim(-2, 2)
plt.xlim(-2, 12)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Curve with Tangent and Normal at (7,0)")
plt.grid(True)
plt.savefig("/home/user/Matrix Theory: workspace/Matgeo_assignments/10.4.2/figs/figure_1.png")
plt.show()

