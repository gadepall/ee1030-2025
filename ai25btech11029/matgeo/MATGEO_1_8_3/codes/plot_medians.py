import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL('./solve_medians.so')
lib.solve_medians.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.solve_medians.restype = None

# Triangle vertices: A(0,6), B(4,0), C(6,0)
triangle = np.array([[0.0, 6.0], [4.0, 0.0], [6.0, 0.0]], dtype=np.float64)
coords = triangle.flatten()
medians = np.zeros(12, dtype=np.float64)

# Call C function
lib.solve_medians(coords.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                  medians.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))

# Plot triangle
plt.plot(*triangle[[0, 1]].T, 'k-')
plt.plot(*triangle[[1, 2]].T, 'k-')
plt.plot(*triangle[[2, 0]].T, 'k-')

# Plot medians
for i in range(0, 12, 4):
    x = [medians[i], medians[i+2]]
    y = [medians[i+1], medians[i+3]]
    plt.plot(x, y, 'r--')

# Annotate vertices
for i, label in enumerate(['A', 'B', 'C']):
    plt.text(triangle[i][0], triangle[i][1], label, fontsize=12, ha='right')

plt.axis('equal')
plt.grid(True)
plt.title('Triangle and Medians')
plt.show()
