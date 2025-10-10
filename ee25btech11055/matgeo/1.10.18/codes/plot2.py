import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

vec = np.array([1, 1, -1]).reshape(-1, 1)

# Solving
print(f"Direction ratios are {vec[0]}, {vec[1]}, {vec[2]}")
unit = vec / LA.norm(vec)
print(f"Direction cosines are {unit[0]}, {unit[1]}, {unit[2]}")

# Plotting

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")

x, y, z = vec
ax.scatter(x, y, z, color="red", s=50, label="Given Point")
ax.quiver(
    0, 0, 0, x, y, z, color="blue", arrow_length_ratio=0.1, label="Position Vector"
)
x, y, z = unit
ax.quiver(0, 0, 0, x, y, z, color="green", arrow_length_ratio=0.1, label="Unit Vector")

ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("1.10.18")
ax.legend()
ax.grid(True)

plt.savefig("../figs/python.png")
plt.show()
