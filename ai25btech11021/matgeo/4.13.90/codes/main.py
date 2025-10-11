import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

P = np.array([1, -2, 1])
F = np.array([8/3, 4/3, -7/3])
A, B, C, D_plane = 1, 2, -2, 10

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(*P, color='r', s=100, label=r'Point P(1, -2, 1)')
ax.scatter(*F, color='g', s=100, label=r'Foot of Perpendicular F($\frac{8}{3}, \frac{4}{3}, -\frac{7}{3}$)')

ax.plot([P[0], F[0]], [P[1], F[1]], [P[2], F[2]], 'k--', label='Perpendicular Line PF')

x_min, x_max = -1, 4
y_min, y_max = -4, 4

xx, yy = np.meshgrid(np.linspace(x_min, x_max, 10), np.linspace(y_min, y_max, 10))

zz = (A * xx + B * yy - D_plane) / C

ax.plot_surface(xx, yy, zz, alpha=0.5, rstride=100, cstride=100, color='c')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title(r'3D Plot of Point, Plane, and Foot of Perpendicular')

ax.legend()
ax.view_init(elev=20, azim=45)
ax.set_box_aspect([np.ptp(a) for a in [ax.get_xlim(), ax.get_ylim(), ax.get_zlim()]]) 

plt.savefig('3d_point_plane_perpendicular.png')