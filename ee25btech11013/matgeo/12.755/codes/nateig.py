import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

d = np.linspace(-2, 2, 40)
Y, Z = np.meshgrid(d, d)  # create grid

# Plane 1: x - 2y = 0 → X = 2Y, Z free
X1 = 2 * Y
Z1 = Z
ax.plot_surface(X1, Y, Z1, alpha=0.5, color='g')

# Plane 2: y = 0 → Y=0, X and Z free
X2, Z2 = np.meshgrid(d, d)
Y2 = np.zeros_like(X2)
ax.plot_surface(X2, Y2, Z2, alpha=0.5, color='r')

# Intersection line: x=0, y=0, z free
z_line = np.linspace(-2, 2, 20)
x_line = np.zeros_like(z_line)
y_line = np.zeros_like(z_line)
ax.plot3D(x_line, y_line, z_line, color='k', linewidth=3)

# Intersection point at origin
ax.scatter(0, 0, 0, color='black', s=80)

# Legend
legend_elements = [
    Line2D([0],[0], color='g', lw=4, alpha=0.5, label='x - 2y = 0'),
    Line2D([0],[0], color='r', lw=4, alpha=0.5, label='y = 0'),
    Line2D([0],[0], color='k', lw=3, label='Intersection Line (x=0, y=0)'),
    Line2D([0],[0], marker='o', color='k', label='Origin (0,0,0)', markersize=8, linestyle='')
]
ax.legend(handles=legend_elements)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Intersection of Planes: x - 2y = 0 and y = 0')
ax.view_init(elev=25, azim=-60)
plt.savefig("/mnt/c/Users/bharg/Documents/backupmatrix/ee25btech11013/matgeo/12.755/figs/Figure_1.png")

plt.show()

