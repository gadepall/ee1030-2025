import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the vectors (unit vectors 120° apart in xy-plane)
a = np.array([1.0, 0.0, 0.0])
b = np.array([-0.5, np.sqrt(3)/2, 0.0])
c = np.array([-0.5, -np.sqrt(3)/2, 0.0])

# Cross product (all same)
ab = np.cross(a, b)

# Create 3D plot
fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, projection="3d")

# Plot vector a (red arrow)
ax.quiver(0,0,0, *a, color="r")
ax.text(a[0], a[1], a[2], "a", color="r")

# Plot vector b (green thick line)
ax.plot([0, b[0]], [0, b[1]], [0, b[2]], color="g", linewidth=3)
ax.text(b[0] + 0.2, b[1], b[2], "b", color="g")   # label moved right

# Plot vector c (blue arrow)
ax.quiver(0,0,0, *c, color="b")
ax.text(c[0] - 0.2, c[1], c[2], "c", color="b")   # label moved left

# Plot cross product vector (black arrow)
ax.quiver(0,0,0, *ab, color="k", linestyle="dashed")
ax.text(ab[0], ab[1], ab[2], "a×b = b×c = c×a", color="k")

# Axes settings
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([0, 1.2])
ax.set_title("Vectors a, b, c and Cross Products")
plt.savefig("../figs/figb.png")
plt.show()

