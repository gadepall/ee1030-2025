import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given points
A = np.array([2, 5, -3])
B = np.array([-2, -3, 5])
C = np.array([5, 3, -3])
P = np.array([3, 1, 5])
Q = np.array([-1, -3, -1])

# Step 1: Normal to the plane (AB x AC)
AB = B - A
AC = C - A
n = np.cross(AB, AC)

# Plane equation: n . (x - A) = 0
d = -np.dot(n, A)  # plane constant
print("Plane equation: {}x + {}y + {}z + {} = 0".format(n[0], n[1], n[2], d))

# Step 2: Line parametric equation
d_line = Q - P   # direction vector
t = np.linspace(-5, 5, 100)
line_points = P[:, None] + d_line[:, None] * t  # shape (3, len(t))

# Step 3: Find intersection of line with plane
# Solve n.(P + t*d_line) + d = 0
t_inter = -(np.dot(n, P) + d) / np.dot(n, d_line)
intersection = P + t_inter * d_line
print("Intersection point:", intersection)

# Step 4: Plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot plane
xx, yy = np.meshgrid(range(-5, 8), range(-5, 8))
zz = (-n[0]*xx - n[1]*yy - d) / n[2]
ax.plot_surface(xx, yy, zz, alpha=0.5, color='cyan')

# Plot line
ax.plot(line_points[0], line_points[1], line_points[2], color='red', label="Line")

# Plot intersection
ax.scatter(*intersection, color='black', s=60, label="Intersection")

# Plot given points
ax.scatter(*A, color='blue', s=50, label='A')
ax.scatter(*B, color='green', s=50, label='B')
ax.scatter(*C, color='purple', s=50, label='C')
ax.scatter(*P, color='orange', s=50, label='P')
ax.scatter(*Q, color='brown', s=50, label='Q')

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
ax.set_title("Plane, Line, and Intersection")
plt.savefig("\sdcard\4.4.12.png")
plt.show()
