

import sys
sys.path.insert(0, '/sdcard/github/matgeo/codes/CoordGeo')  # Your custom path

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Local imports (keeping as requested)
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

# Plane coefficients: a = b = c = 1, distance from origin = 3 * sqrt(3)
a, b, c = 1, 1, 1
d1 = -9   # Plane 1: x + y + z = 9  (rewrite as x + y + z - 9 = 0)
d2 = 9    # Plane 2: x + y + z = -9 (rewrite as x + y + z + 9 = 0)

# Create grid for x and y
x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)
X, Y = np.meshgrid(x, y)

# Calculate corresponding z for both planes
Z1 = (-a * X - b * Y - d1) / c
Z2 = (-a * X - b * Y - d2) / c

# Create figure and 3D axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot both planes with transparency and different colors
ax.plot_surface(X, Y, Z1, alpha=0.5, color='cyan', rstride=1, cstride=1, edgecolor='none', label='Plane 1: x+y+z=9')
ax.plot_surface(X, Y, Z2, alpha=0.5, color='orange', rstride=1, cstride=1, edgecolor='none', label='Plane 2: x+y+z=-9')

# Mark the origin
ax.scatter(0, 0, 0, color='red', s=80, label='Origin (0,0,0)')

# Normal vector (same for both planes)
normal_vec = np.array([a, b, c])
origin = np.array([0, 0, 0])
ax.quiver(*origin, *normal_vec, length=7, color='black', linewidth=2, label='Normal Vector (1,1,1)')

# Annotate the intercepts of Plane 1 (where x=0,y=0 -> z=9 etc)
intercepts_p1 = np.array([[9, 0, 0], [0, 9, 0], [0, 0, 9]])
for i, point in enumerate(intercepts_p1):
    ax.scatter(*point, color='blue', s=60)
    ax.text(*point, f'P{i+1}\n({point[0]}, {point[1]}, {point[2]})', color='blue', fontsize=10, ha='left')

# Annotate the intercepts of Plane 2
intercepts_p2 = np.array([[-9, 0, 0], [0, -9, 0], [0, 0, -9]])
for i, point in enumerate(intercepts_p2):
    ax.scatter(*point, color='darkorange', s=60)
    ax.text(*point, f'Q{i+1}\n({point[0]}, {point[1]}, {point[2]})', color='darkorange', fontsize=10, ha='right')

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Planes $x + y + z = 9$ and $x + y + z = -9$ with normal vector\nDistance from origin = $3\\sqrt{3}$')

# Set limits and equal aspect ratio for better view
ax.set_xlim(-12, 12)
ax.set_ylim(-12, 12)
ax.set_zlim(-12, 12)
ax.set_box_aspect([1, 1, 1])

# Add legend manually because plot_surface does not support label param well
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color='cyan', lw=8, label='Plane 1: x + y + z = 9'),
    Line2D([0], [0], color='orange', lw=8, label='Plane 2: x + y + z = -9'),
    Line2D([0], [0], marker='o', color='w', label='Origin', markerfacecolor='red', markersize=10),
    Line2D([0], [0], color='black', lw=2, label='Normal Vector (1,1,1)'),
    Line2D([0], [0], marker='o', color='w', label='Plane 1 intercepts', markerfacecolor='blue', markersize=8),
    Line2D([0], [0], marker='o', color='w', label='Plane 2 intercepts', markerfacecolor='darkorange', markersize=8),
]
ax.legend(handles=legend_elements, loc='upper left')

plt.grid(True)
plt.show()

