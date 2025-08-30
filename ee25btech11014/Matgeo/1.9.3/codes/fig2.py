import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Define the 3D figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Define points of rectangle
points = np.array([
    [0, 0, 0],   # A
    [4, 0, 0],   # B
    [4, -3, 0],  # C
    [0, -3, 0],  # D
    [0, 0, 0]    # back to A to close
])

# Plot the rectangle edges
ax.plot(points[:, 0], points[:, 1], points[:, 2], 'g--', label='Rectangle')

# Plot the diagonal line segment (from A=(0,0,0) to C=(4,-3,0))
ax.plot([0, 4], [0, -3], [0, 0], 'b', linewidth=2, label='Diagonal')

# Mark the key points
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='r', s=60, label='Points')

# Add labels
labels = ["(0,0)", "(4,0)", "(4,-3)", "(0,-3)"]
for i, txt in enumerate(labels):
    ax.text(points[i, 0], points[i, 1], points[i, 2], txt)

# Set labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Show grid and legend
ax.grid(True)
ax.legend()

plt.savefig('fig2.png', dpi=300)

plt.show()

