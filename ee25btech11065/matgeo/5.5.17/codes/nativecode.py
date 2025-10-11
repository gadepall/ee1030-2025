import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x_vals = np.linspace(-10, 10, 50)
y_vals = np.linspace(-10, 10, 50)
x, y = np.meshgrid(x_vals, y_vals)

z1 = 6 - x - y
z2 = (11 - y) / 3
z3 = 2*y - x

A = np.array([
    [1, 1, 1],
    [0, 1, 3],
    [1, -2, 1]
])
b = np.array([6, 11, 0])

intersection_point = np.linalg.solve(A, b)
px, py, pz = intersection_point

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, z1, alpha=0.5, color='red', label='Plane 1')
ax.plot_surface(x, y, z2, alpha=0.5, color='green', label='Plane 2')
ax.plot_surface(x, y, z3, alpha=0.5, color='blue', label='Plane 3')

ax.scatter(px, py, pz, color='black', s=100, label='Intersection Point')
ax.text(px, py, pz + 1, f"({px:.2f}, {py:.2f}, {pz:.2f})", color='black')

ax.text(6, -9, 8, "x + y + z = 6", color='red')
ax.text(-10, 9, (11 - 9)/3, "y + 3z = 11", color='green')
ax.text(-9, -9, 2*(-9) - (-9), "x - 2y + z = 0", color='blue')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)

ax.set_xticks(np.linspace(-10, 10, 5))
ax.set_yticks(np.linspace(-10, 10, 5))
ax.set_zticks(np.linspace(-10, 10, 5))

ax.grid(True)
ax.set_title('Intersection of Three Planes')
ax.legend()

plt.show()

