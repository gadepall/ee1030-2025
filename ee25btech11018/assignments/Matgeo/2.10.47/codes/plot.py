import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define vectors for a = 1/sqrt(3)
a = 1/np.sqrt(3)
p = np.array([1, 0, a])
q = np.array([a, 1, 0])
r = np.array([1, a, 1])

# Parallelepiped vertices (8 corners)
O  = np.array([0, 0, 0])     # origin
P  = p
Q  = q
R  = r
PQ = p + q
PR = p + r
QR = q + r
PQR = p + q + r

vertices = [O, P, Q, PQ, R, PR, QR, PQR]

# Faces of parallelepiped (each face is a list of 4 vertices)
faces = [
    [O, P, PQ, Q],
    [O, P, PR, R],
    [O, Q, QR, R],
    [P, PQ, PQR, PR],
    [Q, PQ, PQR, QR],
    [R, PR, PQR, QR]
]

# Plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Draw faces
ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', 
                                     edgecolors='black', alpha=0.6))

# Draw vectors p, q, r
ax.quiver(0, 0, 0, *p, color='r', label='p')
ax.quiver(0, 0, 0, *q, color='g', label='q')
ax.quiver(0, 0, 0, *r, color='b', label='r')

# Set limits
all_points = np.array(vertices)
ax.set_xlim([np.min(all_points[:,0])-0.5, np.max(all_points[:,0])+0.5])
ax.set_ylim([np.min(all_points[:,1])-0.5, np.max(all_points[:,1])+0.5])
ax.set_zlim([np.min(all_points[:,2])-0.5, np.max(all_points[:,2])+0.5])

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Parallelopiped formed by p, q, r (a = 1/sqrt(3))")
ax.legend()

plt.show()

