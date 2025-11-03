import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plane coefficients
plane_params = [
    (1, 2, 3, 2),    # Plane 1
    (1, -1, 1, 3),   # Plane 2
    (-5, 11, -1, -17) # Plane 3
]

# Generate grid points for x and y (common grid for all planes)
x = np.linspace(-8, 8, 100)
y = np.linspace(-8, 8, 100)
X, Y = np.meshgrid(x, y)

for (a, b, c, d) in plane_params:
    # Compute z values for the current plane
    # Avoid division by zero for nearly flat planes (rare)
    if abs(c) > 1e-8:
        Z = (-a*X - b*Y - d) / c
        ax.plot_surface(X, Y, Z, alpha=0.5)

# Set limits for axes and aspect ratio
ax.set_xlim(-14, 14)
ax.set_ylim(-14, 14)
ax.set_zlim(-14, 14)
ax.set_box_aspect([1, 1, 1])  # Equal aspect ratio

plt.grid(True)
plt.savefig('../figs/fig.png')
plt.show()
