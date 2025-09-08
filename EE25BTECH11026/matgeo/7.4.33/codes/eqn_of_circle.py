import ctypes
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp
mp.use("TkAgg")

# Load C library
lib = ctypes.CDLL("./circle_equation.so")

# Define argument types
lib.circle_equation.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                ctypes.c_double, ctypes.c_double, ctypes.c_double]

# Define return type (void)
lib.circle_equation.restype = None

# Inputs (line: sqrt(3)x + y - 6 = 0, D=(3√3/2, 3/2), r=1)
a, b, c = np.sqrt(3), 1, -6
xd, yd = 3*np.sqrt(3)/2, 3/2
r = 1

# Call C function (prints result)
lib.circle_equation(a, b, c, xd, yd, r)

# ---- Plotting after computing manually in Python (center known: (√3,1)) ----
h, k = np.sqrt(3), 1

theta = np.linspace(0, 2*np.pi, 500)
x_circle = h + r*np.cos(theta)
y_circle = k + r*np.sin(theta)

# Line PQ
x_vals = np.linspace(0, 6, 200)
y_vals = -(a*x_vals + c)/b

# Tangency point D
D = np.array([xd, yd])

plt.figure(figsize=(6,6))
plt.plot(x_circle, y_circle, label="Circle C")
plt.plot(x_vals, y_vals, label="Line PQ")
plt.scatter(*D, color="red", label="Tangency D")
plt.scatter(h, k, color="black", label="Center O")

plt.axis("equal")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.title("Circle Plot")
plt.savefig("/home/user/Matrix/Matgeo_assignments/7.4.33/figs/Figure_1")
plt.show()

