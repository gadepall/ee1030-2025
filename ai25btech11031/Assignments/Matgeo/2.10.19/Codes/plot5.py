import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define vectors
u = np.array([1, -1, 1])
v = np.array([0, 1, 2])
w = np.array([1, 0, -1])

# Set up 3D plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Draw vectors
origin = np.array([0, 0, 0])  # starting point (0,0,0)

ax.quiver(*origin, *u, color='r', label='u = (1, -1, 1)')
ax.quiver(*origin, *v, color='g', label='v = (0, 1, 2)')
ax.quiver(*origin, *w, color='b', label='w = (1, 0, -1)')

# Axes labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Axes limits
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 3])

ax.legend()
ax.set_title("3D Plot of Vectors u, v, w")

# Save the figure
plt.savefig("plot5.png", dpi=300, bbox_inches="tight")

plt.show()

