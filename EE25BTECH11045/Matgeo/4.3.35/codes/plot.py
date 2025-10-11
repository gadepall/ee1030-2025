import numpy as np
import matplotlib.pyplot as plt

# Plane equation: 2x - 3y + 5z + 4 = 0
x_int = -4/2   # X-intercept
y_int = 4/3    # Y-intercept
z_int = -4/5   # Z-intercept

# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Meshgrid for plane
xx, yy = np.meshgrid(np.linspace(-4, 4, 50), np.linspace(-4, 4, 50))
zz = (-2*xx + 3*yy - 4) / 5

# Plot plane
ax.plot_surface(xx, yy, zz, alpha=0.5, color='cyan')

# Draw coordinate axes (bold colored)
ax.plot([-4, 4], [0, 0], [0, 0], color='red', linewidth=2)   # X-axis
ax.plot([0, 0], [-4, 4], [0, 0], color='green', linewidth=2) # Y-axis
ax.plot([0, 0], [0, 0], [-4, 4], color='blue', linewidth=2)  # Z-axis

# Plot intercepts with big markers
ax.scatter(x_int, 0, 0, color='red', s=200, marker='o', edgecolor='k', zorder=5)
ax.scatter(0, y_int, 0, color='green', s=200, marker='o', edgecolor='k', zorder=5)
ax.scatter(0, 0, z_int, color='blue', s=200, marker='o', edgecolor='k', zorder=5)

# Add labels for intercepts
ax.text(x_int, 0, 0, f'(-2,0,0)', color='red', fontsize=12, weight='bold')
ax.text(0, y_int, 0, f'(0,1.33,0)', color='green', fontsize=12, weight='bold')
ax.text(0, 0, z_int, f'(0,0,-0.8)', color='blue', fontsize=12, weight='bold')

# Axes labels
ax.set_xlabel('X axis', fontsize=12, weight='bold')
ax.set_ylabel('Y axis', fontsize=12, weight='bold')
ax.set_zlabel('Z axis', fontsize=12, weight='bold')
ax.set_title('Plane 2x - 3y + 5z + 4 = 0 with Intercepts', fontsize=14, weight='bold')

# Equal aspect ratio
ax.set_box_aspect([1,1,0.8])

# Adjust view
ax.view_init(elev=25, azim=35)

plt.show()