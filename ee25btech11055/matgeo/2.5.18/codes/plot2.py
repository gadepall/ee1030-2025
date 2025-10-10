import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = np.array([1, 2, -3]).T
b = np.array([3, -1, 2]).T

# Solving
c = a + b
d = a - b
result = (c.T) @ d
if result == 0:
    print("a+b and a-b are perpendicular")
else:
    print("a+b and a-b are not perpendicular")
# Plotting

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")

ax.quiver(0, 0, 0, c[0], c[1], c[2], color="red", label="a+b")
ax.quiver(0, 0, 0, d[0], d[1], d[2], color="blue", label="a-b")

ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("2.5.18")
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])
ax.legend()
ax.grid(True)

plt.savefig("../figs/python.png")
plt.show()
