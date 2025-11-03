import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D   # registers 3D projection
from matplotlib.patches import Patch

# Plane coefficients: a*x + b*y + c*z = d
planes = [
    (3, -2,  3, 8,  "3x - 2y + 3z = 8"),
    (2,  1, -1, 1,  "2x +  y -  z = 1"),
    (4, -3,  2, 4,  "4x - 3y + 2z = 4")
]
colors = ["tab:blue", "tab:orange", "tab:green"]

# Solve linear system to find intersection point (if unique)
A = np.array([[p[0], p[1], p[2]] for p in planes], dtype=float)
b = np.array([p[3] for p in planes], dtype=float)

intersection = None
try:
    intersection = np.linalg.solve(A, b)   # [x0, y0, z0]
    has_unique = True
except np.linalg.LinAlgError:
    has_unique = False

# Build a grid in x-y around the intersection (or default range)
if has_unique:
    x0, y0, z0 = intersection
    rng = 3.0
    x_min, x_max = x0 - rng, x0 + rng
    y_min, y_max = y0 - rng, y0 + rng
else:
    x_min, x_max = -5, 5
    y_min, y_max = -5, 5

xx, yy = np.meshgrid(np.linspace(x_min, x_max, 40),
                     np.linspace(y_min, y_max, 40))

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot each plane
patches = []
for (a, b_coef, c, d, label), col in zip(planes, colors):
    # compute z = (d - a*x - b*y)/c  (works since c != 0 for these planes)
    zz = (d - a * xx - b_coef * yy) / c
    surf = ax.plot_surface(xx, yy, zz, alpha=0.5, rstride=1, cstride=1, linewidth=0, antialiased=True)
    patches.append(Patch(facecolor=col, label=label))
    # Color the surface by setting the facecolors (plot_surface doesn't accept label directly)
    surf.set_facecolor(col)
    surf.set_edgecolor((0,0,0,0))  # hide edges for smooth look

# Plot intersection point if exists
if has_unique:
    ax.scatter([x0], [y0], [z0], color="red", s=60, label="Intersection point")
    ax.text(x0, y0, z0, f"  ({x0:.2f}, {y0:.2f}, {z0:.2f})", color="red")

# Labels, limits and legend
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

# Create legend: include plane labels and intersection point if present
legend_handles = [Patch(facecolor=colors[i], label=planes[i][4]) for i in range(len(planes))]
if has_unique:
    legend_handles.append(plt.Line2D([0], [0], marker='o', color='w',
                                     markerfacecolor='red', markersize=8, label='Intersection point'))
ax.legend(handles=legend_handles, loc='upper left', bbox_to_anchor=(1.05, 1))

ax.set_title("3 Planes: 3x-2y+3z=8, 2x+y-z=1, 4x-3y+2z=4")
plt.tight_layout()
plt.show()