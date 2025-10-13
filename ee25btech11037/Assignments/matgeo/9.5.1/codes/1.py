import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared object file
lib = ctypes.CDLL("./mat.so")

# Define argument and return types
lib.roots.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                      ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.roots.restype = None

# Quadratic coefficients
a, b, c = 1.0, 3.0, -10.0   # Example: x^2 - 3x + 2

# Variables to store results
x1 = ctypes.c_double()
x2 = ctypes.c_double()

# Call C function
lib.roots(a, b, c, ctypes.byref(x1), ctypes.byref(x2))

# Extract roots
r1, r2 = x1.value, x2.value
print(f"Roots from C function: A=({r1},0), B=({r2},0)")

# Plot parabola
x_vals = np.linspace(min(r1, r2) - 2, max(r1, r2) + 2, 400)
y_vals = a * x_vals**2 + b * x_vals + c

plt.axhline(0, color="black", linewidth=0.8)  # x-axis
plt.axvline(0, color="black", linewidth=0.8)  # y-axis

# Plot parabola with label
plt.plot(x_vals, y_vals, label=f"$y = {a}x^2 + {b}x + {c}$", color="blue")

# Mark roots
plt.scatter([r1, r2], [0, 0], color="red", zorder=5)

# Add labels near the roots
plt.text(r1, -0.5, f"A({r1:.2f}, 0)", fontsize=11, color="red", ha="center")
plt.text(r2, -0.5, f"B({r2:.2f}, 0)", fontsize=11, color="red", ha="center")

plt.title("Quadratic Curve and Roots")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.savefig('1.png')
plt.show()

