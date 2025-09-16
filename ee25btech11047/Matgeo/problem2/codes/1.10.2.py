import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define vectors
a = np.array([2, -1, 1])
b = np.array([0, 2, 1])
result = a + b                 # a + b
unit_result = result / np.linalg.norm(result)   # unit vector

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the resultant vector
ax.quiver(0, 0, 0, result[0], result[1], result[2], color='b', label='a+b', arrow_length_ratio=0.1)

# Plot the unit vector (scaled to length 1)
ax.quiver(0, 0, 0, unit_result[0], unit_result[1], unit_result[2], color='r', label='Unit vector', arrow_length_ratio=0.1)

# Labels
ax.set_xlim([0, 3])
ax.set_ylim([0, 3])
ax.set_zlim([0, 3])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()
