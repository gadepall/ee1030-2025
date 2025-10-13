import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Patch

# Define the grid
x = np.linspace(-1, 10, 30)
y = np.linspace(-1, 10, 30)
X, Y = np.meshgrid(x, y)

# Define the planes
Z1 = 6 - X - Y                # From x + y + z = 6
Z2 = (7 - X) / 2              # From x + 2z = 7
Z3 = 12 - 3*X - Y             # From 3x + y + z = 12

# Plot the surfaces
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot planes
surf1 = ax.plot_surface(X, Y, Z1, alpha=0.5, color='red')
surf2 = ax.plot_surface(X, Y, Z2, alpha=0.5, color='green')
surf3 = ax.plot_surface(X, Y, Z3, alpha=0.5, color='blue')

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Graph of 3 Planes')

# Create custom legend
legend_patches = [
    Patch(color='red', label='x + y + z = 6'),
    Patch(color='green', label='x + 2z = 7'),
    Patch(color='blue', label='3x + y + z = 12')
]
ax.legend(handles=legend_patches)

plt.show()
