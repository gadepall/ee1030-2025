import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

def get_point_on_line(point, direction, t):
    return np.array(point) + t * np.array(direction)

A = np.array([1, 2, 3])
d = np.array([1, 2, -5])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the plane first (behind the line)
xx, yy = np.meshgrid(np.linspace(-3, 5, 15), np.linspace(-2, 6, 15))
zz = (xx + 2*yy + 9) / 5
ax.plot_surface(xx, yy, zz, alpha=0.4, color='yellow', edgecolor='none')

# Plot the line with more contrast
t_values = np.linspace(-1.5, 1.5, 100)
line_points = np.array([get_point_on_line(A, d, t) for t in t_values])

ax.plot(line_points[:, 0], line_points[:, 1], line_points[:, 2], 
        'b-', linewidth=2, label='Line', zorder=10)

# Mark point A clearly
ax.scatter([A[0]], [A[1]], [A[2]], color='red', s=80, 
          edgecolor='black', linewidth=1, label='Point A', zorder=15)

# Add text label for point A with coordinates
ax.text(A[0]+0.2, A[1]+0.2, A[2]+0.2, f'A({A[0]},{A[1]},{A[2]})', fontsize=10)

# Direction vector arrow
ax.quiver(A[0], A[1], A[2], d[0]*0.3, d[1]*0.3, d[2]*0.3,
          color='red', arrow_length_ratio=0.2, linewidth=3, 
          label='Direction Vector', zorder=12)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Line Perpendicular to Plane')
ax.legend()
ax.grid(True)
plt.show()