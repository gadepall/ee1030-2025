import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the three unit vectors with dot products = 1/2
a = np.array([1, 0, 0])
b = np.array([0.5, np.sqrt(3)/2, 0])
c = np.array([0.5, 1/(2*np.sqrt(3)), np.sqrt(2/3)])

# Vertices of parallelepiped
p1 = np.array([0,0,0])
p2 = a
p3 = b
p4 = c
p5 = a+b
p6 = b+c
p7 = c+a
p8 = a+b+c

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

# Bottom face
ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], 'grey')
ax.plot([p1[0], p3[0]], [p1[1], p3[1]], [p1[2], p3[2]], 'grey')
ax.plot([p2[0], p5[0]], [p2[1], p5[1]], [p2[2], p5[2]], 'grey')
ax.plot([p3[0], p5[0]], [p3[1], p5[1]], [p3[2], p5[2]], 'grey')

# Top face
ax.plot([p4[0], p7[0]], [p4[1], p7[1]], [p4[2], p7[2]], 'grey')
ax.plot([p4[0], p6[0]], [p4[1], p6[1]], [p4[2], p6[2]], 'grey')
ax.plot([p7[0], p8[0]], [p7[1], p8[1]], [p7[2], p8[2]], 'grey')
ax.plot([p6[0], p8[0]], [p6[1], p8[1]], [p6[2], p8[2]], 'grey')

# Vertical edges
ax.plot([p1[0], p4[0]], [p1[1], p4[1]], [p1[2], p4[2]], 'grey')
ax.plot([p2[0], p7[0]], [p2[1], p7[1]], [p2[2], p7[2]], 'grey')
ax.plot([p3[0], p6[0]], [p3[1], p6[1]], [p3[2], p6[2]], 'grey')
ax.plot([p5[0], p8[0]], [p5[1], p8[1]], [p5[2], p8[2]], 'grey')


ax.plot([], [], [], 'grey', label=r"Parallelepiped of volume $1/\sqrt{2}$")

ax.set_xlabel("X - AXIS")
ax.set_ylabel("Y - AXIS")
ax.set_zlabel("Z - AXIS")
ax.set_title("Parallelepiped with a·b = b·c = c·a = 1/2")
ax.legend()
ax.set_box_aspect([1,1,1])
ax.view_init(elev=15, azim=135)
plt.savefig("parallelepiped.png", dpi=300)
plt.show()
