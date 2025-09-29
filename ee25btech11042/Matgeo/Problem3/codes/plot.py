import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared C library
lib = ctypes.CDLL("./trianglearea.so")
lib.triangle_area.argtypes = [ctypes.c_float, ctypes.c_float,
                              ctypes.c_float, ctypes.c_float,
                              ctypes.c_float, ctypes.c_float]
lib.triangle_area.restype = ctypes.c_float

# Vertices
A = (2, 9)
B = (2, 5)
C = (5, 5)

# Call C function
area = lib.triangle_area(A[0], A[1], B[0], B[1], C[0], C[1])
print("Area of triangle ABC (from C):", area)

# Plot triangle
x = [A[0], B[0], C[0], A[0]]
y = [A[1], B[1], C[1], A[1]]

plt.plot(x, y, 'bo-')
plt.text(A[0], A[1], "A(2,9)", fontsize=10, ha="right")
plt.text(B[0], B[1], "B(2,5)", fontsize=10, ha="right")
plt.text(C[0], C[1], "C(5,5)", fontsize=10, ha="right")
plt.title("Right Triangle ABC")
plt.grid(True)
plt.axis("equal")
plt.show()

