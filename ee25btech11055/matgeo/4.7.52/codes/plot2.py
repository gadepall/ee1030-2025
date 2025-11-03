import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

n = np.array([3, 4, -12]).T
d = -13
a = np.array([-3, 0, 1]).T
b = np.array([1, 1, 1]).T
c = np.array([1, 1, 7 / 3]).T

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")


x, y = np.meshgrid(range(10), range(10))
z = -(n[0] * x + n[1] * y - d) / n[2]

ax.plot_surface(x, y, z, alpha=0.7, color="gray")

ax.scatter(a[0], a[1], a[2], color="red", label="a")
ax.scatter(b[0], b[1], b[2], color="blue", label="b")
ax.scatter(c[0], c[1], c[2], color="green", label="c")

ax.text(a[0], a[1], a[2], "Given Point")
ax.text(b[0], b[1], b[2], "Point 1")
ax.text(c[0], c[1], c[2], "Point 2")

ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("4.7.52")
ax.set_xlim([-5, 10])
ax.set_ylim([-5, 10])
ax.set_zlim([-5, 10])
ax.legend()
ax.grid(True)

plt.savefig("../figs/python.png")
plt.show()
