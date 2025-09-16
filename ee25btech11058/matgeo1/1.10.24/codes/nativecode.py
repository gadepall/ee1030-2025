import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the plane: 6x - 3y - 2z + 1 = 0
normal = np.array([6, -3, -2])  # Normal vector to the plane

# Create grid for the plane
x = np.linspace(-5, 5, 10)
y = np.linspace(-5, 5, 10)
X, Y = np.meshgrid(x, y)
Z = (6*X - 3*Y + 1)/2  # Rearranged plane equation

# Plot the plane
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, alpha=0.5, color='cyan', edgecolor='k')

# Plot the normal vector from the origin
ax.quiver(0, 0, 0, normal[0], normal[1], normal[2], 
          color='r', linewidth=2, label='Normal Vector (6, -3, -2)')

# Labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Plane $6x - 3y - 2z + 1 = 0$ and its Normal Vector')

# Legend
ax.legend()

# Show plot
plt.show()
