import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Plane: 2x - 2y + 4z + 5 = 0
# Point: p(1, 3/2, 2)
p = np.array([1.0, 1.5, 2.0])
n = np.array([2.0, -2.0, 4.0])

# Foot of perpendicular (xo)
lam = - (np.dot(n, p) + 5) / np.dot(n, n)
xo = p + lam * n

# Distance (perpendicular length)
distance = abs(np.dot(n, p) + 5) / LA.norm(n)

# Create mesh for plane
x_vals = np.linspace(-2, 2, 40)
y_vals = np.linspace(0, 3.5, 40)
xx, yy = np.meshgrid(x_vals, y_vals)
zz = (-2*xx + 2*yy - 5)/4

# Plotting
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection='3d')

# Plane
ax.plot_surface(xx, yy, zz, alpha=0.5, color='lightblue')

# Scatter points
ax.scatter(*p, color='red', s=80, label='p(1, 3/2, 2)')
ax.scatter(*xo, color='blue', s=80, label=f'xo(0, 2.5, 0)')

# Perpendicular line pxo
ax.plot([p[0], xo[0]], [p[1], xo[1]], [p[2], xo[2]], 
        color='black', linestyle='--', linewidth=2, label='pxo ⟂ plane')

# ---- Draw right-angle square marker at xo ----
eps = 0.15  # size of the square
# Two perpendicular directions in the plane
u = np.cross(n, [1,0,0])
if LA.norm(u) == 0:
    u = np.cross(n, [0,1,0])
u = u / LA.norm(u)
v = np.cross(n, u)
v = v / LA.norm(v)

# Tiny square centered at xo
square_pts = [xo, xo + eps*u, xo + eps*u + eps*v, xo + eps*v, xo]
ax.plot([pt[0] for pt in square_pts], 
        [pt[1] for pt in square_pts], 
        [pt[2] for pt in square_pts], color="k")

# Annotations
ax.text(p[0]+0.05, p[1]+0.05, p[2]+0.05, "p(1, 3/2, 2)", color='red')
ax.text(xo[0]+0.05, xo[1]-0.15, xo[2]+0.05, "xo(0, 2.5, 0)", color='blue')

# Labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title(f'Perpendicular from p to plane (Length = {distance:.4f})')
ax.legend()

plt.show()