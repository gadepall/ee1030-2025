import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load the compiled shared object file
lib = ctypes.CDLL("./formula.so")

# Define function argument types
lib.ellipse.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64),  # theta array
    np.ctypeslib.ndpointer(dtype=np.float64),  # x output array
    np.ctypeslib.ndpointer(dtype=np.float64),  # y output array
    ctypes.c_int,                              # number of points
    ctypes.c_double,                           # a
    ctypes.c_double                            # b
]

# Ellipse parameters
a = 2.0   # semi-major axis
b = 1.0   # semi-minor axis
n = 400

# Create arrays
theta = np.linspace(0, 2*np.pi, n)
x = np.zeros(n)
y = np.zeros(n)

# Call C function
lib.ellipse(theta, x, y, n, a, b)

# Plot
plt.figure(figsize=(6,6))
plt.plot(x, y, 'g', linewidth=2, label=r'$4x^2 + y^2 = 4$')
plt.axhline(0, color='k', linewidth=0.8)
plt.axvline(0, color='k', linewidth=0.8)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Ellipse: $4x^2 + y^2 = 4$')
plt.xlabel('X - axis')
plt.ylabel('Y - axis')
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()