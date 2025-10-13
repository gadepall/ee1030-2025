# Code by GVV Sharma
# September 12, 2023
# Revised July 21, 2024
# released under GNU GPL

# Point Vectors

import sys
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D

# Given points
A = np.array(([1, 1, 1])).reshape(-1, 1)  # reshaped as column vector (3,1)

# Create a figure and a 3D Axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

a, b, c, d = 1, -1, 1, 4  # coefficients of the plane equation: ax + by + cz + d = 0

# Generate grid points for x and y
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)

# Calculate corresponding z values for each (x, y) pair to satisfy the plane equation
Z = (-a*X - b*Y - d) / c

# Plot the plane
ax.plot_surface(X, Y, Z, alpha=0.5, color='grey')

# Use np.block and flatten to get scatter coordinates as 1D array
coords = np.block([A]).flatten()
ax.scatter(coords[0], coords[1], coords[2], color='red', s=50)  # scatter plot point A

# Add text label for point A
ax.text(coords[0], coords[1], coords[2], 'P', fontsize=12, ha='center', va='bottom')

# Set labels and title (optional)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Plane and Point A')

# Save the figure
plt.savefig('../figs/fig1.png')

# Show the plot
plt.show()
