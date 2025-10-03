import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Define the plane equation: 2x + y - z + 5 = 0
# Rearranged: z = 2x + y + 5
xx, yy = np.meshgrid(np.linspace(-6, 6, 20), np.linspace(-6, 6, 20))
zz = 2*xx + yy + 5

# Intercepts
x_int = (-5/2, 0, 0)
y_int = (0, -5, 0)
z_int = (0, 0, 5)

# Plotting setup
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the plane
ax.plot_surface(xx, yy, zz, alpha=0.5, color='cyan')

# Plot intercepts
ax.scatter(*x_int, color='red', s=60, label="X-intercept (-5/2, 0, 0)")
ax.scatter(*y_int, color='blue', s=60, label="Y-intercept (0, -5, 0)")
ax.scatter(*z_int, color='green', s=60, label="Z-intercept (0, 0, 5)")

# Labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Axis limits
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_zlim(-6, 6)

# Legend
ax.legend()

# Show the plot
plt.show()
