import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load C shared library
lib = ctypes.CDLL("./15.so")

# Set return type for circle_radius()
lib.circle_radius.restype = ctypes.c_float

# Call the C function
r = lib.circle_radius()
print("Radius of the circle =", r)

# -------------- Plotting --------------
# Ellipse: x^2/16 + y^2/9 = 1
a = 4
b = 3
x = np.linspace(-a, a, 400)
y_top = b * np.sqrt(1 - (x**2 / a**2))
y_bottom = -y_top

# Foci
c = np.sqrt(a**2 - b**2)
F1 = (c, 0)
F2 = (-c, 0)

# Circle centered at (0, 3) passing through (sqrt(7), 0)
theta = np.linspace(0, 2*np.pi, 200)
x_circ = r * np.cos(theta)
y_circ = 3 + r * np.sin(theta)

# Plot ellipse
plt.plot(x, y_top, 'b', label="Ellipse")
plt.plot(x, y_bottom, 'b')

# Plot circle
plt.plot(x_circ, y_circ, 'r', label="Circle")

# Plot foci and center
plt.scatter([F1[0], F2[0]], [F1[1], F2[1]], color='green', label="Foci")
plt.scatter(0, 3, color='black', label="Circle center (0,3)")

# Equal aspect ratio
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Ellipse and Circle passing through Foci")
plt.grid(True)
plt.legend()
plt.show()