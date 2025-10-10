import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
import subprocess
import sys

lib_name = 'code5.so'

lib_path = os.path.join(os.getcwd(), lib_name)

if not os.path.exists(lib_path):
    print(f"Error: Shared library '{lib_name}' not found at '{lib_path}'.")
    print("Please compile the C code first.")
    sys.exit(1)


# --- Step 2: Load the shared library and define function signatures ---
try:
    c_lib = ctypes.CDLL(lib_path)
except OSError as e:
    print(f"Error loading shared library: {e}")
    sys.exit(1)

# Define the argument types for the C functions for type safety
# void rotate_vector(double original_vec[3], double rotated_vec[3])
c_lib.rotate_vector.argtypes = [np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C'),
                                np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C')]
c_lib.rotate_vector.restype = None

# void generate_points(double vector[3], int num_points, double* points_out)
c_lib.generate_points.argtypes = [np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C'),
                                  ctypes.c_int,
                                  np.ctypeslib.ndpointer(dtype=np.float64, ndim=2, flags='C')]
c_lib.generate_points.restype = None


# --- Step 3: Use the C functions to get vector points ---

# Define the original vector and ensure it's a C-contiguous numpy array of float64
original_vector = np.array([4, 2, 7], dtype=np.float64)
rotated_vector = np.zeros(3, dtype=np.float64)

# Call the C function to perform the rotation
c_lib.rotate_vector(original_vector, rotated_vector)

print(f"Original vector: {original_vector.tolist()}")
print(f"Rotated vector (from C): {rotated_vector.tolist()}")

# Define number of points to generate for the plot
num_points = 50

# Prepare C-contiguous output arrays for the points
points_original = np.zeros((num_points, 3), dtype=np.float64)
points_rotated = np.zeros((num_points, 3), dtype=np.float64)

# Call C function to generate points for both vectors
c_lib.generate_points(original_vector, num_points, points_original)
c_lib.generate_points(rotated_vector, num_points, points_rotated)


# --- Step 4: Plot the results using Matplotlib ---

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot points for the original vector and draw an arrow at the tip
ax.plot(points_original[:, 0], points_original[:, 1], points_original[:, 2], 'o-', color='blue', markersize=2, label='Original Vector A')
ax.quiver(0, 0, 0, original_vector[0], original_vector[1], original_vector[2], color='blue', arrow_length_ratio=0.1, normalize=False)
ax.text(original_vector[0], original_vector[1], original_vector[2], '  A', color='blue', fontsize=14)

# Plot points for the rotated vector and draw an arrow at the tip
ax.plot(points_rotated[:, 0], points_rotated[:, 1], points_rotated[:, 2], 'o-', color='red', markersize=2, label="Rotated Vector A'")
ax.quiver(0, 0, 0, rotated_vector[0], rotated_vector[1], rotated_vector[2], color='red', arrow_length_ratio=0.1, normalize=False)
ax.text(rotated_vector[0], rotated_vector[1], rotated_vector[2], "  A'", color='red', fontsize=14)

# Setting plot labels and limits
max_val = np.max(np.abs(np.concatenate((original_vector, rotated_vector)))) * 1.2
ax.set_xlim([-max_val, max_val])
ax.set_ylim([-max_val, max_val])
ax.set_zlim([-max_val, max_val])
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)
ax.set_zlabel('Z-axis', fontsize=12)
ax.set_title('Vector Rotation using C Library and Plotted with Python', fontsize=16)

ax.legend()
ax.grid(True)
ax.view_init(elev=20, azim=30)
plt.tight_layout()
plt.show()
