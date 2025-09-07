# Code by Aarush
# August 28, 2025
# Released under GNU GPL
# Section Formula - Trisection of a Line Segment in 3D

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given points
P = np.array(([4, 2, -6])).reshape(-1,1)
Q = np.array(([10, -16, 6])).reshape(-1,1)

# Points dividing PQ in 1:2 and 2:1 (Trisection points)
R = (2*P + Q)/3   # Point closer to P
S = (P + 2*Q)/3   # Point closer to Q

# print("Trisection points are:")
# print("R =", R.T)
# print("S =", S.T)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Line PQ
x_vals = [P[0,0], Q[0,0]]
y_vals = [P[1,0], Q[1,0]]
z_vals = [P[2,0], Q[2,0]]
ax.plot(x_vals, y_vals, z_vals, label='$PQ$', color="blue")

# All points
points = np.block([[P,Q,R,S]])
ax.scatter(points[0,:], points[1,:], points[2,:], color="red", s=50)

# Labels using annotate with arrows (avoids overlap)
labels = ['P','Q','R','S']
offsets = [(5,5,5), (5,-5,5), (-5,5,5), (5,5,-5)]  # different offsets

for i, txt in enumerate(labels):
    dx, dy, dz = offsets[i]
    ax.text(points[0,i]+dx, points[1,i]+dy, points[2,i]+dz,
            f'{txt}({points[0,i]:.0f},{points[1,i]:.0f},{points[2,i]:.0f})',
            fontsize=9, color="black")
    ax.plot([points[0,i], points[0,i]+dx],
            [points[1,i], points[1,i]+dy],
            [points[2,i], points[2,i]+dz],
            color="gray", linestyle="dotted")  # arrow-like connector

# Equal axis scaling
max_range = np.array([points[0,:].max()-points[0,:].min(),
                      points[1,:].max()-points[1,:].min(),
                      points[2,:].max()-points[2,:].min()]).max() / 2.0

mid_x = (points[0,:].max()+points[0,:].min()) * 0.5
mid_y = (points[1,:].max()+points[1,:].min()) * 0.5
mid_z = (points[2,:].max()+points[2,:].min()) * 0.5

ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

# Beautify plot
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.legend()
ax.grid(True)

plt.show()
