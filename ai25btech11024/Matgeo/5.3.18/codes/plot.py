import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D

#local imports
from line.funcs import * 

#Given points
A = np.array(([2,2,3])).reshape(-1,1)

# Create a figure and a 3D Axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

a1, b1, c1, d1 = 2, -3, 5, -13  # coefficients of the plane equation: ax + by + cz + d = 0
a2, b2, c2, d2 = 3, 2, -4, 2
a3, b3, c3, d3 = 1, 1, -2, 2

# Generate grid points for x and y
x1 = np.linspace(-5, 5, 50)
y1 = np.linspace(-5, 5, 50)
X1, Y1 = np.meshgrid(x1, y1)

x2 = np.linspace(-5, 5, 50)
y2 = np.linspace(-5, 5, 50)
X2, Y2 = np.meshgrid(x2, y2)

x3 = np.linspace(-5, 5, 50)
y3 = np.linspace(-5, 5, 50)
X3, Y3 = np.meshgrid(x3, y3)

# Calculate corresponding z values for each (x, y) pair to satisfy the plane equation
Z1 = (-a1*X1 - b1*Y1 - d1) / c1
Z2 = (-a2*X2 - b2*Y2 - d2) / c2
Z3 = (-a3*X3 - b3*Y3 - d3) / c3

# Plot the plane
ax.plot_surface(X1, Y1, Z1, alpha=0.5)
ax.plot_surface(X2, Y2, Z2, alpha=0.5)
ax.plot_surface(X3, Y3, Z3, alpha=0.5)

# Scatter plot
ax.scatter(A[0], A[1], A[2], c='r')

ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

# Set limits and aspect ratio to magnify the plane
ax.set_xlim(-4, 4)  # Adjust limits based on your data
ax.set_ylim(-4, 4)  # Adjust limits based on your data
ax.set_zlim(-4, 4)  # Adjust limits based on your data
ax.set_box_aspect([1,1,1])  # Equal aspect ratio for x, y, and z axes

plt.grid() # minor
plt.axis('equal')

plt.savefig('../figs/img.png')
plt.show()
