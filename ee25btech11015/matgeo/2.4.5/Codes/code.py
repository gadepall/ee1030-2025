import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import ctypes
import os

# --- Load the C library ---
try:
    c_lib = ctypes.CDLL('./code.so')
except OSError:
    print("Error: 'code.so' not found. Compile using: gcc -shared -o code.so -fPIC triangle.c")
    exit()

# Define argument and return types
c_lib.is_right_triangle.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float,
                                    ctypes.c_float, ctypes.c_float, ctypes.c_float,
                                    ctypes.c_float, ctypes.c_float, ctypes.c_float]
c_lib.is_right_triangle.restype = ctypes.c_int

# --- Given points ---
A = np.array([2, -1, 1], dtype=np.float32)
B = np.array([1, -3, -5], dtype=np.float32)
C = np.array([3, -4, -4], dtype=np.float32)

# --- Call C function ---
result = c_lib.is_right_triangle(A[0], A[1], A[2],
                                 B[0], B[1], B[2],
                                 C[0], C[1], C[2])

if result == 1:
    print("✅ The points form a right-angled triangle.")
else:
    print("❌ The points do not form a right-angled triangle.")

# --- Plotting ---
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Points
ax.scatter(*A, color="red", s=50)
ax.scatter(*B, color="blue", s=50)
ax.scatter(*C, color="green", s=50)

# Triangle surface
triangle = np.array([A, B, C])
ax.add_collection3d(Poly3DCollection([triangle], alpha=0.2, facecolor='cyan'))

# Edges
ax.plot(*zip(A,B), color="black")
ax.plot(*zip(B,C), color="black")
ax.plot(*zip(C,A), color="black")

# Labels
ax.text(*A, "A(2,-1,1)", color="red")
ax.text(*B, "B(1,-3,-5)", color="blue")
ax.text(*C, "C(3,-4,-4)", color="green")

# Axes labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Triangle formed by A, B, C")

plt.show()
