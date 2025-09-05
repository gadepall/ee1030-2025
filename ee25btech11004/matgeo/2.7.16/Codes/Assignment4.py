import numpy as np
import ctypes
import matplotlib.pyplot as plt

c_lib=ctypes.CDLL('./4c.so')

# Define the argument types for the x function
c_lib.crossprod.argtypes = [ctypes.c_float, ctypes.c_float,ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float]

c_lib.crossprod.restype = ctypes.c_float


vecA = np.array([2,1,3])

vecB = np.array([3,5,-2])

mod = c_lib.crossprod(
    ctypes.c_float(vecA[0]),
    ctypes.c_float(vecA[1]), 
    ctypes.c_float(vecA[2]),
    ctypes.c_float(vecB[0]), 
    ctypes.c_float(vecB[1]),
    ctypes.c_float(vecB[2])
)

print(mod)

vecA = np.array([2,1,3]).reshape(-1,1)

vecB = np.array([3,5,-2]).reshape(-1,1)

# Create a 3D plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

origin = np.array([0, 0, 0])

ax.quiver(*origin, *vecA, color='r', label='Vector (3, 5, -2)')
ax.quiver(*origin, *vecB, color='b', label='Vector (2, 1, 3)')

max_val = np.max(np.abs(np.concatenate((vecA, vecB))))
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

# Show the plot
plt.show()