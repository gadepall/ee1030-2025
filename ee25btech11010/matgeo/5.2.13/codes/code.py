import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL("./code.so")

# Define argtypes and restype for functions
lib.eq1.argtypes = [ctypes.c_double]
lib.eq1.restype = ctypes.c_double

lib.eq2.argtypes = [ctypes.c_double]
lib.eq2.restype = ctypes.c_double

# Generate x values
x_vals = np.linspace(-2, 5, 200)

# Compute y values using C functions
y1_vals = [lib.eq1(float(x)) for x in x_vals]
y2_vals = [lib.eq2(float(x)) for x in x_vals]

# Plot
plt.plot(x_vals, y1_vals, label="2x - 2y = 2")
plt.plot(x_vals, y2_vals, label="4x - 4y = 5")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graph of the two equations")
plt.legend()
plt.grid(True)
plt.savefig("/home/arsh-dhoke/ee1030-2025/ee25btech11010/matgeo/5.2.13/figs/q10.png")
plt.show()
