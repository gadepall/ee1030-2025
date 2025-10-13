import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL('./geometry.so')

# Define function signatures
lib.foot_of_perpendicular.argtypes = [ctypes.POINTER(ctypes.c_double)] * 4
lib.image_point.argtypes = [ctypes.POINTER(ctypes.c_double)] * 3

# Define points
A = np.array([-1, 8, 4], dtype=np.double)
B = np.array([0, -1, 3], dtype=np.double)
C = np.array([2, -3, -1], dtype=np.double)
foot = np.zeros(3, dtype=np.double)
image = np.zeros(3, dtype=np.double)

# Call C functions
lib.foot_of_perpendicular(
    A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    B.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    C.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    foot.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
)

lib.image_point(
    A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    foot.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    image.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


# Extend line BC in both directions
direction = C - B
t_vals = np.linspace(-1.5, 2.5, 100)  # Adjust range for desired extension
extended_line = np.array([B + t * direction for t in t_vals])

# Line BC
# ax.plot([B[0], C[0]], [B[1], C[1]], [B[2], C[2]], 'k-', label='Line BC')

# Extended line BC
ax.plot(extended_line[:, 0], extended_line[:, 1], extended_line[:, 2], 'k-', label='Extended Line BC')


# Points
ax.scatter(*A, color='red', label='Point A')
ax.scatter(*foot, color='green', label='Foot of Perpendicular')
ax.scatter(*image, color='purple', label='Image of A')

# Dashed line from A to foot
ax.plot([A[0], foot[0]], [A[1], foot[1]], [A[2], foot[2]], 'r--', label='A to Foot')

# Dashed line from A to image (reflection)
ax.plot([A[0], image[0]], [A[1], image[1]], [A[2], image[2]], 'b--', label='A to Image')

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Foot of Perpendicular and Image of A in Line BC')
ax.legend()
plt.tight_layout()
plt.show()

