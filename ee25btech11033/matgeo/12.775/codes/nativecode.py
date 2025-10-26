import numpy as np
import matplotlib.pyplot as plt
# The Axes3D object is part of the mplot3d toolkit, which is included with matplotlib
from mpl_toolkits.mplot3d import Axes3D

# --- Setup for the 3D Plot ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# --- Create a grid of (x,y) points to plot the planes over ---
x_vals = np.linspace(-10, 10, 50)
y_vals = np.linspace(-10, 10, 50)
X, Y = np.meshgrid(x_vals, y_vals)

# --- Define Plane 1 from the equation: x - 2y + z = 0 ---
# Rearranging for z gives: z = 2y - x
Z1 = 2 * Y - X

# --- Define Plane 2 from the equation: x - z = 0 ---
# Rearranging for z gives: z = x
Z2 = X

# --- Plot the two planes using plot_surface ---
# We use transparency (alpha) to make the intersection visible.
ax.plot_surface(X, Y, Z1, alpha=0.6, color='c', label='Plane 1: x - 2y + z = 0')
ax.plot_surface(X, Y, Z2, alpha=0.6, color='m', label='Plane 2: x - z = 0')

# --- Define and plot the line of intersection ---
# The solution is x = α(1,1,1), which means x=α, y=α, z=α.
alpha = np.linspace(-10, 10, 100) # Parameter for the line
ax.plot(alpha, alpha, alpha, color='red', linewidth=3, label='Intersection Line: α(1,1,1)')

# --- Formatting the plot with labels and title ---
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Since matplotlib struggles with legends for surface plots, we create proxy artists.
p1 = plt.Rectangle((0, 0), 1, 1, fc="c", alpha=0.6)
p2 = plt.Rectangle((0, 0), 1, 1, fc="m", alpha=0.6)
line = plt.Line2D([0,1],[0,1], color='red', linewidth=3)
ax.legend([p1, p2, line], ['Plane 1: x - 2y + z = 0', 'Plane 2: x - z = 0', 'Intersection Line (Solution Set)'])

# Set a suitable viewing angle
ax.view_init(elev=25, azim=-50)

plt.savefig('../figs/fig.png')
# Display the plot
plt.show()
