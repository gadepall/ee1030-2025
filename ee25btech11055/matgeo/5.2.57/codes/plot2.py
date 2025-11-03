import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

e1 = np.array([2, 1, 1, 1])
e2 = np.array([1, -2, -1, 3 / 2])
e3 = np.array([0, 3, -5, 9])

cols = ["", "red", "blue", "green"]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")

x, y = np.meshgrid(range(-10, 10), range(-10, 10))

for i in range(1, 4):
    z = (
        -(eval(f"e{i}")[0] * x + eval(f"e{i}")[1] * y - eval(f"e{i}")[3])
        / eval(f"e{i}")[2]
    )
    ax.plot_surface(x, y, z, alpha=0.35, color=cols[i])

ax.scatter(1, 1 / 2, -3 / 2, color="yellow", label="Point")
ax.text(1, 1 / 2, -3 / 2, " Point")

ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("5.2.57")
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])
ax.legend()
ax.grid(True)

plt.savefig("../figs/python.png")
plt.show()
