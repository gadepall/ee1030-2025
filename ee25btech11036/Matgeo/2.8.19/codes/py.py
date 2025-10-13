import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define 3 coplanar vectors (lying in xy-plane)
a = np.array([1, 1, 0])
b = np.array([1, 0, 0])
c = np.array([0, 1, 0])

# Cross product b x c
b_cross_c = np.cross(b, c)

# Scalar triple product a . (b x c)
scalar_triple = np.dot(a, b_cross_c)

# Print the scalar triple product (should be 0)
print(f"Scalar triple product: {scalar_triple:.2f}")

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot origin
origin = np.array([0, 0, 0])

# Plot vectors
ax.quiver(*origin, *a, color='r', label='Vector a', linewidth=2)
ax.quiver(*origin, *b, color='g', label='Vector b', linewidth=2)
ax.quiver(*origin, *c, color='b', label='Vector c', linewidth=2)

# Plot b x c
ax.quiver(*origin, *b_cross_c, color='orange', linestyle='dashed', label='b x c', linewidth=2)

# Labels & limits
ax.set_xlim([0, 1.5])
ax.set_ylim([0, 1.5])
ax.set_zlim([0, 1.5])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f'Scalar Triple Product = {scalar_triple:.2f}')

# Legend and grid
ax.legend()
ax.grid(True)
plt.show()

