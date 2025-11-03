import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL("./points.so")

# Function prototypes
lib.dot_product.argtypes = [ctypes.POINTER(ctypes.c_double),
                            ctypes.POINTER(ctypes.c_double)]
lib.dot_product.restype = ctypes.c_double

lib.norm_squared.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.norm_squared.restype = ctypes.c_double

lib.vector_diff.argtypes = [ctypes.POINTER(ctypes.c_double),
                            ctypes.POINTER(ctypes.c_double),
                            ctypes.POINTER(ctypes.c_double)]
lib.vector_diff.restype = None

# Define points
A = np.array([-4.0, 0.0])
B = np.array([4.0, 0.0])
C = np.array([0.0, 3.0])

# Compute vectors
AB = np.zeros(2)
AC = np.zeros(2)
BC = np.zeros(2)

lib.vector_diff(A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                B.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                AB.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))

lib.vector_diff(A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                C.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                AC.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))

lib.vector_diff(B.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                C.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                BC.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))

# Check dot products for right angle
dp1 = lib.dot_product(AB.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                      AC.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))

dp2 = lib.dot_product((-AB).ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                      BC.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))

dp3 = lib.dot_product((-AC).ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                      (-BC).ctypes.data_as(ctypes.POINTER(ctypes.c_double)))

# Norm squared of sides
AB2 = lib.norm_squared(AB.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
AC2 = lib.norm_squared(AC.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
BC2 = lib.norm_squared(BC.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))

print("Dot products:", dp1, dp2, dp3)
print("Side lengths squared:", AB2, AC2, BC2)

# Plot the triangle
points = np.array([A, B, C, A])
plt.plot(points[:,0], points[:,1], 'b-o')
plt.text(A[0], A[1], "A")
plt.text(B[0], B[1], "B")
plt.text(C[0], C[1], "C")
plt.axis("equal")
plt.grid(True)
plt.show()

