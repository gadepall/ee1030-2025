import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL('./libellipse.so')

# Define function signature
lib.generate_ellipse.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int,
                                 np.ctypeslib.ndpointer(dtype=np.float64, flags="C_CONTIGUOUS"),
                                 np.ctypeslib.ndpointer(dtype=np.float64, flags="C_CONTIGUOUS")]

# Parameters
a = 4.0  # semi-major axis
b = 2.0  # semi-minor axis
n = 500  # number of points

# Allocate arrays
x = np.zeros(n, dtype=np.float64)
y = np.zeros(n, dtype=np.float64)

# Call C function
lib.generate_ellipse(a, b, n, x, y)

# Plot
plt.plot(x, y)
plt.gca().set_aspect('equal')
plt.title("Ellipse from C Code")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

