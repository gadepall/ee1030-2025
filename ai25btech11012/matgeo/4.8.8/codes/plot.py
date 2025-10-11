#Code by Unnathi

import sys                                          #for path to external scripts
sys.path.insert(0, '/Users/unnathi/Documents/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#if using termux
import subprocess
import shlex
#end if

# Point on the plane
P = np.array([-1, 3, 2])

# Create a figure and a 3D Axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plane coefficients: 7x - 8y + 3z + 25 = 0
a, b, c, d = 7, -8, 3, 25  

# Generate grid points for x and y
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)

# Calculate corresponding z values
Z = (-a*X - b*Y - d) / c

# Plot the plane
ax.plot_surface(X, Y, Z, alpha=0.5, color="lightblue")

# Plot the single point P
ax.scatter(P[0], P[1], P[2], color='red', s=50)
ax.text(P[0], P[1], P[2], "P(-1,3,2)", fontsize=12, ha='center', va='bottom')

# Set limits and aspect ratio
ax.set_xlim(-5, 5)  
ax.set_ylim(-5, 5)  
ax.set_zlim(-5, 5)  
ax.set_box_aspect([1,1,1])  

plt.grid()
plt.axis('equal')

#if using termux
plt.savefig('/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/4.8.8/figs/fig.png')

plt.show()

