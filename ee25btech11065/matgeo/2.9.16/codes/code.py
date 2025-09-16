import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import ctypes
import os

# --- C Library and Structure Setup ---

# Define the Vector structure in Python to match the C struct
class Vector(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double),
                ("z", ctypes.c_double)]

    def __repr__(self):
        return f"({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"

# Load the compiled C shared library (e.g., 'vector_lib.so')
try:
    c_lib = ctypes.CDLL('./vector_lib.so')
except OSError:
    print("Error: 'vector_lib.so' not found.")
    print("Please compile the 'vector_lib.c' file first.")
    print("Command: gcc -shared -o vector_lib.so -fPIC vector_lib.c")
    exit()

# Define the function signature for the C function we want to use.
# It takes three Vector structs and returns one Vector struct.
c_lib.check_collinearity_condition.argtypes = [Vector, Vector, Vector]
c_lib.check_collinearity_condition.restype = Vector


# --- Data for Visualization ---

# Case 1: Three points that ARE collinear
a1 = Vector(1.0, 1.0, 1.0)
b1 = Vector(2.0, 2.0, 2.0)
c1 = Vector(-1.0, -1.0, -1.0)

# Case 2: Three points that are NOT collinear (form a triangle)
a2 = Vector(4.0, 0.0, 0.0)
b2 = Vector(0.0, 4.0, 0.0)
c2 = Vector(0.0, 0.0, 4.0)


# --- Call C Function and Print Results ---

# Call the C function for the collinear case
result_collinear = c_lib.check_collinearity_condition(a1, b1, c1)
print(f"Result for collinear points: {result_collinear}")

# Call the C function for the non-collinear case
result_non_collinear = c_lib.check_collinearity_condition(a2, b2, c2)
print(f"Result for non-collinear points: {result_non_collinear}")


# --- Plotting ---

fig = plt.figure(figsize=(15, 8))
fig.suptitle('3D Visualization of Vector Collinearity Condition', fontsize=16)

# Subplot 1: Collinear Case
ax1 = fig.add_subplot(121, projection='3d')
points1 = np.array([[a1.x, a1.y, a1.z], [b1.x, b1.y, b1.z], [c1.x, c1.y, c1.z]])
ax1.scatter(points1[:, 0], points1[:, 1], points1[:, 2], color='red', s=60, depthshade=True)

# Annotate points
for point, label in zip(points1, ['A', 'B', 'C']):
    ax1.text(point[0], point[1], point[2], f' {label}', size=12, zorder=1, color='k')

# Draw a line through the points to emphasize collinearity
line_range = np.linspace(np.min(points1), np.max(points1), 10)
ax1.plot(line_range, line_range, line_range, 'b--', alpha=0.7, label='Line of Collinearity')
ax1.set_title(f'Collinear Points\nResult: {result_collinear}', fontsize=12)
ax1.set_xlabel('X axis'), ax1.set_ylabel('Y axis'), ax1.set_zlabel('Z axis')
ax1.legend()


# Subplot 2: Non-Collinear Case
ax2 = fig.add_subplot(122, projection='3d')
points2 = np.array([[a2.x, a2.y, a2.z], [b2.x, b2.y, b2.z], [c2.x, c2.y, c2.z]])
ax2.scatter(points2[:, 0], points2[:, 1], points2[:, 2], color='green', s=60, depthshade=True)

# Annotate points
for point, label in zip(points2, ['A', 'B', 'C']):
    ax2.text(point[0], point[1], point[2], f' {label}', size=12, zorder=1, color='k')

# Draw lines to form a triangle
for s, e in [[points2[0], points2[1]], [points2[1], points2[2]], [points2[2], points2[0]]]:
    ax2.plot([s[0], e[0]], [s[1], e[1]], [s[2], e[2]], 'k-', alpha=0.5)

ax2.set_title(f'Non-Collinear Points\nResult: {result_non_collinear}', fontsize=12)
ax2.set_xlabel('X axis'), ax2.set_ylabel('Y axis'), ax2.set_zlabel('Z axis')


plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()


