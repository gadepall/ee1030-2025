import ctypes
import matplotlib.pyplot as plt
import numpy as np

# Load shared library
lib = ctypes.CDLL("./quad_area.so")   # use quad_area.dll on Windows

# Function signature
lib.quad_area.restype = ctypes.c_double
lib.quad_area.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                          ctypes.c_double, ctypes.c_double, ctypes.c_double]

# Points A, B, C, D
A = np.array([0, 4, 1])
B = np.array([2, 3, -1])
C = np.array([4, 5, 0])
D = np.array([2, 6, 2])

# Diagonals
P = C - A
Q = D - B

# Call C function
area = lib.quad_area(P[0], P[1], P[2], Q[0], Q[1], Q[2])
print("Area (from C via ctypes) =", area)

# --- Plot quadrilateral ---
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Connect vertices in order A-B-D-C-A
X = [A[0], B[0], C[0], D[0], A[0]]
Y = [A[1], B[1], C[1], D[1], A[1]]
Z = [A[2], B[2], C[2], D[2], A[2]]

ax.plot(X, Y, Z, 'b-', marker='o')
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.show()
