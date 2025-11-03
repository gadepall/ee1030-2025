import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = np.array([2, -1, 2]).T
b = np.array([5, 3, 4]).T
p = np.array([2, 0, 3]).T
q = np.array([1, 1, 5]).T
r = np.array([3, 2, 4]).T

h = a
m = b - a
k = 10
l1 = h - k * m
l2 = h + k * m

A = np.array([p, q, r])
c = np.array([1, 1, 1]).T
n = LA.solve(A, c)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")

ax.plot([l1[0], l2[0]], [l1[1], l2[1]], [l1[2], l2[2]], color="blue")

ax.scatter(b[0], b[1], b[2], color="green", label="B")
ax.scatter(a[0], a[1], a[2], color="red", label="A")

ax.text(a[0], a[1], a[2], "A")
ax.text(b[0], b[1], b[2], "B")

x, y = np.meshgrid(range(-10, 10), range(-10, 10))
z = -(n[0] * x + n[1] * y - 1) / n[2]

ax.plot_surface(x, y, z, alpha=0.7, color="gray")

ax.scatter(13 / 5, -1 / 5, 12 / 5, color="yellow", label="Point")
ax.text(13 / 5, -1 / 5, 12 / 5, "Point")

ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("4.11.32")
ax.set_xlim([-20, 20])
ax.set_ylim([-20, 20])
ax.set_zlim([-20, 20])
ax.legend()
ax.grid(True)

plt.savefig("../figs/python.png")
plt.show()
