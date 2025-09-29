# Triangle Plotting Script
# Author: Dhanush (based on GVV Sharma)
# September 13, 2025
# Draw a triangle, calculate area, and save figure

import sys
import os
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

# Add parent folder of 'triangle' and 'line' to Python path
sys.path.insert(0, '/home/dhanush-kumar-a/code/CoordGeo')

# Local imports
from triangle.funcs import tri_sides, tri_mid_pt
from line.funcs import dir_vec, norm_vec, line_gen


# -----------------------
# Triangle vertices (column vectors)
A = np.array([-1, 0]).reshape(-1,1)
B = np.array([1, 3]).reshape(-1,1)
C = np.array([3, 2]).reshape(-1,1)
m1 = dir_vec(A,B)
m2 = dir_vec(B,C)
m3 = dir_vec(C,A)

# Area using cross product
arvec = np.cross(m1[:,0], m3[:,0])
area = 0.5 * LA.norm(arvec)
print(f"Area of the triangle: {area:.3f}")

# Generate points for triangle sides
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

# Plot triangle sides
plt.plot(x_AB[0,:], x_AB[1,:], 'b', label='AB')
plt.plot(x_BC[0,:], x_BC[1,:], 'g', label='BC')
plt.plot(x_CA[0,:], x_CA[1,:], 'r', label='CA')

# Plot vertices
tri_coords = np.block([[A,B,C]])
plt.scatter(tri_coords[0,:], tri_coords[1,:], color='red')

# Annotate vertices
vert_labels = ['A','B','C']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt,
                 (tri_coords[0,i], tri_coords[1,i]),
                 textcoords="offset points",
                 xytext=(0,10),
                 ha='center',
                 fontsize=12, color='blue')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Triangle Plot')
plt.grid(True)
plt.axis('equal')
plt.legend()

# Save the figure
plt.savefig('../figs/triangle_plot.png', dpi=300)
print("Figure saved as figs/triangle_plot.png")

plt.show()
