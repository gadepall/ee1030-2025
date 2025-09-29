import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

A = np.array([2, -4, -5])
B = np.array([2,  2,  3])
O = np.array([0, 0, 0])
C = A + B
points = np.array([O, A, C, B])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
verts = [[O, A, C, B]]
ax.add_collection3d(Poly3DCollection(verts, alpha=0.3, facecolor='cyan'))
edges = [(O, A), (O, B), (A, C), (B, C)]
for p1, p2 in edges:
    ax.plot(*zip(p1, p2), color='blue')
ax.plot(*zip(O, C), color='red', linestyle='--')
ax.plot(*zip(A, B), color='green', linestyle='--')

labels = {"O": O, "A": A, "B": B, "C": C}
for name, coord in labels.items():
    ax.scatter(*coord, color='black', s=10)
    ax.text(coord[0], coord[1], coord[2], f"{name}{tuple(coord)}", fontsize=9)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

max_range = np.array([points[:,0].max()-points[:,0].min(), 
                      points[:,1].max()-points[:,1].min(), 
                      points[:,2].max()-points[:,2].min()]).max() / 2.0
mid_x = (points[:,0].max()+points[:,0].min()) * 0.5
mid_y = (points[:,1].max()+points[:,1].min()) * 0.5
mid_z = (points[:,2].max()+points[:,2].min()) * 0.5
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

plt.show()
