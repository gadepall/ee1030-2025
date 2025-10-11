# File: visualize.py
import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
# --- Step 1: Load the compiled shared library ---
lib = ctypes.CDLL("./4.11.19.so")
# --- Step 2: Define the function signature (argument and return types) ---
lib.calculate_plot_data.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C_CONTIGUOUS'), # p
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C_CONTIGUOUS'), # q
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C_CONTIGUOUS'), # intersection_point (output)
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C_CONTIGUOUS'), # line_x (output)
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C_CONTIGUOUS'), # line_y (output)
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C_CONTIGUOUS'), # line_z (output)
    ctypes.c_int  # num_line_points
]
lib.calculate_plot_data.restype = None

# --- Step 3: Prepare data and call the C function ---
p_point = np.array([4, 3, 2], dtype=np.float64)
q_point = np.array([5, 1, 6], dtype=np.float64)

# Allocate memory for the output arrays that the C function will modify
num_line_points = 100
intersection_point = np.zeros(3, dtype=np.float64)
line_x = np.zeros(num_line_points, dtype=np.float64)
line_y = np.zeros(num_line_points, dtype=np.float64)
line_z = np.zeros(num_line_points, dtype=np.float64)

# Execute the function from our .so library
lib.calculate_plot_data(
    p_point, q_point, intersection_point,
    line_x, line_y, line_z, num_line_points
)

print(f"Intersection point from C library: {intersection_point}")

# --- Step 4: Create the 3D plot with Matplotlib ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the XZ plane surface
plane_x_range = np.arange(2, 9, 1)
plane_z_range = np.arange(0, 13, 1)
plane_xx, plane_zz = np.meshgrid(plane_x_range, plane_z_range)
plane_yy = np.zeros_like(plane_xx)
ax.plot_surface(plane_xx, plane_yy, plane_zz, alpha=0.2, color='c', rstride=10, cstride=10)

# Plot the line calculated by the C function
ax.plot(line_x, line_y, line_z, color='m', label='Line through P and Q')

# Plot the points
ax.scatter(*p_point, color='blue', s=100, label=f'P {tuple(p_point)}')
ax.scatter(*q_point, color='green', s=100, label=f'Q {tuple(q_point)}')
ax.scatter(*intersection_point, color='red', s=150, zorder=10, marker='*', label=f'Intersection')

# Formatting the plot
ax.set_xlabel('X-axis'), ax.set_ylabel('Y-axis'), ax.set_zlabel('Z-axis')
ax.set_title('Line Intersection with XZ Plane')
ax.legend()
ax.view_init(elev=20, azim=-60)
plt.show()
