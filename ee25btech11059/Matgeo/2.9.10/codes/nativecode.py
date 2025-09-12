import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Line3DCollection

# Define vectors
a = np.array([1, 0, 0])
b = np.array([-0.5, 1, 0])
a_plus_2b = a + 2 * b

# Confirm perpendicularity
dot_product = np.dot(a, a_plus_2b)
print("Dot product a · (a + 2b):", dot_product)  # Should be 0

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title("Vectors a, b, and a + 2b (Perpendicular)")

# Plot origin
origin = np.zeros(3)

# Plot vectors
ax.quiver(*origin, *a, color='blue', label='a')
ax.quiver(*origin, *b, color='green', label='b')
ax.quiver(*origin, *a_plus_2b, color='red', label='a + 2b')

# ---- Add 90-degree arc ----
# Normalize vectors
a_unit = a / np.linalg.norm(a)
a2b_unit = a_plus_2b / np.linalg.norm(a_plus_2b)

# Create arc between a and a+2b
theta = np.linspace(0, np.pi / 2, 30)
arc_radius = 0.4
arc_points = np.array([arc_radius * (np.cos(t) * a_unit + np.sin(t) * a2b_unit) for t in theta])

# Plot the arc
ax.plot(arc_points[:, 0], arc_points[:, 1], arc_points[:, 2], color='black')

# Label the angle
angle_label_pos = arc_radius * (np.cos(np.pi / 4) * a_unit + np.sin(np.pi / 4) * a2b_unit)
ax.text(*angle_label_pos, "90°", fontsize=12, color='black')

# Axis settings
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim([-1, 2])
ax.set_ylim([-1, 2])
ax.set_zlim([-1, 1])
ax.legend()

# Save figure
plt.savefig("graph4.png")
print("Saved as graph4.png")

# Optional: Show the plot
# plt.show()

