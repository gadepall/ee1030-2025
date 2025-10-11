import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load compiled C library
lib = ctypes.CDLL("./libellipse.so")

# Define argument and return types
lib.ellipse_point.argtypes = [ctypes.c_double, ctypes.c_double,
                              ctypes.c_double,
                              ctypes.POINTER(ctypes.c_double),
                              ctypes.POINTER(ctypes.c_double)]

# Semi-axes
a = 3.0
b = np.sqrt(5.0)

# Generate ellipse points
theta_vals = np.linspace(0, 2*np.pi, 400)
x_vals, y_vals = [], []

for theta in theta_vals:
    x = ctypes.c_double()
    y = ctypes.c_double()
    lib.ellipse_point(a, b, theta, ctypes.byref(x), ctypes.byref(y))
    x_vals.append(x.value)
    y_vals.append(y.value)

# Plot ellipse
plt.plot(x_vals, y_vals, label=r'$\dfrac{x^2}{9} + \dfrac{y^2}{5} = 1$')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Ellipse Locus")
plt.grid(True)
plt.legend(loc="upper right")
plt.axis("equal")
plt.show()