import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Vectors
a = np.array([2, -3, 2])
b = np.array([2, 3, 1])

# Cross product and area
cross = np.cross(a, b)
area = 0.5 * np.linalg.norm(cross)
print("Area of triangle OAB:", area)

# Points
origin = np.array([0, 0, 0])
A = a
B = b

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot vectors a and b
ax.quiver(0, 0, 0, a[0], a[1], a[2], color='r', label='a = (2,-3,2)')
ax.quiver(0, 0, 0, b[0], b[1], b[2], color='b', label='b = (2,3,1)')

# Draw triangle OAB
verts = [[origin, A, B]]
ax.add_collection3d(Poly3DCollection(verts, alpha=0.3, facecolor='cyan'))

# Labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Set equal aspect ratio
ax.set_box_aspect([1,1,1])

# Save figure as image
plt.savefig("triangle_OAB.png", dpi=300)
plt.show()