import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given points
P = np.array([-2, -1, -3])  # Point from which perpendicular is drawn
F = np.array([1, -3, 3])    # Foot of the perpendicular

# Normal vector to the plane (vector PF)
n = F - P

# Create a grid of points (x, y)
xx, yy = np.meshgrid(range(-5, 5), range(-5, 5))

# Calculate corresponding z for the plane using plane equation: n•(r - F) = 0
# => n_x (x - x0) + n_y (y - y0) + n_z (z - z0) = 0
# => z = ( -n_x (x - x0) - n_y (y - y0) ) / n_z + z0

a, b, c = n
x0, y0, z0 = F

# Avoid division by zero in case c = 0
if c != 0:
    zz = (-a * (xx - x0) - b * (yy - y0)) / c + z0
else:
    zz = np.zeros_like(xx)  # Plane is vertical; adjust accordingly

# Plotting
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the plane
ax.plot_surface(xx, yy, zz, alpha=0.5, color='cyan')

# Plot points P and F
ax.scatter(*P, color='red', s=100, label='Point P (-2, -1, -3)')
ax.scatter(*F, color='blue', s=100, label='Foot F (1, -3, 3)')

# Plot line segment PF
ax.plot([P[0], F[0]], [P[1], F[1]], [P[2], F[2]], color='green', linestyle='--', label='Perpendicular')

# Labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Plane and Perpendicular Foot')
ax.legend()

plt.show()
