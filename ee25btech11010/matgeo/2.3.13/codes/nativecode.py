import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Vectors
v = np.array([1, -1, 2])
e2 = np.array([0, 1, 0])

# Normalize for plotting
v_unit = v / np.linalg.norm(v)
e2_unit = e2 / np.linalg.norm(e2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

origin = np.array([0, 0, 0])

# Plot vectors
ax.quiver(*origin, *v_unit, color='r')
ax.quiver(*origin, *e2_unit, color='b')

# Add labels next to the tips
ax.text(*v_unit, "Line (1,-1,2)", color='r', fontsize=10)
ax.text(*e2_unit, "Y-axis (0,1,0)", color='b', fontsize=10)

# Axes labels and limits
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([0, 2])
ax.grid(True)

plt.savefig("/home/arsh-dhoke/ee1030-2025/ee25btech11010/matgeo/2.3.13/figs/q3.png")

plt.show()
