# main.py
import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared object
lib = ctypes.CDLL("./libparabola.so")

# Define function prototype
lib.generate_points.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    ctypes.c_int
]
lib.generate_points.restype = ctypes.c_int

# Allocate arrays
n = 4000
x = np.zeros(n, dtype=np.float64)
y = np.zeros(n, dtype=np.float64)

# Call the C function
count = lib.generate_points(x, y, n)

# Slice to actual filled points
x = x[:count]
y = y[:count]

# Plot parabola
plt.figure(figsize=(6,6))
plt.scatter(x, y, s=5, c='b', label=r"$y^2=-8x$")
plt.axhline(0, color='k', linewidth=0.8)
plt.axvline(0, color='k', linewidth=0.8)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Parabola: $y^2 = -8x$")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.show()
