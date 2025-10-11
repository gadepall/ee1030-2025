import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Point the line passes through
point = np.array([5, 2, -4])
# Direction vector
direction = np.array([3, 2, -8])

# Parameter t
t = np.linspace(-5, 5, 100)

# Parametric equations of the line
x = point[0] + direction[0] * t
y = point[1] + direction[1] * t
z = point[2] + direction[2] * t

# Create the figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the line
ax.plot(x, y, z, color='blue', label='Line through (5,2,-4) parallel to (3,2,-8)')

# Highlight the given point
ax.scatter(point[0], point[1], point[2], color='red', s=50, label='Point (5,2,-4)')

# Axis labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Line Plot')
ax.legend()

plt.show()