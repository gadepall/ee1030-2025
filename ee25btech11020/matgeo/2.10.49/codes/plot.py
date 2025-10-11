
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

A = np.array([2, 1, 1])
B = np.array([1, -1, 1])
C = np.array([3, 2, 6])
P = np.array([0, 0.9486833, -0.3162277])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

origin = np.array([0, 0, 0])

ax.quiver(*origin, *A, color='r', label='A', arrow_length_ratio=0.1)
ax.quiver(*origin, *B, color='g', label='B', arrow_length_ratio=0.1)
ax.quiver(*origin, *C, color='b', label='C', arrow_length_ratio=0.1)
ax.quiver(*origin, *P, color='m', label='P', arrow_length_ratio=0.3)

ax.text(A[0], A[1], A[2], "A")
ax.text(B[0], B[1], B[2], "B")
ax.text(C[0], C[1], C[2], "C")
ax.text(P[0], P[1], P[2], "P")

ax.set_xlim([-4, 4])
ax.set_ylim([-4, 4])
ax.set_zlim([-4, 7])

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')


ax.view_init(elev=20, azim=-120)

plt.savefig("../figs/fig.png")
