import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the C library
lib = ctypes.CDLL("./linear.so")

# Define array size
n = 400
x = np.linspace(-10, 10, n)

# Create empty arrays for y1, y2
y1 = np.zeros(n, dtype=np.double)
y2 = np.zeros(n, dtype=np.double)

# Convert numpy arrays to ctypes pointers
lib.compute_lines.argtypes = [np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS"),
                              np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS"),
                              np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS"),
                              ctypes.c_int]

lib.compute_lines(x, y1, y2, n)
# Plot the results
plt.plot(x, y1, label="2x + 3y - 8 = 0")
plt.plot(x, y2, label="4x + 6y - 7 = 0")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot using C computations via ctypes")
plt.grid(True)
plt.legend()
plt.show()