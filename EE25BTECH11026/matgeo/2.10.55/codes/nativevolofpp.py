import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp
mp.use('TkAgg')
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define three unit vectors with given dot products = 0.5
a = np.array([1, 0, 0])
b = np.array([0.5, np.sqrt(3)/2, 0])                 
c = np.array([0.5, 1/2*np.sqrt(3), np.sqrt(2/3)])   
# Gram matrix
G = np.array([[np.dot(a,a), np.dot(a,b), np.dot(a,c)],
              [np.dot(b,a), np.dot(b,b), np.dot(b,c)],
              [np.dot(c,a), np.dot(c,b), np.dot(c,c)]])

# Volume of parallelepiped
volume = np.sqrt(np.linalg.det(G))
print("Volume of parallelepiped =", round(volume,4))

# Vertices
O = np.array([0,0,0])
A = a
B = b
C = c
AB = a+b
AC = a+c
BC = b+c
ABC = a+b+c

vertices = [O, A, B, C, AB, AC, BC, ABC]
labels = ["O","A","B","C","A+B","A+C","B+C","A+B+C"]

# Define faces
faces = [
    [O, A, AB, B],
    [O, A, AC, C],
    [O, B, BC, C],
    [A, AB, ABC, AC],
    [B, AB, ABC, BC],
    [C, AC, ABC, BC]
]

# Plot
fig = plt.figure(figsize=(9,7))
ax = fig.add_subplot(111, projection='3d')

# Draw faces
poly3d = [[list(v) for v in face] for face in faces]
ax.add_collection3d(Poly3DCollection(poly3d, alpha=0.3, facecolor='cyan'))

# Draw vectors
ax.quiver(0,0,0, a[0],a[1],a[2], color='r', linewidth=2, label='a')
ax.quiver(0,0,0, b[0],b[1],b[2], color='g', linewidth=2, label='b')
ax.quiver(0,0,0, c[0],c[1],c[2], color='b', linewidth=2, label='c')

# Label vertices
for i, v in enumerate(vertices):
    ax.text(v[0], v[1], v[2], labels[i], fontsize=10, color='black')

# Labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Parallelepiped formed by unit vectors a, b, c")

ax.set_box_aspect([1,1,1])  # equal aspect
ax.legend()
plt.savefig("/home/user/Matrix/Matgeo_assignments/2.10.55/figs/Figure-1.png")
plt.show()

