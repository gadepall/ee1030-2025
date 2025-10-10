import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL('./libcollinear.so')

# Define argument types
lib.are_collinear.argtypes = [ctypes.POINTER(ctypes.c_float),
                              ctypes.POINTER(ctypes.c_float),
                              ctypes.POINTER(ctypes.c_float)]
lib.are_collinear.restype = ctypes.c_int

# Define points
A = np.array([-2, 3, 5], dtype=np.float32)
B = np.array([1, 2, 3], dtype=np.float32)
C = np.array([7, 0, -1], dtype=np.float32)

# Call the function
result = lib.are_collinear(A.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
                           B.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
                           C.ctypes.data_as(ctypes.POINTER(ctypes.c_float)))

if result == 1:
    print("Points are collinear")
else:
    print("Points are NOT collinear")

# Plotting the points
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(*A, color='red', label='A')
ax.scatter(*B, color='green', label='B')
ax.scatter(*C, color='blue', label='C')

# Draw lines between points
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], 'gray', linestyle='--')
ax.plot([A[0], C[0]], [A[1], C[1]], [A[2], C[2]], 'gray', linestyle='--')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.title("Visualization of Points A, B, and C")
plt.savefig("/home/gara-varun-kumar/ee1030-2025/ai25btech11011/matgeo/1.6.26/figs/Fig 1.png")
plt.show()
