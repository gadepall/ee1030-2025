import ctypes
import os
import subprocess
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- 1. Compile C Code into a Shared Library ---
# This ensures the latest version of the C code is always used.
# This version assumes a C compiler is available in the system's PATH.


# --- 2. Define Interface with the C Library ---

# Define a Python class that mirrors the C Point3D struct
class Point3D(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double),
                ("z", ctypes.c_double)]

# Load the compiled dynamic link library
solver_lib = ctypes.CDLL('./c8_functions.dll')

# Define argument and return types for the C functions for type safety
# get_intersection_and_distance(Point3D* p, Point3D* q) -> double
solver_lib.get_intersection_and_distance.argtypes = [ctypes.POINTER(Point3D), ctypes.POINTER(Point3D)]
solver_lib.get_intersection_and_distance.restype = ctypes.c_double

# generate_line_points(Point3D* points, int num_points)
solver_lib.generate_line_points.argtypes = [ctypes.POINTER(Point3D), ctypes.c_int]
solver_lib.generate_line_points.restype = None

# generate_plane_points(Point3D* points, int grid_size, double range)
solver_lib.generate_plane_points.argtypes = [ctypes.POINTER(Point3D), ctypes.c_int, ctypes.c_double]
solver_lib.generate_plane_points.restype = None

# --- 3. Call C Functions to Get Data ---

# Create instances of Point3D to be filled by the C function
point_p = Point3D()
point_q = Point3D()
distance = solver_lib.get_intersection_and_distance(ctypes.byref(point_p), ctypes.byref(point_q))

# Get line points from C
NUM_LINE_POINTS = 50
LinePointsArray = Point3D * NUM_LINE_POINTS
line_points_c = LinePointsArray()
solver_lib.generate_line_points(line_points_c, NUM_LINE_POINTS)

# Get plane points from C
GRID_SIZE = 20 # 20x20 grid
PLANE_RANGE = 10 # from -10 to +10
NUM_PLANE_POINTS = GRID_SIZE * GRID_SIZE
PlanePointsArray = Point3D * NUM_PLANE_POINTS
plane_points_c = PlanePointsArray()
solver_lib.generate_plane_points(plane_points_c, GRID_SIZE, PLANE_RANGE)

# --- 4. Convert C Data to NumPy for Plotting ---
p = np.array([point_p.x, point_p.y, point_p.z])
q = np.array([point_q.x, point_q.y, point_q.z])

line_points = np.array([[pt.x, pt.y, pt.z] for pt in line_points_c])

# Reshape plane points into a grid for surface plotting
plane_x = np.array([pt.x for pt in plane_points_c]).reshape(GRID_SIZE, GRID_SIZE)
plane_y = np.array([pt.y for pt in plane_points_c]).reshape(GRID_SIZE, GRID_SIZE)
plane_z = np.array([pt.z for pt in plane_points_c]).reshape(GRID_SIZE, GRID_SIZE)

# --- 5. Plotting ---
print("--- Plotting Results ---")
print(f"Point P: ({p[0]}, {p[1]}, {p[2]})")
print(f"Intersection Point Q: ({q[0]}, {q[1]}, {q[2]})")
print(f"Calculated Distance: {distance:.2f} units")

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot the plane surface
ax.plot_surface(plane_x, plane_y, plane_z, alpha=0.5, color='cyan', rstride=1, cstride=1, edgecolor='k', linewidth=0.2, label='Plane')

# Plot the line
ax.plot(line_points[:, 0], line_points[:, 1], line_points[:, 2], color='magenta', lw=3, label='Line')

# Plot the points
ax.scatter(p[0], p[1], p[2], color='red', s=150, depthshade=False, label=f'Point P ({p[0]}, {p[1]}, {p[2]})')
ax.scatter(q[0], q[1], q[2], color='blue', s=150, depthshade=False, label=f'Intersection Q ({q[0]}, {q[1]}, {q[2]})')

# Plot the distance vector between P and Q
ax.plot([p[0], q[0]], [p[1], q[1]], [p[2], q[2]], 'r--', lw=2, label=f'Distance = {distance:.2f}')

# Formatting
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Line, Plane, and Intersection Visualization', fontsize=16)

# Create a custom legend
# Matplotlib 3D doesn't handle labels for plot_surface well, so we create a proxy artist
from matplotlib.patches import Patch
legend_elements = [
    plt.Line2D([0], [0], color='magenta', lw=3, label='Line'),
    Patch(facecolor='cyan', edgecolor='k', label='Plane: x-y+z=5'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label=f'Point P'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label=f'Intersection Q'),
    plt.Line2D([0], [0], color='r', linestyle='--', lw=2, label=f'Distance ({distance:.2f})')
]
ax.legend(handles=legend_elements)

plt.show()
