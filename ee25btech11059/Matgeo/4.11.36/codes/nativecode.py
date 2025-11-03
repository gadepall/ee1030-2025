import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given points
A = np.array([3, -4, -5])
B = np.array([2, -3, 1])
P = np.array([1, 2, 3])
Q = np.array([4, 2, -3])
R = np.array([0, 4, 3])

# Direction vector of line AB
AB = B - A

# Normal vector to plane PQR = (Q-P) x (R-P)
n = np.cross(Q-P, R-P)

# Solve for intersection: A + t*AB lies in plane
t = np.dot(n, P-A) / np.dot(n, AB)
C = A + t*AB  # intersection point

# Generate grid for plane PQR
u = np.linspace(-2, 2, 10)
v = np.linspace(-2, 2, 10)
U, V = np.meshgrid(u, v)
plane_points = P.reshape(3,1,1) + (Q-P).reshape(3,1,1)*U + (R-P).reshape(3,1,1)*V

# Create plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Extended line AB
t_vals = np.linspace(-10, 10, 200)
line_points = A.reshape(3,1) + np.outer(AB, t_vals)
ax.plot(line_points[0], line_points[1], line_points[2], 'b--', label="Line AB")

# Plot plane
ax.plot_surface(plane_points[0], plane_points[1], plane_points[2], alpha=0.4, color='orange')

# Plot points
ax.scatter(*A, color='red', s=60)
ax.text(*A, "A", fontsize=12)

ax.scatter(*B, color='blue', s=60)
ax.text(*B, "B", fontsize=12)

ax.scatter(*P, color='green', s=60)
ax.text(*P, "P", fontsize=12)

ax.scatter(*Q, color='purple', s=60)
ax.text(*Q, "Q", fontsize=12)

ax.scatter(*R, color='brown', s=60)
ax.text(*R, "R", fontsize=12)

ax.scatter(*C, color='black', s=100, marker='X')
ax.text(*C, "C", fontsize=14, color='black', weight='bold')

# Labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Line AB intersecting Plane PQR at C")

plt.legend()
plt.savefig("graph8.png", dpi=300)
plt.show()

print("Intersection Point C =", C)


