import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given points
A = np.array([2, 5, -3])
B = np.array([-2, -3, 5])
C = np.array([5, 3, -3])
P = np.array([3, 1, 5])
Q = np.array([-1, -3, -1])

# Normal vector of the plane = (B-A) x (C-A)
AB = B - A
AC = C - A
n = np.cross(AB, AC)
d = -np.dot(n, A)

# Plane equation: n·X + d = 0
xx, yy = np.meshgrid(range(-5, 6), range(-5, 6))
zz = (-n[0]*xx - n[1]*yy - d) / n[2]

# Line parametric equation
t = np.linspace(-2, 2, 100)
line_x = P[0] + (Q[0]-P[0])*t
line_y = P[1] + (Q[1]-P[1])*t
line_z = P[2] + (Q[2]-P[2])*t

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plane
ax.plot_surface(xx, yy, zz, alpha=0.5, color='cyan')

# Line
ax.plot(line_x, line_y, line_z, 'r', label="Line")

# Mark given points
ax.scatter(*A, color='blue', s=50, label="Plane Point A")
ax.scatter(*B, color='green', s=50, label="Plane Point B")
ax.scatter(*C, color='orange', s=50, label="Plane Point C")
ax.scatter(*P, color='purple', s=50, label="Line Point P")
ax.scatter(*Q, color='brown', s=50, label="Line Point Q")

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
plt.savefig('2.png')
plt.show()