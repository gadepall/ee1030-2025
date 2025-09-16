import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

point_A = np.array([5.0, 2.0, -4.0])
normal_n = np.array([2.0, 3.0, -1.0])

d = np.dot(normal_n, point_A)
plane_eq_str = f"{normal_n[0]:.0f}x + {normal_n[1]:.0f}y + {normal_n[2]:.0f}z = {d:.0f}"
print(f"Plane equation: {plane_eq_str}")

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

x_range = np.linspace(point_A[0] - 5, point_A[0] + 5, 20)
y_range = np.linspace(point_A[1] - 5, point_A[1] + 5, 20)
x_grid, y_grid = np.meshgrid(x_range, y_range)

z_plane = (d - normal_n[0] * x_grid - normal_n[1] * y_grid) / normal_n[2]

ax.plot_surface(x_grid, y_grid, z_plane, alpha=0.6, cmap='plasma', edgecolor='none')

ax.scatter([point_A[0]], [point_A[1]], [point_A[2]], color='red', s=100, label=f'Point A {tuple(point_A)}')

ax.quiver(
    point_A[0], point_A[1], point_A[2],
    normal_n[0], normal_n[1], normal_n[2],
    length=4, normalize=True, color='black', arrow_length_ratio=0.2,
    label=f'Normal Vector n={tuple(normal_n)}'
)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title(f'Plane Visualization: {plane_eq_str}', fontsize=14)
ax.legend()
plt.grid(True)
plt.show()


