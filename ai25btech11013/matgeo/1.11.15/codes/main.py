from ctypes import CDLL, c_double, POINTER
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Load the shared library
lib = CDLL('./libvector.so')

# Define function prototypes
lib.compute_vector_sum.argtypes = [
    c_double, c_double, c_double,  # a components
    c_double, c_double, c_double,  # b components
    POINTER(c_double), POINTER(c_double), POINTER(c_double)  # result components
]
lib.compute_vector_sum.restype = None

# Given vectors
a = [1.0, 1.0, -2.0]  # i + j - 2k
b = [2.0, -4.0, 5.0]  # 2i - 4j + 5k

# Prepare result variables
result_i = c_double()
result_j = c_double()
result_k = c_double()

# Call the C function
lib.compute_vector_sum(
    c_double(a[0]), c_double(a[1]), c_double(a[2]),
    c_double(b[0]), c_double(b[1]), c_double(b[2]),
    result_i, result_j, result_k
)

# Get the results
result_vector = [result_i.value, result_j.value, result_k.value]

print("Vector Operations using Python and C Library")
print("===========================================")
print(f"Vector a = {a[0]}i + {a[1]}j + {a[2]}k")
print(f"Vector b = {b[0]}i + {b[1]}j + {b[2]}k")
print(f"3a + 2b = {result_vector[0]:.1f}i + {result_vector[1]:.1f}j + {result_vector[2]:.1f}k")
print(f"\nDirection ratios of 3a + 2b:")
print(f"x-component: {result_vector[0]:.1f}")
print(f"y-component: {result_vector[1]:.1f}")
print(f"z-component: {result_vector[2]:.1f}")

# Create a detailed 3D plot
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Origin point
origin = [0, 0, 0]

# Plot vector a (red)
ax.quiver(*origin, *a, color='red', arrow_length_ratio=0.1, linewidth=3, 
          label=f'a = {a[0]}i + {a[1]}j + {a[2]}k')

# Plot vector b (blue)
ax.quiver(*origin, *b, color='blue', arrow_length_ratio=0.1, linewidth=3,
          label=f'b = {b[0]}i + {b[1]}j + {b[2]}k')

# Plot result vector (green)
ax.quiver(*origin, *result_vector, color='green', arrow_length_ratio=0.1, linewidth=4,
          label=f'3a + 2b = {result_vector[0]:.1f}i + {result_vector[1]:.1f}j + {result_vector[2]:.1f}k')

# Also show the components of 3a + 2b as dotted lines
# X-component (along x-axis)
ax.plot([0, result_vector[0]], [0, 0], [0, 0], 'g--', alpha=0.7, linewidth=2, label='X-component')
# Y-component (along y-axis)
ax.plot([0, 0], [0, result_vector[1]], [0, 0], 'g--', alpha=0.7, linewidth=2, label='Y-component')
# Z-component (along z-axis)
ax.plot([0, 0], [0, 0], [0, result_vector[2]], 'g--', alpha=0.7, linewidth=2, label='Z-component')

# Add coordinate system axes
ax.quiver(0, 0, 0, 8, 0, 0, color='black', arrow_length_ratio=0.05, alpha=0.5, linestyle=':')
ax.quiver(0, 0, 0, 0, 8, 0, color='black', arrow_length_ratio=0.05, alpha=0.5, linestyle=':')
ax.quiver(0, 0, 0, 0, 0, 8, color='black', arrow_length_ratio=0.05, alpha=0.5, linestyle=':')

# Add text labels for axes
ax.text(8.5, 0, 0, 'X (i)', fontsize=12, color='black')
ax.text(0, 8.5, 0, 'Y (j)', fontsize=12, color='black')
ax.text(0, 0, 8.5, 'Z (k)', fontsize=12, color='black')

# Add text labels for vector endpoints
ax.text(a[0], a[1], a[2], ' a', fontsize=10, color='red')
ax.text(b[0], b[1], b[2], ' b', fontsize=10, color='blue')
ax.text(result_vector[0], result_vector[1], result_vector[2], ' 3a+2b', fontsize=12, color='green')

# Add text for direction ratios
ax.text(2, -6, 6, f'Direction Ratios:\nX: {result_vector[0]:.1f}\nY: {result_vector[1]:.1f}\nZ: {result_vector[2]:.1f}', 
        fontsize=11, bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))

# Set plot limits with some padding
max_val = max(max(abs(x) for x in a + b + result_vector), 1) + 2
ax.set_xlim([-max_val, max_val])
ax.set_ylim([-max_val, max_val])
ax.set_zlim([-max_val, max_val])

# Labels and title
ax.set_xlabel('X-axis (i)', fontsize=12, fontweight='bold')
ax.set_ylabel('Y-axis (j)', fontsize=12, fontweight='bold')
ax.set_zlabel('Z-axis (k)', fontsize=12, fontweight='bold')
ax.set_title('3D Vector Visualization: 3a + 2b\nDirection Ratios: (7.0, -5.0, 4.0)', 
             fontsize=14, fontweight='bold', pad=20)

# Add grid with better visibility
ax.grid(True, alpha=0.3)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.xaxis.pane.set_edgecolor('w')
ax.yaxis.pane.set_edgecolor('w')
ax.zaxis.pane.set_edgecolor('w')

# Set view angle for better visualization
ax.view_init(elev=20, azim=30)

# Add legend
ax.legend(loc='upper left', bbox_to_anchor=(0, 1))


plt.savefig("/home/gauthamp/ee1030-2025/ai25btech11013/matgeo/1.11.15/figs/fig1.png")
plt.show()
