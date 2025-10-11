import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the shared library
lib_geometry = ctypes.CDLL("./code8.so")

# Define the argument types and return type for the C function
lib_geometry.findIntersectionAndAngle.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,  # x1, y1, z1 (Point A)
    ctypes.c_double, ctypes.c_double, ctypes.c_double,  # x2, y2, z2 (Point B)
    ctypes.POINTER(ctypes.c_double), # ix (intersection x)
    ctypes.POINTER(ctypes.c_double), # iy (intersection y)
    ctypes.POINTER(ctypes.c_double), # iz (intersection z)
    ctypes.POINTER(ctypes.c_double)  # angle_degrees
]
lib_geometry.findIntersectionAndAngle.restype = None

# Given points
A = np.array([3.0, 4.0, 1.0]) # Use floats for ctypes compatibility
B = np.array([5.0, 1.0, 6.0])

# Create ctypes doubles to hold the results
ix_result = ctypes.c_double()
iy_result = ctypes.c_double()
iz_result = ctypes.c_double()
angle_result = ctypes.c_double()

# Call the C function
lib_geometry.findIntersectionAndAngle(
    A[0], A[1], A[2],
    B[0], B[1], B[2],
    ctypes.byref(ix_result),
    ctypes.byref(iy_result),
    ctypes.byref(iz_result),
    ctypes.byref(angle_result)
)

intersection_point = np.array([ix_result.value, iy_result.value, iz_result.value])
angle_with_xz_plane = angle_result.value

print(f"The line crosses the XZ plane at point C: ({intersection_point[0]:.2f}, {intersection_point[1]:.2f}, {intersection_point[2]:.2f})")
print(f"The angle the line makes with the XZ plane is: {angle_with_xz_plane:.2f} degrees")

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot points A, B, and C
ax.scatter(A[0], A[1], A[2], color='red', s=100, label=f'A({A[0]},{A[1]},{A[2]})')
ax.scatter(B[0], B[1], B[2], color='blue', s=100, label=f'B({B[0]},{B[1]},{B[2]})')
ax.scatter(intersection_point[0], intersection_point[1], intersection_point[2],
           color='green', s=100, zorder=5, label=f'C({intersection_point[0]:.2f},{intersection_point[1]:.2f},{intersection_point[2]:.2f}) (Intersection)')

# Annotate points
ax.text(A[0], A[1], A[2], f'  A', color='red', fontsize=10)
ax.text(B[0], B[1], B[2], f'  B', color='blue', fontsize=10)
ax.text(intersection_point[0], intersection_point[1], intersection_point[2],
        f'  C',
        color='green', fontsize=10)


# Plot the line segment A-B
line_points_ab = np.array([A, B])
ax.plot(line_points_ab[:, 0], line_points_ab[:, 1], line_points_ab[:, 2], 'purple', linewidth=2, label='Line Segment A-B')

# Plot the full line for better visualization, extending beyond A and B
# Direction vector
L = B - A
t_vals = np.linspace(-1, 2, 100) # Extend the line
line_full_x = A[0] + t_vals * L[0]
line_full_y = A[1] + t_vals * L[1]
line_full_z = A[2] + t_vals * L[2]
ax.plot(line_full_x, line_full_y, line_full_z, 'purple', linestyle='--', alpha=0.6, label='Extended Line')


# Plot the XZ plane (y=0)
x_plane_range = np.linspace(min(A[0], B[0], intersection_point[0]) - 2,
                            max(A[0], B[0], intersection_point[0]) + 2, 10)
z_plane_range = np.linspace(min(A[2], B[2], intersection_point[2]) - 2,
                            max(A[2], B[2], intersection_point[2]) + 2, 10)
X_plane, Z_plane = np.meshgrid(x_plane_range, z_plane_range)
Y_plane = np.zeros_like(X_plane) # Y-coordinate is 0 for XZ plane

ax.plot_surface(X_plane, Y_plane, Z_plane, alpha=0.2, color='gray', label='XZ Plane')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Line Intersection with XZ Plane and Angle')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.show()
