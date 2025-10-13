import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Line: r = (-1, -2, -3) + λ(3, 4, 3)
P0 = np.array([-1, -2, -3])   # point on line
d = np.array([3, 4, 3])       # direction vector

# Plane: x + y + 3z = -4
n = np.array([1, 1, 3])       # normal vector
c = -4

# Solve for intersection: n · (P0 + λd) + 4 = 0
# => λ = -(n·P0 + 4)/(n·d)
lam = -(np.dot(n, P0) + 4) / np.dot(n, d)
P_inter = P0 + lam * d

print("Intersection point:", P_inter)

# Create 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot line
lams = np.linspace(-2, 2, 100)
line_points = P0[:, None] + d[:, None] * lams
ax.plot(line_points[0], line_points[1], line_points[2], 'b-', label="Line")

# Plot plane
xx, yy = np.meshgrid(np.linspace(-5, 5, 10), np.linspace(-5, 5, 10))
zz = (-c - xx - yy) / 3
ax.plot_surface(xx, yy, zz, alpha=0.5, color='orange')

# Plot intersection point
ax.scatter(*P_inter, color='red', s=50, label="Intersection point")

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()

plt.title("Intersection of Line and Plane")
plt.show()
