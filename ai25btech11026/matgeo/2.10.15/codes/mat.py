import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given vectors
a = np.array([1, 1, 0])
b = np.array([0, 1, 1])

# Cross product gives a vector perpendicular to both
v = np.cross(a, b)
v = v / np.linalg.norm(v)  # Unit vector

# The two perpendicular unit vectors are ±v
v1 = v
v2 = -v

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot given vectors
ax.quiver(0, 0, 0, a[0], a[1], a[2], color='r', label='a = (1,1,0)')
ax.quiver(0, 0, 0, b[0], b[1], b[2], color='g', label='b = (0,1,1)')

# Plot perpendicular unit vectors
ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='b', label='Unit perp vector +v')
ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='orange', label='Unit perp vector -v')

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Unit vectors perpendicular to a and b')
ax.legend()

# Save image
plt.savefig("perpendicular_vectors.png")
plt.show()
