#Code by GVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL

import sys
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
sys.path.insert(0, '/workspaces/urban-potato/matgeo/codes/CoordGeo/') 
from call import get_vectors_from_c
hat_symbol = '\u0302'
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

point_a, dir_b = get_vectors_from_c()
# Import the interface function from our C wrapper
from call import get_vectors_from_c

point_a, dir_b = get_vectors_from_c()
 
lambda_vals = np.array([-2, 2])
line_points = point_a + lambda_vals.reshape(-1,1) * dir_b

# --- Plotting ---
fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111, projection='3d')

# Plot the line segment itself
ax.plot(line_points[:, 0], line_points[:, 1], line_points[:, 2], color='blue', label='The Line')

# Plot the point 'a' on the line
ax.scatter(point_a[0], point_a[1], point_a[2], color='red', s=100, label='Point $\\vec{a}$')

# Plot the direction vector 'd' starting from point 'a'
ax.quiver(point_a[0], point_a[1], point_a[2], 
          dir_b[0], dir_b[1], dir_b[2], 
          color='green', label='Direction Vector $\\vec{b}$', length=5, arrow_length_ratio=0.3)

# Add text labels for the point and vectors
ax.text(point_a[0], point_a[1], point_a[2] + 0.5, f' $\\vec{{a}} = ({point_a[0]:.0f}, {point_a[1]:.0f}, {point_a[2]:.0f})$')
ax.text(point_a[0] + dir_b[0], point_a[1] + dir_b[1], point_a[2] + dir_b[2], ' $\\vec{b}$')

# --- Formatting ---
ax.set_title('Vector Equation of the Line')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

ax.grid(True)

ax.legend()
plt.show()
plt.savefig('../figs/fig1.png')
