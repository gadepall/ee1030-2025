import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define vectors
a = np.array([2, 1, 3])
b = np.array([3, 5, -2])
cross_ab = np.cross(a, b)

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot vectors using quiver
ax.quiver(0, 0, 0, a[0], a[1], a[2], color='r', label=r'$\vec{a}$')
ax.quiver(0, 0, 0, b[0], b[1], b[2], color='b', label=r'$\vec{b}$')
ax.quiver(0, 0, 0, cross_ab[0], cross_ab[1], cross_ab[2], color='g', label=r'$\vec{a} \times \vec{b}$')

# Set labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("3D Representation of Vectors and Cross Product")

# Set axis limits for better visualization
ax.set_xlim([-20, 20])
ax.set_ylim([-20, 20])
ax.set_zlim([-20, 20])

# Show legend
ax.legend()

# Show plot
plt.show()
