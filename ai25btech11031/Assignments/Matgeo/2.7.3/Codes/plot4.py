import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Vectors
a = np.array([1, -1, 1])
b = np.array([2, -1, -3])
c = np.array([0, -3, 1])

# 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot vectors from origin
def draw_vector(v, color, label):
    ax.quiver(0, 0, 0, v[0], v[1], v[2],
              color=color, arrow_length_ratio=0.1, label=label)

draw_vector(a, 'r', 'a = (1,-1,1)')
draw_vector(b, 'g', 'b = (2,-1,-3)')
draw_vector(c, 'b', 'c = (0,-3,1)')

# Set plot limits
max_range = max(np.linalg.norm(a), np.linalg.norm(b), np.linalg.norm(c)) + 1
ax.set_xlim([-max_range, max_range])
ax.set_ylim([-max_range, max_range])
ax.set_zlim([-max_range, max_range])

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.savefig("plot4.png", dpi=300)
plt.show()

