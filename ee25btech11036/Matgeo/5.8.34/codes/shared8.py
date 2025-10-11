import ctypes
from ctypes import Structure, c_double
import matplotlib.pyplot as plt
import numpy as np

# Define the Point structure as in C
class Point(Structure):
    _fields_ = [("x", c_double), ("y", c_double)]

# Load the shared library
lib = ctypes.CDLL('./libtriangle.so')

# Define the argument types for the C function
lib.get_triangle_vertices.argtypes = [ctypes.POINTER(Point), ctypes.POINTER(Point), ctypes.POINTER(Point)]

# Create Point instances to hold the vertices
A = Point()
B = Point()
C = Point()

# Call the C function to fill the points
lib.get_triangle_vertices(ctypes.byref(A), ctypes.byref(B), ctypes.byref(C))

# Extract points as numpy arrays for plotting
A_np = np.array([A.x, A.y])
B_np = np.array([B.x, B.y])
C_np = np.array([C.x, C.y])

# Plot setup
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(min(A.x, B.x, C.x) - 2, max(A.x, B.x, C.x) + 2)
ax.set_ylim(min(A.y, B.y, C.y) - 2, max(A.y, B.y, C.y) + 2)

# Draw the triangle
triangle = plt.Polygon([A_np, B_np, C_np], closed=True, color='skyblue', edgecolor='black', alpha=0.6, label='Triangle')
ax.add_patch(triangle)

# Draw lines
x = np.linspace(min(A.x, B.x, C.x) - 2, max(A.x, B.x, C.x) + 2, 400)

# Line 1: x - y + 1 = 0 ⟹ y = x + 1
y1 = x + 1
ax.plot(x, y1, 'r--', label='Line 1: x - y + 1 = 0')

# Line 2: 3x + 2y - 12 = 0 ⟹ y = (12 - 3x)/2
y2 = (12 - 3*x)/2
ax.plot(x, y2, 'g--', label='Line 2: 3x + 2y - 12 = 0')

# X and Y axes
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# Mark points A, B, C
points = {f'A ({A.x}, {A.y})': A_np, f'B ({B.x}, {B.y})': B_np, f'C ({C.x}, {C.y})': C_np}
for label, point in points.items():
    ax.plot(*point, 'ko')
    ax.text(point[0] + 0.1, point[1] + 0.1, label, fontsize=10)

# Grid and legend
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend()
plt.title("Triangle formed by lines and x-axis (from C shared library)")
plt.xlabel("x")
plt.ylabel("y")

plt.show()

