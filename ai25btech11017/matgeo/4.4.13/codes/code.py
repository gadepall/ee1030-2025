import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Point and direction vector
P = np.array([2, -1, 4])
d = np.array([1, 1, -2])

# Parameter range for t
t = np.linspace(-5, 5, 100)

# Line points
x = P[0] + d[0]*t
y = P[1] + d[1]*t
z = P[2] + d[2]*t

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z, label="Line")
ax.scatter(P[0], P[1], P[2], color='red', s=50, label="Point (2,-1,4)")

# Labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Line through (2,-1,4) in direction (1,1,-2)')
ax.legend()

# Save as picture
plt.savefig("line_3d.png", dpi=300)
plt.show()
