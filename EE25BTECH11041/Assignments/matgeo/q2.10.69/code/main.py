# main.py
import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared object
lib = ctypes.CDLL("./libcalc.so")

# Tell Python about the function signature
lib.quadratic.argtypes = [ctypes.c_double, ctypes.c_double]
lib.quadratic.restype = ctypes.c_double

# Choose a valid c value in (-4/3, 0)
c = -1.0  

# Generate data
x_vals = np.linspace(-10, 10, 400)
y_vals = [lib.quadratic(x, c) for x in x_vals]

# Plot
plt.axhline(0, color='black', linestyle='--')
plt.plot(x_vals, y_vals, label=f"c={c}")
plt.title("Quadratic Condition for Obtuse Angle")
plt.xlabel("x")
plt.ylabel("f(x,c) = c x^2 - 6 c x - 12")
plt.legend()
plt.grid(True)
plt.show()

