import sys
import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load C library
c_lib = ctypes.CDLL('./formula.so')

c_lib.line_vectors.argtypes = [
    ctypes.POINTER(ctypes.c_float),  
    ctypes.POINTER(ctypes.c_float),  
    ctypes.c_float, ctypes.c_float
]
c_lib.line_vectors.restype = None  

# For line: x + y = 4
a, b, c = 1.0, 1.0, 4.0

normal = np.zeros(2, dtype=np.float32)
direction = np.zeros(2, dtype=np.float32)

c_lib.line_vectors(
    normal.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
    direction.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
    ctypes.c_float(a), ctypes.c_float(b)
)

print("Normal Vector:", normal)
print("Direction Vector:", direction)

# Plot line
x = np.linspace(-1, 6, 100)
y = (c - a*x)/b
plt.plot(x, y, label="x+y=4")

# Plot normal at (2,2)
P = np.array([2, 2])
plt.quiver(P[0], P[1], normal[0], normal[1], angles='xy', scale_units='xy', scale=1, color='r', label='Normal')
plt.quiver(P[0], P[1], direction[0], direction[1], angles='xy', scale_units='xy', scale=1, color='g', label='Direction')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.savefig("figs/Plot_P.png")
plt.show()