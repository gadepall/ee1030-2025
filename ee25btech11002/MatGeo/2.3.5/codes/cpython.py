# Python script to call a C library from a specific path and plot the result.
# September 12, 2025

import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- Part 1: C Function Integration ---

# Define the absolute path to the compiled C library.
# In Python strings, backslashes must be escaped (\\) or you can use a raw string (r"...").
lib_path = ctypes.CDLL('./formula.so')

# Define the argument and return types for the C function
#c_float_p = ctypes.POINTER(ctypes.c_float)
lib_path.formula.argtypes = [
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float)
]
lib_path.formula.restype = ctypes.c_float

# Prepare the input vectors for problem 2.3.5
d_vec = np.array([3, -1, 2], dtype=np.float32)
n_vec = np.array([1, 1, 1], dtype=np.float32)

#d_p = d_vec.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
#n_p = n_vec.ctypes.data_as(ctypes.POINTER(ctypes.c_float))

# Call the C function to calculate the angle
angle = lib_path.formula(
    d_vec.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
    n_vec.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
)

print(f"Angle between line and plane: {angle:.4f} degrees")

# Plane and Line definitions
a, b, c, d_plane = 1, 1, 1, 3 
line_point = np.array([1, -1, 1])
line_direction = d_vec
intersection_point = line_point + 0.5 * line_direction

# Plotting setup
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
plot_lim = 8

x_plane = np.linspace(-plot_lim, plot_lim, 50)
y_plane = np.linspace(-plot_lim, plot_lim, 50)
X, Y = np.meshgrid(x_plane, y_plane)
Z = (d_plane - a*X - b*Y) / c
Z[(Z > plot_lim) | (Z < -plot_lim)] = np.nan # Masking

# Plotting the geometry
ax.plot_surface(X, Y, Z, alpha=0.6, color='cyan')
t = np.linspace(-3, 3, 100)
ax.plot(line_point[0] + t * line_direction[0], 
        line_point[1] + t * line_direction[1], 
        line_point[2] + t * line_direction[2], 
        color='magenta', linewidth=3)
ax.scatter(intersection_point[0], intersection_point[1], intersection_point[2], 
           color='red', s=150, zorder=10)

# Formatting the plot
ax.set_xlabel('X-axis'); ax.set_ylabel('Y-axis'); ax.set_zlabel('Z-axis')
ax.set_title('Intersection Plot (Angle calculated in C)', fontsize=16)
ax.set_xlim([-plot_lim, plot_lim]); ax.set_ylim([-plot_lim, plot_lim]); ax.set_zlim([-plot_lim, plot_lim])
ax.set_box_aspect([1,1,1])
plt.grid(True)
plt.legend()

# Save and show the final plot
plt.savefig('plot_from_c_and_python_absolute_path.pdf')
plt.show()