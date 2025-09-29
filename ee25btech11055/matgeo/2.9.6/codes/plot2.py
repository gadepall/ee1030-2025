import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = np.array([8, 0, 0]).T
b = np.array([(27**0.5) / 2, 1.5, 0]).T

# Solving
c = np.cross(a,b)
# Plotting

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")

ax.quiver(0, 0, 0, a[0], a[1], a[2], color="red", label="a")
ax.quiver(0, 0, 0, b[0], b[1], b[2], color="blue", label="b")
ax.quiver(0, 0, 0, c[0], c[1], c[2], color="green", label="axb")

ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("2.9.6")
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])
ax.legend()
ax.grid(True)

plt.savefig("../figs/python.png")
plt.show()
