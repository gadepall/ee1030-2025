#Code by GVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL
import sys                                          #for path to external scripts
sys.path.insert(0, '/workspaces/urban-potato/matgeo/codes/CoordGeo/') 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#local imports
from line.funcs import *
from triangle.funcs import *

from call import get_line_data_from_c

# Get the intersection point P, and the line's defining vectors a and d
P, point_a, dir_d = get_line_data_from_c()
print(f"Intersection Point: ({P[0]:.0f}, {P[1]:.0f}, {P[2]:.0f})")

lambda_vals = np.array([-3, 3])
line_points = point_a + lambda_vals[:, np.newaxis] * dir_d
 
a_plane, b_plane, c_plane, d_plane = 0, 0, 1, 0
x = np.linspace(-4, 12, 10)   
y = np.linspace(-5, 15, 10)   
X_plane, Y_plane = np.meshgrid(x, y)
 
Z_plane = (-a_plane * X_plane - b_plane * Y_plane - d_plane) / c_plane

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X_plane, Y_plane, Z_plane, alpha=0.2, color='gray', label='XY Plane')

