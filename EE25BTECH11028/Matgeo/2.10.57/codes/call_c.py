import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the compiled C library
lib = ctypes.CDLL("./libvectors.so")   # use "vectors.dll" on Windows

# Define argument types
lib.check.argtypes = [
    ctypes.POINTER(ctypes.c_double), 
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]

# Define vectors (unit vectors)
a = (ctypes.c_double * 3)(1, 0, 0)  # along x
d = (ctypes.c_double * 3)(1, 0, 0)  # parallel to a
b = (ctypes.c_double * 3)(0, 1, 0)  # along y
c = (ctypes.c_double * 3)(0, 1, 0)  # parallel to b

val1 = ctypes.c_double()
val2 = ctypes.c_double()

# Call C function
lib.check(a, b, c, d, ctypes.byref(val1), ctypes.byref(val2))

print("(a×b)·(c×d) =", val1.value)
print("a·c =", val2.value)

# Plot in Python
fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, projection='3d')

origin = [0,0,0]

ax.quiver(*origin, *a, color='r', label='a')
ax.quiver(*origin, *b, color='g', label='b')
ax.quiver(*origin, *c, color='b', label='c')
ax.quiver(*origin, *d, color='m', label='d')

ax.set_xlim([0,1.5])
ax.set_ylim([0,1.5])
ax.set_zlim([0,1.5])
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title("C code in Python: a || d, b || c")

ax.legend()
plt.savefig("fig5.1.png")
plt.show()