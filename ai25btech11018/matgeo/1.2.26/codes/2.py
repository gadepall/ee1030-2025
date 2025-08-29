import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Define vector components
rain_velocity = np.array([0, 0, -35])    # Rain falling vertically
woman_velocity = np.array([-12, 0, 0])   # Woman moving east to west
relative_velocity = rain_velocity - woman_velocity  # Relative velocity of rain w.r.t woman

# Origin point for vectors
origin = np.array([0, 0, 0])

# Plot setup
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot rain velocity vector (blue)
ax.quiver(*origin, *rain_velocity, color='blue', label='Rain Velocity', arrow_length_ratio=0.1)

# Plot woman velocity vector (green)
ax.quiver(*origin, *woman_velocity, color='green', label='Woman Velocity', arrow_length_ratio=0.1)

# Plot relative velocity vector (red)
ax.quiver(*origin, *relative_velocity, color='red', label='Relative Velocity (Umbrella Direction)', arrow_length_ratio=0.1)

# Set axis labels
ax.set_xlabel('X (East-West)')
ax.set_ylabel('Y (North-South)')
ax.set_zlabel('Z (Vertical)')

# Set plot limits
ax.set_xlim([-20, 20])
ax.set_ylim([-20, 20])
ax.set_zlim([-40, 10])

# Title and legend
ax.set_title('Direction to Hold Umbrella (Relative Velocity)')
ax.legend()

# Save the figure as an image
plt.savefig("fig.png", dpi=300)
# Show the plot
plt.show()

