import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define vectors
v_rain = np.array([0, 0, -30])   # Rain velocity (downward along z)
v_woman = np.array([10, 0, 0])   # Woman velocity (south along x)
v_rel = v_rain - v_woman         # Relative velocity

# Create 3D plot
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Origin
origin = np.array([0, 0, 0])

# Plot vectors
ax.quiver(*origin, *v_rain, color='blue', linewidth=2, arrow_length_ratio=0.1, label="Rain velocity")
ax.quiver(*origin, *v_woman, color='green', linewidth=2, arrow_length_ratio=0.1, label="Woman velocity")
ax.quiver(*origin, *v_rel, color='red', linewidth=2, arrow_length_ratio=0.1, label="Relative velocity")

# Set labels
ax.set_xlim([-15, 15])
ax.set_ylim([-15, 15])
ax.set_zlim([-35, 5])

ax.set_xlabel("x (South direction)")
ax.set_ylabel("y (East direction)")
ax.set_zlabel("z (Vertical Down)")

ax.set_title("3D Representation of Rain and Bicycle Problem")
ax.legend()

plt.show()


