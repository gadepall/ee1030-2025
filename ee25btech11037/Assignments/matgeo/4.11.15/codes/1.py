import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the shared library
lib = ctypes.CDLL('./mat.so')

# Define argument and result types
lib.computePlaneEquation.argtypes = [
    ctypes.POINTER(ctypes.c_double), ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.c_double,
    ctypes.POINTER(ctypes.c_double)
]
lib.computePlaneEquation.restype = None

# Input plane data
n1 = np.array([1.0, 2.0, 3.0], dtype=np.double)
d1 = -4.0
n2 = np.array([2.0, 1.0, -1.0], dtype=np.double)
d2 = 5.0
n3 = np.array([5.0, 3.0, -6.0], dtype=np.double)
d3 = 8.0

# Output array to store computed plane coefficients
result = np.zeros(4, dtype=np.double)

# Call the C function
lib.computePlaneEquation(
    np.ctypeslib.as_ctypes(n1), d1,
    np.ctypeslib.as_ctypes(n2), d2,
    np.ctypeslib.as_ctypes(n3), d3,
    np.ctypeslib.as_ctypes(result)
)

A, B, C, D = result[0], result[1], result[2], result[3]

# Scale by 19 to get integer coefficients
denominator = 19
A_int = round(A * denominator)
B_int = round(B * denominator)
C_int = round(C * denominator)
D_int = round(D * denominator)

print(f"Integer-coefficient plane equation (Plane p):")
print(f"p: {A_int}x + {B_int}y + {C_int}z + {D_int} = 0")

# Set up 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Generate grid
grid_range = np.linspace(-10, 10, 50)
xx, yy = np.meshgrid(grid_range, grid_range)

def plot_plane(A, B, C, D, color, label):
    if C != 0:
        zz = -(A * xx + B * yy + D) / C
        ax.plot_surface(xx, yy, zz, alpha=0.5, rstride=1, cstride=1, color=color, edgecolor='none', label=label)

# Plot planes with appropriate labels
p1 = ax.plot_surface(xx, yy, -(1 * xx + 2 * yy -4) / 3, alpha=0.5, color='lightcoral', edgecolor='none')
p2 = ax.plot_surface(xx, yy, -(2 * xx + 1 * yy +5) / -1, alpha=0.5, color='lightgreen', edgecolor='none')
p3 = ax.plot_surface(xx, yy, -(5 * xx + 3 * yy +8) / -6, alpha=0.5, color='lightblue', edgecolor='none')
p  = ax.plot_surface(xx, yy, -(A_int * xx + B_int * yy + D_int) / C_int, alpha=0.5, color='cyan', edgecolor='none')

# Custom legend using proxy artists
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='lightcoral', label='p1: Plane 1'),
    Patch(facecolor='lightgreen', label='p2: Plane 2'),
    Patch(facecolor='lightblue', label='p3: Plane 3'),
    Patch(facecolor='cyan', label='p')
]
ax.legend(handles=legend_elements, loc='upper right')

# Axis labels and limits
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)

ax.set_title('3D Plot of Planes p1, p2, p3, and p')

# Save the figure
plt.savefig('1.png', dpi=300, bbox_inches='tight')
plt.show()
