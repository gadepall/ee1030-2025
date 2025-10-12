import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

# --- Define C data structures in Python using ctypes ---

class Vector3D(ctypes.Structure):
    """Maps the C Vector3D struct to a Python class."""
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double),
                ("z", ctypes.c_double)]

class Plane(ctypes.Structure):
    """Maps the C Plane struct to a Python class."""
    _fields_ = [("a", ctypes.c_double),
                ("b", ctypes.c_double),
                ("c", ctypes.c_double),
                ("d", ctypes.c_double)]

# --- Load the compiled C shared library ---
c_lib = ctypes.CDLL('./code.so')
# --- Specify the function signature for type safety ---
c_lib.find_intersection_direction.argtypes = [Plane, Plane]
c_lib.find_intersection_direction.restype = Vector3D
    
# --- Define the planes from the problem ---
# Plane 1: x - 2y + z = 0
plane1 = Plane(1.0, -2.0, 1.0, 0.0)
# Plane 2: x + 0y - z = 0
plane2 = Plane(1.0, 0.0, -1.0, 0.0)
    
# --- Call the C function to get the direction vector ---
direction_vector = c_lib.find_intersection_direction(plane1, plane2)
dv = (direction_vector.x, direction_vector.y, direction_vector.z)
# --- Setup for the 3D Plot (similar to the original file) ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# --- Create a grid of (x,y) points ---
x_vals = np.linspace(-10, 10, 50)
y_vals = np.linspace(-10, 10, 50)
X, Y = np.meshgrid(x_vals, y_vals)

# --- Define and plot Plane 1: x - 2y + z = 0 ---
Z1 = 2 * Y - X
ax.plot_surface(X, Y, Z1, alpha=0.6, color='c')

# --- Define and plot Plane 2: x - z = 0 ---
Z2 = X
ax.plot_surface(X, Y, Z2, alpha=0.6, color='m')

# --- Define and plot the line of intersection using the vector from C ---
alpha = np.linspace(-10, 10, 100) # Parameter for the line
# Use the components of the direction vector to draw the line
line_x = alpha * dv[0]
line_y = alpha * dv[1]
line_z = alpha * dv[2]
ax.plot(line_x, line_y, line_z, color='red', linewidth=3)

# --- Formatting the plot ---
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Create proxy artists for a clear legend
p1 = plt.Rectangle((0, 0), 1, 1, fc="c", alpha=0.6)
p2 = plt.Rectangle((0, 0), 1, 1, fc="m", alpha=0.6)
line = plt.Line2D([0,1],[0,1], color='red', linewidth=3)
ax.legend([p1, p2, line], ['Plane 1: x - 2y + z = 0', 'Plane 2: x - z = 0', 'Intersection Line'])

ax.view_init(elev=25, azim=-50)
plt.show()
