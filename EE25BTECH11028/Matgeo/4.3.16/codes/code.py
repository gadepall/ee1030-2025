import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given points
P1 = np.array([2, 1, 0])
P2 = np.array([3, -2, -2])
P3 = np.array([3, 1, 7])

# Create a meshgrid for x, y
xx, yy = np.meshgrid(range(-2, 6), range(-3, 6))

# Equation of plane: 7x + 3y - z - 17 = 0  => z = 7x + 3y - 17
zz = 7*xx + 3*yy - 17

# Plot
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface (plane)
ax.plot_surface(xx, yy, zz, alpha=0.5, color='cyan')

# Plot points
ax.scatter(*P1, color='r', s=50, label='P1 (2,1,0)')
ax.scatter(*P2, color='g', s=50, label='P2 (3,-2,-2)')
ax.scatter(*P3, color='b', s=50, label='P3 (3,1,7)')

# Labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title("Plane: 7x + 3y - z - 17 = 0")

ax.legend()
plt.savefig("fig6.png")
plt.show()
