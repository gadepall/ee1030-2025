import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given vectors (treated as position vectors from the origin)
a = np.array([1, -2, 3])
b = np.array([2, 3, -4])
c = np.array([1, -3, 5])

# Compute plane normal using two direction vectors from point a
v1 = b - a
v2 = c - a
normal = np.cross(v1, v2)

# Plane equation: normal . (x - a) = 0 --> solve for z when possible
def plane_z(X, Y, point, normal):
    nx, ny, nz = normal
    x0, y0, z0 = point
    if abs(nz) < 1e-8:
        return np.full_like(X, np.nan)
    return ((-nx*(X - x0) - ny*(Y - y0)) / nz) + z0

# Build a grid that comfortably contains the three points
all_pts = np.vstack([a, b, c])
mins = all_pts.min(axis=0) - 1
maxs = all_pts.max(axis=0) + 1

x = np.linspace(mins[0], maxs[0], 20)
y = np.linspace(mins[1], maxs[1], 20)
X, Y = np.meshgrid(x, y)
Z = plane_z(X, Y, a, normal)

# Create the plot
fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the plane surface (alpha for transparency)
ax.plot_surface(X, Y, Z, alpha=0.35, rstride=1, cstride=1)

# Plot vectors as arrows from origin
origin = np.zeros(3)
ax.quiver(origin[0], origin[1], origin[2], a[0], a[1], a[2], linewidth=2)
ax.quiver(origin[0], origin[1], origin[2], b[0], b[1], b[2], linewidth=2)
ax.quiver(origin[0], origin[1], origin[2], c[0], c[1], c[2], linewidth=2)

# Mark endpoints and annotate
ax.scatter(all_pts[:,0], all_pts[:,1], all_pts[:,2], s=40)
for vec, name in zip([a,b,c], ['a','b','c']):
    ax.text(vec[0], vec[1], vec[2], f'  {name}{tuple(vec)}', fontsize=10)

# Axes labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Vectors and the Plane through them (coplanar)')

# Make axes aspect equal
max_range = np.array([all_pts[:,0].max()-all_pts[:,0].min(),
                      all_pts[:,1].max()-all_pts[:,1].min(),
                      all_pts[:,2].max()-all_pts[:,2].min()]).max() / 2.0

mid_x = (all_pts[:,0].max()+all_pts[:,0].min()) * 0.5
mid_y = (all_pts[:,1].max()+all_pts[:,1].min()) * 0.5
mid_z = (all_pts[:,2].max()+all_pts[:,2].min()) * 0.5
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

plt.show()
