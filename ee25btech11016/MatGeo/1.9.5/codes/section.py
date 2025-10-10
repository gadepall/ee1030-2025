import ctypes
import numpy as np
import matplotlib.pyplot as plt
import math

# Load shared library
lib = ctypes.CDLL('./section.so')

# Define function signature: double find_distance(double, double, double, double)
lib.find_distance.argtypes = [ctypes.c_double, ctypes.c_double,
                              ctypes.c_double, ctypes.c_double]
lib.find_distance.restype = ctypes.c_double

# Points
x1, y1 = 0, 2*math.sqrt(5)
x2, y2 = -2*math.sqrt(5), 0

# Call C function
dist = lib.find_distance(x1, y1, x2, y2)
print(f"Distance between ({x1},{y1:.2f}) and ({x2:.2f},{y2}) = {dist:.2f}")

# Define points
A = np.array([x1, y1])
B = np.array([x2, y2])

# Plot line AB
plt.plot([A[0], B[0]], [A[1], B[1]], 'k-', label='$AB$')

# Plot points
plt.scatter([A[0], B[0]], [A[1], B[1]], c=['red', 'blue'])
labels = [f"A({x1},{y1:.2f})", f"B({x2:.2f},{y2})"]
coords = [A, B]

# Annotate points
for label, coord in zip(labels, coords):
    plt.annotate(label,
                 (coord[0], coord[1]),
                 textcoords="offset points",
                 xytext=(10, -10),
                 ha='center')

# Decorations
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.title(f"Distance = {dist:.2f}")
plt.savefig("2.png", dpi=150)
plt.show()
