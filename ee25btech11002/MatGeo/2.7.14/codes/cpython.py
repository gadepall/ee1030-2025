import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os
import sys
lib_path = ctypes.CDLL("./formula.so")
lib_path.formula.argtypes = [
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float)
]
lib_path.formula.restype = ctypes.c_float

vecA = np.array([1, -2, 3], dtype=np.float32)
vecB = np.array([3, -2, 1], dtype=np.float32)


# --- Plotting ---

# Create a 3D plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Define the origin point
origin = np.array([0, 0, 0])

# Plot the two vectors from the origin using ax.quiver
ax.quiver(*origin, *vecA, color='blue', label='Vector a = (1, -2, 3)')
ax.quiver(*origin, *vecB, color='green', label='Vector b = (3, -2, 1)')

# Set the limits of the plot for better visualization
max_val = np.max(np.abs(np.concatenate((vecA, vecB)))) + 1
ax.set_xlim([-max_val, max_val])
ax.set_ylim([-max_val, max_val])
ax.set_zlim([-max_val, max_val])

# Add labels and a title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Two 3D Vectors')

# Add a legend
ax.legend()

# Add a grid for better visualization
ax.grid(True)

plt.savefig("plot_c.jpg")
# Show the plot
plt.show()