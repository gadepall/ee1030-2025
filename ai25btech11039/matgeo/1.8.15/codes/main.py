# 3D visualization for distance |AB| = 9
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
import numpy as np

A = np.array([-3.0, -14.0, 0.0])
a_val = -3.0              # from |AB| = 9
B = np.array([a_val, -5.0, 0.0])
R = 9.0

# Circle (locus) centered at A of radius 9 in z=0
theta = np.linspace(0, 2*np.pi, 400)
circle = np.column_stack([A[0] + R*np.cos(theta),
                          A[1] + R*np.sin(theta),
                          np.zeros_like(theta)])

# Line y = -5 (locus for B)
x_line = np.linspace(A[0]-15, A[0]+15, 200)
line = np.column_stack([x_line, -5*np.ones_like(x_line),
                        np.zeros_like(x_line)])

# Segment AB
t = np.linspace(0, 1, 100)
seg = (1 - t)[:, None] * A + t[:, None] * B

fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(111, projection='3d')

ax.plot(circle[:,0], circle[:,1], circle[:,2], linewidth=1.5)
ax.plot(line[:,0], line[:,1], line[:,2], linewidth=1.2, linestyle='--')
ax.plot(seg[:,0], seg[:,1], seg[:,2], linewidth=2)

ax.scatter(*A, s=60)
ax.scatter(*B, s=60)
ax.text(*A, "  A(-3,-14)")
ax.text(*B, "  B(-3,-5)")

ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
ax.view_init(elev=22, azim=35)
ax.set_xlim([A[0]-12, A[0]+12])
ax.set_ylim([min(A[1], B[1])-6, max(A[1], B[1])+6])
ax.set_zlim([-0.5, 0.5])

plt.tight_layout()
plt.show()
