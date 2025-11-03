import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the compiled C library
lib = ctypes.CDLL('./9.so')

# Define argument and return types
lib.interior_points.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
lib.interior_points.restype = ctypes.c_int

# Triangle vertices
x1, y1 = 0, 0
x2, y2 = 0, 41
x3, y3 = 41, 0

# Call C function to get interior lattice points
I = lib.interior_points(x1, y1, x2, y2, x3, y3)
print("Number of interior lattice points:", I)

# ---- Generate interior points ----
points = []
for i in range(42):
    for j in range(42):
        if i > 0 and j > 0 and i + j < 41:
            points.append((i, j))

pts = np.array(points)
x, y = pts[:, 0], pts[:, 1]

# ---- Plotting ----
plt.figure(figsize=(6,6))
plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], 'k-', label="Triangle")
plt.scatter(x, y, s=10, color='red', label="Interior Lattice Points")

# Label the vertices with coordinates
plt.text(x1, y1, f"({x1},{y1})", fontsize=10, verticalalignment='bottom', horizontalalignment='right')
plt.text(x2, y2, f"({x2},{y2})", fontsize=10, verticalalignment='bottom', horizontalalignment='left')
plt.text(x3, y3, f"({x3},{y3})", fontsize=10, verticalalignment='top', horizontalalignment='right')

plt.title("Integer Lattice Points Inside Triangle")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()
