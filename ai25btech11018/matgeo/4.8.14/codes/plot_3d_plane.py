import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

n = np.array([2, 1, 3])  # Normal vector to the plane
p = np.array([2, 3, 1])  # Position vector of point P
d = 26  # Plane constant

# Calculate the foot of perpendicular from P to the plane
t_foot = (d - np.dot(n, p)) / np.dot(n, n)
foot = p + t_foot * n

# Calculate image of P (reflection about the plane)
image = 2 * foot - p

# Create grid for the plane
xx, yy = np.meshgrid(np.linspace(0, 8, 8), np.linspace(0, 8, 8))
zz = (d - 2 * xx - yy) / 3

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xx, yy, zz, alpha=0.6, color='cyan', rstride=1, cstride=1, edgecolor='none')

# Plot point P, foot of perpendicular, and image
ax.scatter(*p, color='blue', s=80, label='P (2,3,1)')
ax.scatter(*foot, color='red', s=80, label='Foot of Perpendicular')
ax.scatter(*image, color='green', s=80, label='Image of P')

# Plot perpendicular line
ax.plot([p[0], foot[0]], [p[1], foot[1]], [p[2], foot[2]], color='black', lw=2, linestyle='--', label='Perpendicular')

ax.set_xlim(0, 8)
ax.set_ylim(0, 8)
ax.set_zlim(0, 8)

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Solution Graph: Foot, Distance, Image')
ax.legend()

plt.tight_layout()
plt.savefig('3d_plane_solution.png')
plt.show()
