import ctypes
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import os

# Load the shared library
lib = ctypes.CDLL('/home/shriyasnh/Desktop/matgeonew/4.7.50/codes/libline_perpendicular.so')
    
# Define function signatures
lib.get_point_on_line.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                 ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                 ctypes.c_double,
                                 ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.get_point_on_line.restype = None

def get_point_on_line(point, direction, t):
    """
    Get a point on a line given a starting point, direction vector, and parameter t
    Line equation: P = A + t * d
    """
    x, y, z = ctypes.c_double(), ctypes.c_double(), ctypes.c_double()
    lib.get_point_on_line(ctypes.c_double(point[0]), ctypes.c_double(point[1]), ctypes.c_double(point[2]),
                         ctypes.c_double(direction[0]), ctypes.c_double(direction[1]), ctypes.c_double(direction[2]),
                         ctypes.c_double(t),
                         ctypes.byref(x), ctypes.byref(y), ctypes.byref(z))
    return [x.value, y.value, z.value]

# Define the line
A = np.array([1, 2, 3])  # Starting point
d = np.array([1, 2, -5])  # Direction vector

# Create the plot
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot the plane: x + 2y - 5z + 9 = 0 (rearranged to z = (x + 2y + 9)/5)
xx, yy = np.meshgrid(np.linspace(-3, 5, 20), np.linspace(-2, 6, 20))
zz = (xx + 2*yy + 9) / 5
ax.plot_surface(xx, yy, zz, alpha=0.3, color='yellow', edgecolor='gray', linewidth=0.1)

# Plot the line using C function
#"Plotting line through point A with direction vector d"
t_values = np.linspace(-2, 2, 200)
line_points = []
for t in t_values:
    pt = get_point_on_line(A, d, t)
    line_points.append(pt)

line_points = np.array(line_points)

# Plot the line with high contrast
ax.plot(line_points[:, 0], line_points[:, 1], line_points[:, 2], 
        'b-', linewidth=3, label=f'Line: P = A + t*d', zorder=10)

# Mark the starting point A
ax.scatter([A[0]], [A[1]], [A[2]], color='red', s=100, 
          edgecolor='black', linewidth=2, label=f'Point A({A[0]},{A[1]},{A[2]})', zorder=15)

# Add text label for point A
ax.text(A[0]+0.2, A[1]+0.2, A[2]+0.2, f'A({A[0]},{A[1]},{A[2]})', 
        fontsize=12, fontweight='bold')

# Direction vector arrow from point A
arrow_scale = 0.8
ax.quiver(A[0], A[1], A[2], d[0]*arrow_scale, d[1]*arrow_scale, d[2]*arrow_scale,
          color='red', arrow_length_ratio=0.15, linewidth=3, 
          label=f'Direction d({d[0]},{d[1]},{d[2]})', zorder=12)

# Verify the line is perpendicular to the plane
# Plane normal vector is [1, 2, -5] (coefficients of x, y, z)
if np.allclose(np.cross(d, plane_normal), 0, atol=1e-9):
    print("Line is parallel to plane normal → line is perpendicular to plane")
else:
    print("Not perpendicular")

# Set labels and title
ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_zlabel('Z', fontsize=12)
ax.set_title('Line Perpendicular to Plane\nLine: P = A + t*d, Plane: x + 2y - 5z + 9 = 0', fontsize=14)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Set better viewing angle
ax.view_init(elev=20, azim=45)

# Create output directory and save
output_dir = '/home/shriyasnh/Desktop/matgeonew/4.7.50/figs'
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'line_perpendicular.png'), dpi=300, bbox_inches='tight')
plt.show()
