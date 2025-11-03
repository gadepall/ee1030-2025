import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the compiled C library
lib = ctypes.CDLL("./poly.so")
lib.base_factor.restype = ctypes.c_double

# Define a Python wrapper around the C function
def f(x):
    return lib.base_factor(ctypes.c_double(x))

# Generate values
xs = np.linspace(-1, 8, 600)
ys = [f(x) for x in xs]

# Known fixed roots
roots = np.array([1.0, 0.5, 5.0, 7.0, 3.0, 4.0])

# Plot
plt.plot(xs, ys, label="f(x) = (x-1)(x-0.5)(x-5)(x-7)(x-3)(x-4)")
plt.scatter(roots, np.zeros_like(roots), color="red", label="Fixed roots")
plt.axhline(0, color="black", linewidth=0.5)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Base Factor Polynomial with Fixed Roots")
plt.legend()
plt.savefig("poly_dim.png")
plt.show()

