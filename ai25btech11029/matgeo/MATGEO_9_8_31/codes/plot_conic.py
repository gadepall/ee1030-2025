import ctypes
import matplotlib.pyplot as plt
import numpy as np

# Load shared object
lib = ctypes.CDLL('./libconic.so')

# Define return type and argument
class Intersection(ctypes.Structure):
    _fields_ = [("x1", ctypes.c_double),
                ("y1", ctypes.c_double),
                ("x2", ctypes.c_double),
                ("y2", ctypes.c_double)]

lib.solve_conic.restype = Intersection
lib.solve_conic.argtypes = [ctypes.c_double]

# Solve for p
p = 2.0
result = lib.solve_conic(p)

print(f"Intersection points: ({result.x1:.2f}, {result.y1:.2f}) and ({result.x2:.2f}, {result.y2:.2f})")

# Plot parabola y^2 = 2px
x_vals = np.linspace(-1, 5, 400)
y_vals_pos = np.sqrt(2 * p * x_vals)
y_vals_neg = -y_vals_pos

# Plot circle
theta = np.linspace(0, 2 * np.pi, 400)
r = p
h = p / 2
k = 0
circle_x = h + r * np.cos(theta)
circle_y = k + r * np.sin(theta)

# Plot
plt.plot(x_vals, y_vals_pos, 'b', label='Parabola')
plt.plot(x_vals, y_vals_neg, 'b')
plt.plot(circle_x, circle_y, 'g', label='Circle')
plt.plot([result.x1, result.x2], [result.y1, result.y2], 'ro', label='Intersections')
plt.legend()
plt.axis('equal')
plt.title('Intersection of Parabola and Circle')
plt.grid(True)
plt.show()

