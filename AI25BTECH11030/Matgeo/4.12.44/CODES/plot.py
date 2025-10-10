import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create grid for y and z
y_vals = np.linspace(-10, 10, 100)
z_vals = np.linspace(-10, 10, 100)
Y, Z = np.meshgrid(y_vals, z_vals)

# Calculate corresponding x using the plane equation: x = 2z
X = 2 * Z

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the plane
ax.plot_surface(X, Y, Z, alpha=0.5, color='cyan', edgecolor='k')

# Set axis labels with x, y, z
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('3D Plot of plane: x - 2z = 0')
plt.savefig("fig1.png")
plt.show()

