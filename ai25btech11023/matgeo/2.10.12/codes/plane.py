

import sys                                          #for path to external scripts

import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D

#local imports
from line.funcs import *
#from triangle.funcs import *
#from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if


# Read points from output.data file
points = []
with open('output.data', 'r') as file:
    for line in file:
        coords = list(map(float, line.split()))
        points.append(coords)

# Convert to numpy arrays with required shape
P = np.array(points[0]).reshape(-1, 1)
Q = np.array(points[1]).reshape(-1, 1)
R = np.array(points[2]).reshape(-1, 1)


# Create a figure and a 3D Axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

a, b, c, d = 2, 1, 1, -3  # coefficients of the plane equation: ax + by + cz + d = 0

# Generate grid points for x and y
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)

# Calculate corresponding z values for each (x, y) pair to satisfy the plane equation
Z = (-a*X - b*Y - d) / c

# Plot the plane
ax.plot_surface(X, Y, Z, alpha=0.5)

#Generating all lines
#x_BC = line_gen(Q,R)

#Plotting all lines
#ax.plot(x_QR[0,:],x_QR[1,:], x_QR[2,:],label='$BC$')

# Scatter plot
colors = np.arange(2, 5)  # Example colors
tri_coords = np.block([P,Q,R])  # Stack P,Q,R vertically
ax.scatter(tri_coords[0, :], tri_coords[1, :], tri_coords[2, :], c=colors)
vert_labels = ['P', 'Q', 'R']

ax.quiver(1,-1,2, 8,4,4, color='r', linewidth=2, label='n')

for i, txt in enumerate(vert_labels):
    # Annotate each point with its label and coordinates
    ax.text(tri_coords[0, i], tri_coords[1, i], tri_coords[2, i],f'{txt}',fontsize=12, ha='center', va='bottom')
    #ax.text(tri_coords[0, i], tri_coords[1, i], tri_coords[2, i], f'{txt}\n({tri_coords[0, i]:.0f}, {tri_coords[1, i]:.0f}, {tri_coords[2, i]:.0f})',
    #         fontsize=12, ha='center', va='bottom')


ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

# Set limits and aspect ratio to magnify the plane
ax.set_xlim(-4, 4)  # Adjust limits based on your data
ax.set_ylim(-4, 4)  # Adjust limits based on your data
ax.set_zlim(-4, 4)  # Adjust limits based on your data
ax.set_box_aspect([1,1,1])  # Equal aspect ratio for x, y, and z axes
'''
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
'''
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('../figs/fig.png')

#else
#plt.show()
