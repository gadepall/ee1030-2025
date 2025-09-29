import numpy as np
import matplotlib.pyplot as plt

# Create meshgrid for plane
xx, yy = np.meshgrid(np.linspace(-2, 8, 20), np.linspace(-2, 8, 20))
zz = -xx + yy + 1   # From x - y + z - 1 = 0 => z = -x + y + 1

# Line parametric equations: (x,y,z) = (3,6,4) + t(1,5,4)
t = np.linspace(-2, 2, 100)
x_line = 3 + t*1
y_line = 6 + t*5
z_line = 4 + t*4

# Given point
P0 = (3, 2, 0)

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot plane
ax.plot_surface(xx, yy, zz, alpha=0.5, color='cyan')

# Plot line
ax.plot(x_line, y_line, z_line, 'r', label='Line')

# Plot point P0
ax.scatter(P0[0], P0[1], P0[2], color='k', s=50, label='Point (3,2,0)')

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Plane and Line")
ax.legend()

# Save as image
plt.savefig("plane_line.png", dpi=300)
plt.show()