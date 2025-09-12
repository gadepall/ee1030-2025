import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Points
A = (1, 2, 3)
B = (-1, -2, -1)
C = (2, 3, 2)
D = (4, 7, 6)

# Plot setup
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points
ax.scatter(*A, color="r", label="A(1,2,3)")
ax.scatter(*B, color="g", label="B(-1,-2,-1)")
ax.scatter(*C, color="b", label="C(2,3,2)")
ax.scatter(*D, color="orange", label="D(4,7,6)")

# Draw parallelogram edges
edges = [(A, B), (B, C), (C, D), (D, A)]
for p1, p2 in edges:
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], 'k-')

# Fill parallelogram surface
verts = [[A, B, C, D]]
ax.add_collection3d(Poly3DCollection(verts, alpha=0.2, facecolor='cyan'))

# Labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.legend()

plt.show()