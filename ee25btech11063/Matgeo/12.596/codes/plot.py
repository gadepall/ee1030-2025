import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define grid for planes
x = np.linspace(-8, 5, 100)
y = np.linspace(-8, 5, 100)
X, Y = np.meshgrid(x, y)

# Plane equations
Z1 = (-1 - X + 2*Y)/3          # Plane 1: x - 2y + 3z = -1
Z2 = (1 - X + 3*Y)/4           # Plane 2: x - 3y + 4z = 1
Z3 = (-2*X + 4*Y - 2)/6        # Plane 3: -2x + 4y - 6z = 2 (multiple of Plane 1)

# Plotting
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

# Plot planes (red drawn last so it's visible on top of blue)
ax.plot_surface(X, Y, Z2, alpha=0.4, color='green')  # Plane 2
ax.plot_surface(X, Y, Z3, alpha=0.3, color='blue')   # Plane 3
ax.plot_surface(X, Y, Z1, alpha=0.6, color='red')    # Plane 1

# Line of intersection
t = np.linspace(-5, 5, 100)
x_line = -t - 5
y_line = t - 2
z_line = t
ax.plot(x_line, y_line, z_line, color='black', linewidth=3, label="Line of Intersection")

# Labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title("Intersection of 3 Planes (k=2): Infinite Solutions")

# Add plane labels
ax.text(2, -5, 3, "Plane 1: x-2y+3z=-1", color='red')
ax.text(2, -5, -2, "Plane 2: x-3y+4z=1", color='green')
ax.text(-6, 4, 2, "Plane 3: -2x+4y-6z=2", color='blue')

# Show legend
ax.legend()

# Save figure
plt.savefig("planes_intersection.png", dpi=300, bbox_inches='tight')

# Display figure
plt.show()

