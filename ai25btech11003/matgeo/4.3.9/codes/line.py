import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Direction vector A and point B
A = np.array([3, 7, 2])
B = np.array([8, 3, 8])

# Parameter k for the line
k = np.linspace(-10, 10, 400)

# Compute line points: L = B + kA
line_points = B.reshape(3,1) + np.outer(A, k)

# Create a perpendicular offset so vector A doesn’t overlap the line
# Find a vector perpendicular to A by crossing with an arbitrary vector
arbitrary = np.array([1, 0, 0])
if np.allclose(np.cross(A, arbitrary), 0):
    arbitrary = np.array([0, 1, 0])
offset_dir = np.cross(A, arbitrary)
offset_dir = offset_dir / np.linalg.norm(offset_dir)
offset = offset_dir * 2  # magnitude of offset for visibility

# Base point for drawing A offset from the line
base_point = B + offset
arrow_end = base_point + A

# Plot setup
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the line L
ax.plot(line_points[0], line_points[1], line_points[2], color='blue', label='Line L')

# Mark point B on the line
ax.scatter(B[0], B[1], B[2], color='red', s=50, label='Point B (8,3,8)')

# Draw vector A at the offset base_point
ax.quiver(base_point[0], base_point[1], base_point[2],
          A[0], A[1], A[2], color='green', length=5, normalize=False, label='Vector A')

# Labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Line L and Parallel Vector A with Point B')
ax.legend()

# Save the figure
plt.savefig('fig1.png')
plt.close()

