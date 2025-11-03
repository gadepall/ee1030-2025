import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Intersection point (calculated from the system)
poi = np.array([0, -3, -1])

# Grid for plotting planes
x_range = np.linspace(-4, 4, 30)
y_range = np.linspace(-6, 0, 30)
X, Y = np.meshgrid(x_range, y_range)

# Plane 1: x - y + 2z = 1  ->  z = (1 - x + y) / 2
Z1 = (1 - X + Y) / 2

# Plane 2: z = -1
Z2 = -1 * np.ones_like(X)

# Plane 3: 3x - 2y + 4z = 2  -> z = (2 - 3x + 2y) / 4
Z3 = (2 - 3*X + 2*Y) / 4

# Create plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot planes with distinct colors
ax.plot_surface(X, Y, Z1, alpha=0.5, color='red')
ax.plot_surface(X, Y, Z2, alpha=0.5, color='green')
ax.plot_surface(X, Y, Z3, alpha=0.5, color='blue')

# Mark and label the intersection point
ax.scatter([poi[0]], [poi[1]], [poi[2]], s=100, c='black', marker='o')
ax.text(poi[0], poi[1], poi[2]+0.3, f'POI (0, -3, -1)', 
        color='black', fontsize=11, weight='bold')

# Labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Intersection of Three Planes')

# Add legend manually
legend_elements = [
    Line2D([0], [0], color='red', lw=4, label='x - y + 2z = 1'),
    Line2D([0], [0], color='green', lw=4, label='z = -1'),
    Line2D([0], [0], color='blue', lw=4, label='3x - 2y + 4z = 2')
]
ax.legend(handles=legend_elements, loc='upper right')

# Adjust view angle
ax.view_init(elev=20, azim=30)

# Save the figure
plt.savefig("graph9.png", dpi=300, bbox_inches='tight')
plt.close()
