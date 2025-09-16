import ctypes
import numpy as np
import matplotlib as mp
mp.use("TkAgg")  # must come before pyplot
import matplotlib.pyplot as plt

# Load C library
lib = ctypes.CDLL('./libmagnitude_sum.so')

# C function signatures
lib.sum_of_vectors.argtypes = [
    ctypes.POINTER(ctypes.c_int), 
    ctypes.POINTER(ctypes.c_int), 
    ctypes.POINTER(ctypes.c_int), 
    ctypes.POINTER(ctypes.c_int)
]
lib.sum_of_vectors.restype = None

lib.find_magnitude.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.find_magnitude.restype = ctypes.c_double

# Define vectors
A = np.array([2, 3, -4], dtype=np.int32)
B = np.array([3, -4, -5], dtype=np.int32)
C = np.array([3, 2, -3], dtype=np.int32)
S = np.zeros(3, dtype=np.int32)

# Sum vectors via C
lib.sum_of_vectors(
    A.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),
    B.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),
    C.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),
    S.ctypes.data_as(ctypes.POINTER(ctypes.c_int))
)

print("Sum of vectors:", S)

# Magnitude via C
magnitude = lib.find_magnitude(S.ctypes.data_as(ctypes.POINTER(ctypes.c_int)))
print("Magnitude of sum vector: {:.3f}".format(magnitude))

# 3D Plot
origin = np.array([0,0,0])
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')

ax.quiver(*origin, *A, color='r', label='A')
ax.quiver(*origin, *B, color='g', label='B')
ax.quiver(*origin, *C, color='b', label='C')
ax.quiver(*origin, *S, color='k', linewidth=2, label='Sum (A+B+C)')

max_val = max(np.abs(S)) + 2
ax.set_xlim([0, max_val])
ax.set_ylim([0, max_val])
ax.set_zlim([min(0, np.min(S)) - 2, max_val])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Vectors and their Sum')
ax.legend()

plt.savefig("/home/user/Matrix/Matgeo_assignments/1.9.15/figs/Figure_1.png", dpi=300, bbox_inches='tight')
plt.show()

