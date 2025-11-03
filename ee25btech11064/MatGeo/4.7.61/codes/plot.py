import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Plane equation: 2x - 3y + 4z - 6 = 0
# The point is the foot of the perpendicular (12/29, 18/29, 24/29)
foot_of_perpendicular = np.array([12/29, 18/29, 24/29])

# Create grid for the plane
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# Solve for Z using the plane equation 2x - 3y + 4z - 6 = 0
Z = (6 - 2*X + 3*Y) / 4

# Create a 3D plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the plane
ax.plot_surface(X, Y, Z, alpha=0.5, rstride=100, cstride=100, color='gray', edgecolor='k')

# Plot the foot of the perpendicular
ax.scatter(foot_of_perpendicular[0], foot_of_perpendicular[1], foot_of_perpendicular[2], color='g', s=10, label='Foot of Perpendicular')

# Plot the origin
ax.scatter(0, 0, 0, color='r', s=10, label='Origin')

# Draw the vector from origin to foot of perpendicular
ax.quiver(0, 0, 0, foot_of_perpendicular[0], foot_of_perpendicular[1], foot_of_perpendicular[2], 
          color='b', linewidth=2, label='Vector from Origin to Foot')

# Labels and Title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Plane with Foot of Perpendicular from Origin')

# Show the plot
plt.legend()
plt.show()

