import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define vectors
B = np.array([1, 0, 0])
C = np.array([np.cos(np.pi/6), np.sin(np.pi/6), 0])
cross_BC = np.cross(B, C)
A1 = 2 * cross_BC
A2 = -2 * cross_BC

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Function to draw vectors
def draw_vector(ax, vec, color, label):
    ax.quiver(0, 0, 0, vec[0], vec[1], vec[2], color=color, label=label)

# Draw vectors
draw_vector(ax, B, 'r', 'B')
draw_vector(ax, C, 'g', 'C')
draw_vector(ax, A1, 'b', 'A = +2(B×C)')
draw_vector(ax, A2, 'm', 'A = -2(B×C)')

# Axes settings
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.set_title("Vectors A, B, C in 3D")

plt.show()