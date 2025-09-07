import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define vectors
a = np.array([2, 3, 2])
b = np.array([2, 2, 1])

# Compute projection of a onto b
proj_scalar = np.dot(a, b) / np.dot(b, b)
proj = proj_scalar * b

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot origin
origin = [0, 0, 0]

# Plot vectors
ax.quiver(*origin, *a, color='blue', label='Vector a', linewidth=2)
ax.quiver(*origin, *b, color='green', label='Vector b', linewidth=2)
ax.quiver(*origin, *proj, color='red', label='Projection of a on b', linestyle='dashed', linewidth=2)

# Labels and settings
ax.set_xlim([0, 4])
ax.set_ylim([0, 4])
ax.set_zlim([0, 4])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Projection of Vector a onto Vector b')
ax.legend()
plt.tight_layout()
plt.show()
