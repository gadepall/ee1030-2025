import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import os

# Given points as column vectors (x,y,z)
A = np.array([-1, 2, 1]).reshape(-1,1)
B = np.array([1, -2, 5]).reshape(-1,1)
C = np.array([4, -7, 8]).reshape(-1,1)
D = np.array([2, -3, 4]).reshape(-1,1)

# Stack coordinates
coords = np.block([A,B,C,D])

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter points
ax.scatter(coords[0,:], coords[1,:], coords[2,:], color='r', s=50)

# Draw parallelogram edges
edges = [(A,B), (B,C), (C,D), (D,A)]
for edge in edges:
    pts = np.hstack(edge)
    ax.plot(pts[0,:], pts[1,:], pts[2,:], color='b')

# Fill parallelogram face
verts = [[A.flatten(), B.flatten(), C.flatten(), D.flatten()]]
ax.add_collection3d(Poly3DCollection(verts, alpha=0.3, facecolor='cyan'))

# Labels
ax.text(A[0,0], A[1,0], A[2,0], "A(-1,2,1)")
ax.text(B[0,0], B[1,0], B[2,0], "B(1,-2,5)")
ax.text(C[0,0], C[1,0], C[2,0], "C(4,-7,8)")
ax.text(D[0,0], D[1,0], D[2,0], "D(2,-3,4)")

# Axes
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
plt.title("Parallelogram in 3D")

# Save figure
save_path = '../figs/img.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path, dpi=300)

print(f"Image saved at: {save_path}")

plt.show()
