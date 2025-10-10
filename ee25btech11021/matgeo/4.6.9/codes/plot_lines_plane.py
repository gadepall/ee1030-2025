import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from plane_solver import P1, d1, P2, d2, P3, d3, n, d_plane  # reuse computed values

points = [P1, P2, P3]
directions = [d1, d2, d3]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot lines
t = np.linspace(-1, 2, 50)
for i, (P, d) in enumerate(zip(points, directions)):
    X = P[0] + d[0]*t
    Y = P[1] + d[1]*t
    Z = P[2] + d[2]*t
    ax.plot(X, Y, Z, label=f'Line {i+1}')
    ax.scatter(P[0], P[1], P[2], s=50)
    ax.text(P[0], P[1], P[2], f'P{i+1}({P[0]},{P[1]},{P[2]})')

# Plot plane
xx, yy = np.meshgrid(np.linspace(-1,3,10), np.linspace(-1,3,10))
zz = (d_plane - n[0]*xx - n[1]*yy)/n[2]
ax.plot_surface(xx, yy, zz, alpha=0.3, color='cyan')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.savefig("lines_and_plane.png", dpi=300, bbox_inches='tight')
plt.show()
