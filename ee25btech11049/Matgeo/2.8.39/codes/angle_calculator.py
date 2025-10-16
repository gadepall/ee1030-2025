# Code by GVV Sharma
# July 22, 2024
# Released under GNU GPL
# This script finds the angle between two lines by calling a standard C shared library.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import ctypes
import os

# --- Load the C Shared Library using ctypes ---
try:
    # Construct the full path to the library file, assuming it's in the same directory.
    lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'angle_calculator_lib.so')
    angle_lib = ctypes.CDLL(lib_path)
except OSError:
    print("Error: 'angle_calculator_lib.so' not found.")
    print("Please compile the C library by running this command in your terminal:")
    print("gcc -shared -o angle_calculator_lib.so -fPIC angle_calculator_lib.c")
    exit()

# --- Define the function signature from the C library ---
# Tell ctypes that the function returns a C double. This is crucial for correctness.
angle_lib.get_angle_between_lines.restype = ctypes.c_double

# --- Call the C function ---
angle_deg = angle_lib.get_angle_between_lines()
angle_rad = np.deg2rad(angle_deg)


# --- For Plotting Purposes (re-defining vectors in Python) ---
# Direction ratios
d1_ratios = np.array([0, 1, -1])
d2_ratios = np.array([1, 0, -1])

# Direction cosines (unit vectors)
d1 = d1_ratios / np.linalg.norm(d1_ratios)
d2 = d2_ratios / np.linalg.norm(d2_ratios)

print("--- Calculation performed by standard C library via ctypes ---")
print(f"The angle between the lines is {angle_rad:.4f} radians.")
print(f"The angle between the lines is {angle_deg:.2f} degrees.")
print("-" * 55)


# --- Plotting the vectors in 3D ---
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Origin point
origin = [0, 0, 0]

# Plot the direction cosine vectors
label1 = f'Line 1 DC: ({d1[0]:.2f}, {d1[1]:.2f}, {d1[2]:.2f})'
label2 = f'Line 2 DC: ({d2[0]:.2f}, {d2[1]:.2f}, {d2[2]:.2f})'
ax.quiver(*origin, *d1, color='r', label=label1)
ax.quiver(*origin, *d2, color='b', label=label2)

# Set plot limits
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 1.5])

# Add labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Visualization of the Two Lines in 3D (Angle from C Library)')
ax.legend()
ax.grid(True)

# Equal aspect ratio
ax.set_box_aspect([1,1,1])

plt.show()


