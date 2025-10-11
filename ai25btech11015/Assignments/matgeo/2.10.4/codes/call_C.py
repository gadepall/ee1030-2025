import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import ctypes

"""
Find the area of the triangle whose vertices are
A(1,−1,2),B(2,0,−1),C(3,−1,2).
"""

A = np.array([1, -1, 2], dtype=np.float64)
B = np.array([2, 0, -1], dtype=np.float64)
C = np.array([3, -1, 2], dtype=np.float64)

# Load the shared library
lib = ctypes.CDLL("./main.so")

# Set argument and return types
lib.main.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.main.restype = ctypes.c_double

# Call the C function
area = lib.main(A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                 B.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                          C.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))


print("Area of triangle ABC (Python):", area)

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Triangle vertices
triangle = np.array([A, B, C])

# Plot triangle edges
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], color='blue')
ax.plot([B[0], C[0]], [B[1], C[1]], [B[2], C[2]], color='blue')
ax.plot([C[0], A[0]], [C[1], A[1]], [C[2], A[2]], color='blue')

# Fill triangle surface
ax.add_collection3d(Poly3DCollection([triangle], color='cyan', alpha=0.5))

# Scatter vertices
ax.scatter(A[0], A[1], A[2], color='red')
ax.text(A[0], A[1], A[2], "A", fontsize=12, ha='right')
ax.scatter(B[0], B[1], B[2], color='red')
ax.text(B[0], B[1], B[2], "B", fontsize=12, ha='left')
ax.scatter(C[0], C[1], C[2], color='red')
ax.text(C[0], C[1], C[2], "C", fontsize=12, ha='center')

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Area : " + str(area))

# Save figure
plt.savefig("../figs/fig.png", dpi=300)

