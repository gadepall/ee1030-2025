import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# Define the vectors
a = np.array([4, 5, -1])
b = np.array([1, -4, 5])
c = np.array([3, 1, -1])
# Find a direction for d (perpendicular to both c and b)
d_dir = np.cross(c, b)
# Find k such that d*a = 21
k = 21 / np.dot(d_dir, a)
d = k * d_dir
# Origin for all vectors
origin = np.zeros(3)
# Set up 3D plot
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection='3d')
ax.quiver(*origin, *a, color='r', label='a', length=np.linalg.norm(a), arrow_length_ratio=0.1)
ax.quiver(*origin, *b, color='g', label='b', length=np.linalg.norm(b), arrow_length_ratio=0.1)
ax.quiver(*origin, *c, color='b', label='c', length=np.linalg.norm(c), arrow_length_ratio=0.1)
ax.quiver(*origin, *d, color='k', label='d', length=np.linalg.norm(d), arrow_length_ratio=0.15)
# Styling and labels
ax.set_xlim([0, 8])
ax.set_ylim([0, 8])
ax.set_zlim([-2, 8])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Plot of Vectors a, b, c, and d')
ax.legend()
plt.tight_layout()
plt.show() 