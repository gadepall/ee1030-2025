import numpy as np
import matplotlib.pyplot as plt

# Define the vectors
a = np.array([1, 2, 3])
b = np.array([3, 2, 6])

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot vector a
ax.quiver(0, 0, 0, a[0], a[1], a[2], color='r', label='Vector a = [1, 2, 3]', linewidth=2)
# Plot vector b
ax.quiver(0, 0, 0, b[0], b[1], b[2], color='b', label='Vector b = [3, 2, 6]', linewidth=2)

# Set the limits and labels
ax.set_xlim([0, 4])
ax.set_ylim([0, 4])
ax.set_zlim([0, 7])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Angle Between Vectors a and b')
ax.legend()

plt.tight_layout()
plt.show()

