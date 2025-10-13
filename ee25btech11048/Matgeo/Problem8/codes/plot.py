import numpy as np
import matplotlib.pyplot as plt

# Given point
A = np.array([1, -2, 9])

# Line: r = r0 + lambda*d
r0 = np.array([4, 2, 7])
d = np.array([3, 4, 2])
lambda_vals = np.linspace(-1, 2, 100)
line_points = r0.reshape(3,1) + d.reshape(3,1) * lambda_vals

# Intersection point
P = r0 + d

# Plane: x - y + z = 10 => z = 10 - x + y
x_plane = np.linspace(-5, 10, 20)
y_plane = np.linspace(-5, 10, 20)
X, Y = np.meshgrid(x_plane, y_plane)
Z = 10 - X + Y

# 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot plane
ax.plot_surface(X, Y, Z, alpha=0.3, color='cyan', rstride=1, cstride=1, edgecolor='none')

# Plot line
ax.plot(line_points[0,:], line_points[1,:], line_points[2,:], color='blue', label="Line r=r0+λd")

# Plot points
ax.scatter(A[0], A[1], A[2], color='red', s=50, label="Point A(1,-2,9)")
ax.scatter(P[0], P[1], P[2], color='green', s=50, label="Intersection P(7,6,9)")

# Dotted line from A to P
ax.plot([A[0], P[0]], [A[1], P[1]], [A[2], P[2]], color='magenta', linestyle='--', label="Distance d")

# Labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title("Distance from Point to Line-Plane Intersection")
ax.legend()
plt.show()

