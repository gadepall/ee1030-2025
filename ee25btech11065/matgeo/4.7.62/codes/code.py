import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import ctypes
import os

# --- 1. C Library and Structure Setup ---

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
    c_lib = ctypes.CDLL('./plane_from_point_normal.so')
except OSError:
    print("Error: 'plane_from_point_normal.so' not found.")
    print("Please compile the 'plane_from_point_normal.c' file from the Canvas first.")
    print("Command: gcc -shared -o plane_from_point_normal.so -fPIC plane_from_point_normal.c")
    exit()

c_lib.find_plane_from_point_and_normal.argtypes = [Vector, Vector]
c_lib.find_plane_from_point_and_normal.restype = Plane


# --- 2. Define Input Data from the Question ---

point_A = Vector(5.0, 2.0, -4.0)
normal_n = Vector(2.0, 3.0, -1.0)


# --- 3. Call C Function and Print Results ---

plane_eq = c_lib.find_plane_from_point_and_normal(point_A, normal_n)
print(f"The C function calculated the plane equation:")
print(f"  {plane_eq}")


# --- 4. Plotting ---

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

x_range = np.linspace(0, 10, 20)
y_range = np.linspace(-5, 10, 20)
x_grid, y_grid = np.meshgrid(x_range, y_range)

z_plane = (plane_eq.d - plane_eq.a * x_grid - plane_eq.b * y_grid) / plane_eq.c

ax.plot_surface(x_grid, y_grid, z_plane, alpha=0.6, cmap='plasma', edgecolor='none')

ax.scatter([point_A.x], [point_A.y], [point_A.z], color='red', s=100, label=f'Point A {point_A}')

ax.quiver(
    point_A.x, point_A.y, point_A.z,
    normal_n.x, normal_n.y, normal_n.z,
    length=4, normalize=True, color='black', arrow_length_ratio=0.2,
    label=f'Normal Vector n={normal_n}'
)

# --- 5. Formatting the Plot ---

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title(f'Plane Visualization: {plane_eq}', fontsize=14)
ax.legend()
plt.grid(True)
plt.show()

