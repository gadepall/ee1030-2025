import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Plane coefficients (Ax + By + Cz + D = 0)

# Plane p1: 1x + 2y + 3z - 4 = 0
A1, B1, C1, D1 = 1, 2, 3, -4

# Plane p2: 2x + 1y -1z + 5 = 0
A2, B2, C2, D2 = 2, 1, -1, 5

# Plane p3: 5x + 3y -6z + 8 = 0
A3, B3, C3, D3 = 5, 3, -6, 8

# Computed Plane p: 33x + 45y + 50z - 41 = 0
Ap, Bp, Cp, Dp = 33, 45, 50, -41

# Set up 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Generate grid
grid_range = np.linspace(-10, 10, 50)
xx, yy = np.meshgrid(grid_range, grid_range)

def plot_plane(A, B, C, D, color):
    if C != 0:
        zz = -(A * xx + B * yy + D) / C
        ax.plot_surface(xx, yy, zz, alpha=0.5, rstride=1, cstride=1, color=color, edgecolor='none')

# Plot planes
plot_plane(A1, B1, C1, D1, 'lightcoral')   # p1
plot_plane(A2, B2, C2, D2, 'lightgreen')  # p2
plot_plane(A3, B3, C3, D3, 'lightblue')   # p3
plot_plane(Ap, Bp, Cp, Dp, 'cyan')        # p

# Custom legend
legend_elements = [
    Patch(facecolor='lightcoral', label='p1: 1x + 2y + 3z - 4 = 0'),
    Patch(facecolor='lightgreen', label='p2: 2x + 1y -1z + 5 = 0'),
    Patch(facecolor='lightblue', label='p3: 5x + 3y -6z + 8 = 0'),
    Patch(facecolor='cyan', label='p: 33x + 45y + 50z -41 = 0')
]
ax.legend(handles=legend_elements, loc='upper right')

# Axis labels and limits
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)

ax.set_title('Direct 3D Plot of Planes p1, p2, p3, and p')

# Save figure as 1.png
plt.savefig('2.png', dpi=300, bbox_inches='tight')
plt.show()
