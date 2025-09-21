import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import ctypes
import os

class Vector(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double),
                ("z", ctypes.c_double)]

    def __repr__(self):
        return f"({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"

class Plane(ctypes.Structure):
    _fields_ = [("a", ctypes.c_double),
                ("b", ctypes.c_double),
                ("c", ctypes.c_double),
                ("d", ctypes.c_double)]

    def __repr__(self):
        return f"{self.a:.2f}x + {self.b:.2f}y + {self.c:.2f}z = {self.d:.2f}"

try:
    c_lib = ctypes.CDLL('./plane_calculator.so')
except OSError:
    print("Error: 'plane_calculator.so' not found.")
    print("Please compile the 'plane_calculator.c' file from the Canvas first.")
    print("Command: gcc -shared -o plane_calculator.so -fPIC plane_calculator.c")
    exit()

c_lib.find_plane_equation.argtypes = [Vector, Vector, Vector]
c_lib.find_plane_equation.restype = Plane

p1 = Vector(2.0, 0.0, 0.0)
p2 = Vector(0.0, 3.0, 0.0)
p3 = Vector(0.0, 0.0, 4.0)

plane_eq = c_lib.find_plane_equation(p1, p2, p3)
print(f"The C function calculated the plane equation:")
print(f"  {plane_eq}")
print("(This is equivalent to 6x + 4y + 3z = 12)")

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

x_range = np.linspace(-1, 4, 20)
y_range = np.linspace(-1, 5, 20)
x_grid, y_grid = np.meshgrid(x_range, y_range)

z_plane = (plane_eq.d - plane_eq.a * x_grid - plane_eq.b * y_grid) / plane_eq.c

ax.plot_surface(x_grid, y_grid, z_plane, alpha=0.6, cmap='viridis', edgecolor='none')

intercepts = np.array([[p1.x, p1.y, p1.z], [p2.x, p2.y, p2.z], [p3.x, p3.y, p3.z]])
ax.scatter(intercepts[:, 0], intercepts[:, 1], intercepts[:, 2], color='red', s=100, label='Intercepts')

triangle_center = intercepts.mean(axis=0)
ax.quiver(
    triangle_center[0], triangle_center[1], triangle_center[2],
    plane_eq.a, plane_eq.b, plane_eq.c,
    length=2, normalize=True, color='black', arrow_length_ratio=0.2,
    label=f'Normal Vector n=[{plane_eq.a:.0f},{plane_eq.b:.0f},{plane_eq.c:.0f}]'
)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title(f'Plane Visualization: {plane_eq}', fontsize=14)
ax.set_xlim([0, 5]); ax.set_ylim([0, 5]); ax.set_zlim([0, 5])
ax.legend()
plt.grid(True)
plt.show()


