import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define vectors
a = np.array([np.sqrt(3), 0, 0])  # vector a, magnitude √3
b = np.array([2*np.sqrt(3)/4, np.sqrt(3), 0])  # vector b, magnitude 4, dot = 2√3

# Verify magnitudes and dot product
mag_a = np.linalg.norm(a)
mag_b = np.linalg.norm(b)
dot_ab = np.dot(a, b)
theta = np.degrees(np.arccos(dot_ab / (mag_a * mag_b)))

# Create 3D plot
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')

# Plot origin
origin = np.array([0, 0, 0])

# Plot vectors
ax.quiver(*origin, *a, color='r', label='a (|a|=√3)', arrow_length_ratio=0.1)
ax.quiver(*origin, *b, color='b', label='b (|b|=4)', arrow_length_ratio=0.1)

# Annotate vectors
ax.text(*a, 'a', color='r')
ax.text(*b, 'b', color='b')

# Set axes limits
ax.set_xlim([0, 4])
ax.set_ylim([0, 4])
ax.set_zlim([0, 4])

# Labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f"Angle between a and b = {theta:.0f}°")

ax.legend()
plt.tight_layout()

# Save and show figure
plt.savefig("vectors_angle.png")
plt.show()
