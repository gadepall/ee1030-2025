import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL('./code.so')

# Set argument and return types
lib.dot_product.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
lib.dot_product.restype = ctypes.c_int

lib.is_orthogonal.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
lib.is_orthogonal.restype = ctypes.c_int

lib.normal_vector.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
lib.direction_vector.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]

# Prepare arrays for 2D vectors
nvec = (ctypes.c_int * 2)()
dvec = (ctypes.c_int * 2)()

# Line: x = 3y => 1*x - 3*y = 0
A, B = 1, -3

lib.normal_vector(A, B, nvec)
lib.direction_vector(A, B, dvec)

print("Normal vector:", list(nvec))
print("Direction vector:", list(dvec))

# Plot vectors
origin = np.array([[0,0]])

plt.quiver(*origin.T, nvec[0], nvec[1], color='r', scale=1, scale_units='xy', angles='xy', label='Normal')
plt.quiver(*origin.T, dvec[0], dvec[1], color='b', scale=1, scale_units='xy', angles='xy', label='Direction')

plt.xlim(-5,5)
plt.ylim(-5,5)
plt.grid(True)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.legend()
plt.title('Direction and Normal Vectors for x = 3y')
plt.show()
