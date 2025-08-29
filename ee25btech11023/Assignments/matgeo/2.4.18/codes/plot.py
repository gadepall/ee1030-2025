#Code by GVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL
#Point Vectors

import sys                                          #for path to external scripts
sys.path.insert(0, '/workspaces/urban-potato/matgeo/codes/CoordGeo/')        #path to my scripts

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Import the interface and get vectors directly from the C library
from call import get_vectors_from_c
m1, m2 = get_vectors_from_c()

# Create the plot
fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(projection='3d')

# Plot the vectors AS ARROWS using ax.quiver
# The format is quiver(start_x, start_y, start_z, direction_x, direction_y, direction_z)
ax.quiver(0, 0, 0, m1[0], m1[1], m1[2], color='blue', label='Vector m1')
ax.quiver(0, 0, 0, m2[0], m2[1], m2[2], color='red', label='Vector m2')

# Add text labels at the tip of each vector
ax.text(m1[0], m1[1], m1[2], f' m1 ({m1[0]:.2f}, {m1[1]:.2f}, {m1[2]:.2f})')
ax.text(m2[0], m2[1], m2[2], f' m2 ({m2[0]:.2f}, {m2[1]:.2f}, {m2[2]:.2f})')

# Format the plot
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim([-6, 6]); ax.set_ylim([-6, 6]); ax.set_zlim([-6, 6])
ax.view_init(elev=20, azim=30)
ax.legend()
plt.grid(True)

# Save the plot
plt.savefig('fig1.png')
plt.show()