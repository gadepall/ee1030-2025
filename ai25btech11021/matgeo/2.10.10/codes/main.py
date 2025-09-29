import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the vectors
a = np.array([1, 1, 1])
b = np.array([5/3, 2/3, 2/3])
c = np.array([0, 1, -1])

# Origin for vectors
origin = np.array([0, 0, 0])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot vectors a, b, and c
ax.quiver(*origin, *a, color='r', label='a', arrow_length_ratio=0.1)
ax.quiver(*origin, *b, color='g', label='b', arrow_length_ratio=0.1)
ax.quiver(*origin, *c, color='b', label='c', arrow_length_ratio=0.1)

# Setting the axes properties
ax.set_xlim([0, 2])
ax.set_ylim([0, 2])
ax.set_zlim([-2, 2])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.legend()
ax.set_title('Vectors a, b, and c in 3D')

# Save the figure
plt.savefig('python_plot.png')

# Optional: show the plot window
# plt.show()
