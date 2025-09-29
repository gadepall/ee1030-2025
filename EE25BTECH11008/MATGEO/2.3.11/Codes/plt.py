import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Vectors
u = np.array([1, -2, -2])
v = np.array([3, -6,  2])
origin = np.zeros(3)

# 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot vector u
ax.quiver(*origin, *u, color='r', arrow_length_ratio=0.1)
ax.text(u[0]*1.1, u[1]*1.1, u[2]*1.1, "u", color='r')

# Plot vector v
ax.quiver(*origin, *v, color='b', arrow_length_ratio=0.1)
ax.text(v[0]*1.1, v[1]*1.1, v[2]*1.1, "v", color='b')

# Set axes dynamically
all_points = np.vstack([origin, u, v])
ax.set_xlim([all_points[:,0].min()-1, all_points[:,0].max()+1])
ax.set_ylim([all_points[:,1].min()-1, all_points[:,1].max()+1])
ax.set_zlim([all_points[:,2].min()-1, all_points[:,2].max()+1])

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Normal vectors U and V in 3D plot")

plt.show()
