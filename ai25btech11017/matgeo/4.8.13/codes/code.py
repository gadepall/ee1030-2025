import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the planes:
# Plane 1: 2x - 3y + 6z - 4 = 0
# Plane 2: 6x - 9y + 18z + 30 = 0

# Normalize Plane 2 (divide by 3) → 2x - 3y + 6z + 10 = 0
# Now both planes are parallel with same normal vector n = (2, -3, 6)

# Grid for plotting
xx, yy = np.meshgrid(np.linspace(-10, 10, 20), np.linspace(-10, 10, 20))

# Plane 1: solve for z
zz1 = (4 - 2*xx + 3*yy) / 6

# Plane 2: solve for z
zz2 = (-10 - 2*xx + 3*yy) / 6

# Create 3D figure
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the planes
ax.plot_surface(xx, yy, zz1, alpha=0.5, color='blue', rstride=100, cstride=100, label='Plane 1')
ax.plot_surface(xx, yy, zz2, alpha=0.5, color='red', rstride=100, cstride=100, label='Plane 2')

# Normal vector
n = np.array([2, -3, 6])

# Pick a point on Plane 1 (let y=z=0, solve for x)
x0 = (4)/2  # when y=z=0
P1 = np.array([x0, 0, 0])

# Distance formula: |d2 - d1| / ||n||
d1 = -4
d2 = 10
distance = abs(d2 - d1) / np.linalg.norm(n)

# Direction of normal vector (unit)
n_unit = n / np.linalg.norm(n)

# Point on Plane 2 along the normal
P2 = P1 + distance * n_unit

# Plot the connecting line (shortest distance)
ax.plot([P1[0], P2[0]], [P1[1], P2[1]], [P1[2], P2[2]], 'k--', linewidth=2)

# Mark points
ax.scatter(*P1, color='blue', s=50)
ax.scatter(*P2, color='red', s=50)

# Labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title(f"Distance between planes = {distance:.2f}")

# Save figure
plt.savefig("planes_distance.png", dpi=300)
plt.show()
