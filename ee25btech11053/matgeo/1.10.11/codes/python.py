import matplotlib.pyplot as plt
import numpy as np

# Define vectors
a = np.array([2, 3, -1])
b = np.array([1, -2, 1])

# Resultant vector: a + b
r = a + b

# Magnitude of resultant
mag_r = np.linalg.norm(r)

# Unit vector in direction of resultant
unit_r = r / mag_r

# Vector of magnitude 5, parallel to r
res = 5 * unit_r

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Origin
origin = np.array([0, 0, 0])

# Plot vectors
ax.quiver(*origin, *a, color='r', label='a', linewidth=2)
ax.quiver(*origin, *b, color='g', label='b', linewidth=2)
ax.quiver(*origin, *res, color='b', label='Resultant (Mag 5)', linewidth=2)

# Axes labels
ax.set_xlim([0, 5])
ax.set_ylim([0, 5])
ax.set_zlim([-2, 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Add legend
ax.legend()

plt.title('3D Plot: Vectors a, b, and Resultant Parallel of Mag 5')
plt.savefig("graph.png") 
plt.show()