import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given points
A = np.array([3, 4, 1])
B = np.array([5, 1, 6])

# Direction vector of the line
L = B - A

# For a point to be on the XZ plane, its y-coordinate must be 0.
# The parametric equation of the line is P(t) = A + t * L
# P(t) = (3 + t*2, 4 + t*(-3), 1 + t*5)

# Set the y-coordinate to 0:
# 4 + t*(-3) = 0
# 3*t = 4
# t = 4/3

t_intersect = 4/3

# Calculate the intersection point
C = A + t_intersect * L

print(f"The line crosses the XZ plane at point C: ({C[0]:.2f}, {C[1]:.2f}, {C[2]:.2f})")

# To find the angle with the XZ plane, we need the normal vector to the XZ plane.
# The normal vector to the XZ plane is (0, 1, 0)
normal_xz_plane = np.array([0, 1, 0])

# The angle theta between a line with direction vector L and a plane with normal vector N
# is given by sin(theta) = |L . N| / (||L|| * ||N||)
dot_product = np.dot(L, normal_xz_plane)
magnitude_L = np.linalg.norm(L)
magnitude_N = np.linalg.norm(normal_xz_plane)

sin_theta = abs(dot_product) / (magnitude_L * magnitude_N)
angle_radians = np.arcsin(sin_theta)
angle_degrees = np.degrees(angle_radians)

print(f"The angle the line makes with the XZ plane is: {angle_degrees:.2f} degrees")

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points A, B, and C
ax.scatter(A[0], A[1], A[2], color='red', s=100, label=f'A({A[0]},{A[1]},{A[2]})')
ax.scatter(B[0], B[1], B[2], color='blue', s=100, label=f'B({B[0]},{B[1]},{B[2]})')
ax.scatter(C[0], C[1], C[2], color='green', s=100, label=f'C({C[0]:.2f},{C[1]:.2f},{C[2]:.2f}) (Intersection)')

# Plot the line segment A-B
line_points_ab = np.array([A, B])
ax.plot(line_points_ab[:, 0], line_points_ab[:, 1], line_points_ab[:, 2], 'purple', label='Line Segment A-B')

# Plot the full line
t_vals = np.linspace(-2, 2, 100) # Extend the line for better visualization
line_full = A[:, np.newaxis] + t_vals * L[:, np.newaxis]
ax.plot(line_full[0, :], line_full[1, :], line_full[2, :], 'purple', linestyle='--', alpha=0.6, label='Full Line')

# Plot the XZ plane
x_plane = np.linspace(min(A[0], B[0], C[0]) - 2, max(A[0], B[0], C[0]) + 2, 10)
z_plane = np.linspace(min(A[2], B[2], C[2]) - 2, max(A[2], B[2], C[2]) + 2, 10)
X_plane, Z_plane = np.meshgrid(x_plane, z_plane)
Y_plane = np.zeros_like(X_plane)
ax.plot_surface(X_plane, Y_plane, Z_plane, alpha=0.3, color='gray', rstride=100, cstride=100, label='XZ Plane')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Line Intersection with XZ Plane and Angle')
ax.legend()
plt.tight_layout()
plt.savefig("fig2.png")
plt.show()
