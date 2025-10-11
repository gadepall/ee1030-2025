import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# Points for |r| = 2*sqrt(3) equally inclined -> components equal (±2, ±2, ±2)
point1 = np.array([2, 2, 2], dtype=float)
point2 = np.array([-2, -2, -2], dtype=float)

# Figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Vectors from origin
vector1 = point1
vector2 = point2

# Plot the two vectors
ax.quiver(0, 0, 0, vector1[0], vector1[1], vector1[2],
          label='Vector 1: (2, 2, 2)', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, vector2[0], vector2[1], vector2[2],
          label='Vector 2: (-2, -2, -2)', arrow_length_ratio=0.1)

# Draw coordinate axes (both positive and negative)
scale = 4
ax.quiver(0, 0, 0,  scale, 0, 0, arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, -scale, 0, 0, arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, 0,  scale, 0, arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, 0, -scale, 0, arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, 0, 0,  scale, arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, 0, 0, -scale, arrow_length_ratio=0.1)

# Plot the coordinate planes (transparent)
xx, yy = np.meshgrid(np.linspace(-scale, scale, 10),
                     np.linspace(-scale, scale, 10))
zz = np.zeros_like(xx)
ax.plot_surface(xx, yy, zz, alpha=0.2, rstride=100, cstride=100)  # XY-plane

yy, zz = np.meshgrid(np.linspace(-scale, scale, 10),
                     np.linspace(-scale, scale, 10))
xx = np.zeros_like(yy)
ax.plot_surface(xx, yy, zz, alpha=0.2, rstride=100, cstride=100)  # YZ-plane

xx, zz = np.meshgrid(np.linspace(-scale, scale, 10),
                     np.linspace(-scale, scale, 10))
yy = np.zeros_like(xx)
ax.plot_surface(xx, yy, zz, alpha=0.2, rstride=100, cstride=100)  # ZX-plane

# Limits and labels
ax.set_xlim([-scale, scale])
ax.set_ylim([-scale, scale])
ax.set_zlim([-scale, scale])
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

ax.set_title(r"Vectors equally inclined to axes with $|\vec r|=2\sqrt{3}$")
ax.legend()
plt.show()

