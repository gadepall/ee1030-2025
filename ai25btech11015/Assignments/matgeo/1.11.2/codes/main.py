
import numpy as np

import matplotlib.pyplot as plt


# Read coordinates from unit_vector.dat
coords = []
with open('unit_vector.dat', 'r') as f:
    for line in f:
        if line.strip():
            coords.append([float(x) for x in line.strip().split()])


P = np.array(coords[0][:2])
Q = np.array(coords[1][:2])
A = np.array(coords[2][:2])
O = np.array([0, 0,0])


# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


# Plot PQ in 3D
ax.plot([coords[0][0], coords[1][0]], [coords[0][1], coords[1][1]], [coords[0][2], coords[1][2]], color='blue', label='PQ', linewidth=2)
# Plot OA in 3D
ax.plot([0, coords[2][0]], [0, coords[2][1]], [0, coords[2][2]], color='red', label='OA', linewidth=2)


# Label points in 3D
ax.scatter(coords[0][0], coords[0][1], coords[0][2], color='blue')
ax.text(coords[0][0], coords[0][1], coords[0][2], 'P', fontsize=12, ha='right', va='bottom')
ax.scatter(coords[1][0], coords[1][1], coords[1][2], color='blue')
ax.text(coords[1][0], coords[1][1], coords[1][2], 'Q', fontsize=12, ha='left', va='bottom')
ax.scatter(coords[2][0], coords[2][1], coords[2][2], color='red')
ax.text(coords[2][0], coords[2][1], coords[2][2], 'A', fontsize=12, ha='left', va='top')

ax.scatter(0, 0, 0, color='black')
ax.text(0, 0, 0, 'O', fontsize=12, ha='right', va='top')




ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.grid(True, linestyle='--', alpha=0.5)

# Save figure as fig.png in the ../figs directory
fig.savefig('../figs/fig.png', dpi=300)
