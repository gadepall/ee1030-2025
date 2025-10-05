import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define vectors
v1 = [1, -1, 0]  # i - j
v2 = [0, 1, -1]  # j - k

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot vectors from origin
ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='r', label='i - j')
ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='b', label='j - k')

# Axes labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set axis limits for better view
ax.set_xlim([-1, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

ax.legend()
plt.title("3D Vectors: i - j and j - k")
plt.show()
