import numpy as np

import math

import matplotlib.pyplot as plt

import numpy.linalg as LA

vecA = np.array([2,1,3])

vecB = np.array([3,5,-2])
crossprod = np.cross(vecA,vecB)
print(crossprod)

mod = np.linalg.norm(crossprod)
print(mod)

# Create a 3D plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

origin = np.array([0, 0, 0])

ax.quiver(*origin, *vecA, color='r', label='Vector (3, 5, -2)')
ax.quiver(*origin, *vecB, color='b', label='Vector (2, 1, 3)')

max_val = np.max(np.abs(np.concatenate((vecA, vecB))))
ax.set_xlim([-max_val, max_val])
ax.set_ylim([-max_val, max_val])
ax.set_zlim([-max_val, max_val])

# Add labels and a title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Two 3D Vectors')

# Add a legend
ax.legend()

# Add a grid for better visualization
ax.grid(True)

# Show the plot
plt.show()
