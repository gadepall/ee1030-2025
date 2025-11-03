import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the compiled C library
lib = ctypes.CDLL("./vector_calc.so")   # use "vector_calc.dll" on Windows

# Call the C function
lib.vector_magnitude.restype = ctypes.c_double
magnitude = lib.vector_magnitude()
print("Result from C code |a+b+c| =", magnitude)

# ---- Plotting in Python ----
a = np.array([3, 0, 0])
b = np.array([0, 4, 0])
c = np.array([0, 0, 5])
resultant = a + b + c

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

# plot vectors
origin = np.array([0, 0, 0])
ax.quiver(*origin, *a, color='r', label='a (3)')
ax.quiver(*origin, *b, color='g', label='b (4)')
ax.quiver(*origin, *c, color='b', label='c (5)')
ax.quiver(*origin, *resultant, color='m', label='a+b+c')

ax.set_xlim([0, 8])
ax.set_ylim([0, 8])
ax.set_zlim([0, 8])

ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")
ax.set_title("C code calculation + Python plot")

ax.legend()
plt.show()