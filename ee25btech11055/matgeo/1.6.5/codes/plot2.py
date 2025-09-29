import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

points = np.array([[-1, -2, 1], [2, 3, 4], [5, 8, 7]])

x_coords = points[:, 0]
y_coords = points[:, 1]
z_coords = points[:, 2]

# Solving
coll = np.array([points[1] - points[0], points[2] - points[0]]).T
rank = LA.matrix_ran(coll)
if rank == 1:
    print("The given points are collinear")

# Plotting
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

ax.scatter(x_coords, y_coords, z_coords, color="red", s=50, label="Given Points")
ax.plot(x_coords, y_coords, z_coords, color="blue", label="Line Segment")


ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("1.6.5")
ax.legend()
ax.grid(True)

# plt.savefig("../figs/python.png")
plt.show()
