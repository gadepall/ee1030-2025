import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

p1 = np.array([0,0,0])
p2 = np.array([1,0,0])
p3 = np.array([1,0,1])
p4 = np.array([0,0,1])
p5 = np.array([0,1,0])
p6 = np.array([1,1,0])
p7 = np.array([1,1,1])
p8 = np.array([0,1,1])

fig = plt.figure(figsize = (10,10))
ax = fig.add_subplot(111, projection = '3d')

# Bottom face
ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], 'k--')
ax.plot([p2[0], p3[0]], [p2[1], p3[1]], [p2[2], p3[2]], 'k--')
ax.plot([p3[0], p4[0]], [p3[1], p4[1]], [p3[2], p4[2]], 'k--')
ax.plot([p4[0], p1[0]], [p4[1], p1[1]], [p4[2], p1[2]], 'k--')

# Top face
ax.plot([p5[0], p6[0]], [p5[1], p6[1]], [p5[2], p6[2]], 'k--')
ax.plot([p6[0], p7[0]], [p6[1], p7[1]], [p6[2], p7[2]], 'k--')
ax.plot([p7[0], p8[0]], [p7[1], p8[1]], [p7[2], p8[2]], 'k--')
ax.plot([p8[0], p5[0]], [p8[1], p5[1]], [p8[2], p5[2]], 'k--')

# Vertical edges
ax.plot([p1[0], p5[0]], [p1[1], p5[1]], [p1[2], p5[2]], 'k--')
ax.plot([p2[0], p6[0]], [p2[1], p6[1]], [p2[2], p6[2]], 'k--')
ax.plot([p3[0], p7[0]], [p3[1], p7[1]], [p3[2], p7[2]], 'k--')
ax.plot([p4[0], p8[0]], [p4[1], p8[1]], [p4[2], p8[2]], 'k--')

# Body diagonal from p1 to p7
ax.plot([p1[0], p7[0]], [p1[1], p7[1]], [p1[2], p7[2]], 'b', label = r"d1 makes angle $\alpha$ with Line L")

# Body diagonal from p2 to p8
ax.plot([p2[0], p8[0]], [p2[1], p8[1]], [p2[2], p8[2]], 'g', label = r"d2 makes angle $\beta$ with Line L")

# Body diagonal from p3 to p5
ax.plot([p3[0], p5[0]], [p3[1], p5[1]], [p3[2], p5[2]], 'm', label = r"d3 makes angle $\gamma$ with Line L")

# Body diagonal from p4 to p6
ax.plot([p4[0], p6[0]], [p4[1], p6[1]], [p4[2], p6[2]], 'y', label = r"d4 makes angle $\delta$ with Line L")

# Center of the cube
center = np.array([0.5, 0.5, 0.5])

# Direction vector of the line
v = np.array([2, 1, 3])

# Parameter for length of the line
k = 0.5

# Two points on the line
start = center - k * v
end = center + k * v

# Plot the line
ax.plot([start[0], end[0]], [start[1], end[1]], [start[2], end[2]], 'r', label = 'Line L')


ax.set_xlabel("X - AXIS")
ax.set_ylabel("Y - AXIS")
ax.set_zlabel("Z - AXIS")
ax.set_title("2.8.5")

ax.legend()
ax.set_box_aspect([1, 1, 1])
ax.view_init(elev=10, azim=135)
plt.savefig("fig4.png", dpi=300)
plt.show()
