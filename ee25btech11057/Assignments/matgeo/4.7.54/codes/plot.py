import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given lines direction vectors
d1 = np.array([3, -16, 7])
d2 = np.array([3, 8, -5])
p1 = np.array([8, -19, 10])   # point on line 1
p2 = np.array([15, 29, 5])    # point on line 2

# New line
p0 = np.array([1, 2, -4])
d = np.array([2, 3, 6])

# Parameter ranges
t = np.linspace(-5, 5, 100)

# Line equations
line1 = p1[:, None] + d1[:, None]*t
line2 = p2[:, None] + d2[:, None]*t
line3 = p0[:, None] + d[:, None]*t

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(line1[0], line1[1], line1[2], color='r')
ax.plot(line2[0], line2[1], line2[2], color='g')
ax.plot(line3[0], line3[1], line3[2], color='b')

# Mark the point (1,2,-4)
ax.scatter(p0[0], p0[1], p0[2], color='k', s=50)
ax.text(p0[0], p0[1], p0[2]-4, "(1,2,-4)", color='k', fontsize=8)  # below the point

# Labels beside the lines
# Red line label -> shifted outward in x, but moved a bit downward
ax.text(line1[0][-1]+2, line1[1][-1]-2, line1[2][-1],
        "(x-8)/3 = (y+19)/-16 = (z-10)/7", color='r', fontsize=7)

# Green line label -> shifted upward compared to last version
mid_idx = len(t)//2
ax.text(line2[0][mid_idx], line2[1][mid_idx]-3, line2[2][mid_idx],
        "(x-15)/3 = (y-29)/8 = (z-5)/-5", color='g', fontsize=8)

# Blue line label
ax.text(line3[0][-1]+1, line3[1][-1], line3[2][-1],
        "(1,2,-4)+k(2,3,6)", color='b', fontsize=8)

# Formatting
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Lines in 3D")

plt.savefig("../figs/fig7.png")
plt.show()

