# plot.py
import numpy as np
import matplotlib.pyplot as plt

data = np.load('points.npz')
xs, ys, zs = data['xs'], data['ys'], data['zs']
normal = data['normal']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Line
ax.plot(xs, ys, zs, label="Line through (1,-3,2)")

# Point
ax.scatter([1], [-3], [2], color='red', s=60, label="Point (1,-3,2)")

# Normal vector (as direction vector)
ax.quiver(1, -3, 2, normal[0], normal[1], normal[2], color='green', length=15, label="Direction vector (1,1,1)")

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.title('3D Line passing through(1,-3,2)')
plt.show()

