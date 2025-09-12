import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Step 1: Define vectors
a = np.array([1, 0, 0])   # |a| = 1
b = np.array([0, 2, 0])   # |b| = 2
c = np.array([0, 0, 3])   # |c| = 3

# Required vector
v = 3*a - 2*b + 2*c

# Step 2: Setup 3D figure
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Helper function to draw vectors with shifted labels
def draw_vector(ax, origin, vec, color, label, shift):
    ax.quiver(
        origin[0], origin[1], origin[2],
        vec[0], vec[1], vec[2],
        color=color, arrow_length_ratio=0.1, linewidth=2
    )
    ax.text(
        vec[0] + shift[0],
        vec[1] + shift[1],
        vec[2] + shift[2],
        label,
        fontsize=10, color=color
    )

# Step 3: Plot vectors with shifted labels
draw_vector(ax, [0,0,0], a, "blue",   "|a|=1",    shift=[0.2,0,0])
draw_vector(ax, [0,0,0], b, "green",  "|b|=2",    shift=[0,0.2,0])
draw_vector(ax, [0,0,0], c, "orange", "|c|=3",    shift=[0,0,0.3])
draw_vector(ax, [0,0,0], v, "red",    "3a - 2b + 2c", shift=[0.3,0.3,0.3])

# Step 4: Axis settings
max_range = np.max(np.abs([a, b, c, v])) + 1
ax.set_xlim([-max_range, max_range])
ax.set_ylim([-max_range, max_range])
ax.set_zlim([-max_range, max_range])

ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("3D Vector Diagram (Non-overlapping Labels)")

plt.show()

