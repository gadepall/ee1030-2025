import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given line parameters
h = np.array([5, -4, 6])   # Point on the line
m = np.array([3, 7, 2])    # Direction vector

# Generate points along the line for k in [-2, 2]
k_values = np.linspace(-2, 2, 100)
line_points = np.array([h + k * m for k in k_values])

# Create 3D figure
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

# Plot the line
ax.plot(line_points[:,0], line_points[:,1], line_points[:,2], color='blue', label=r"$\vec{x} = \vec{h} + \kappa \vec{m}$")

# Mark the given point h
ax.scatter(h[0], h[1], h[2], color='red', s=60, label=r"Point $\vec{h}(5, -4, 6)$")

# Draw the direction vector m starting at h
ax.quiver(h[0], h[1], h[2], m[0], m[1], m[2], 
          color='green', arrow_length_ratio=0.1, linewidth=2, label=r"Direction $\vec{m}(3,7,2)$")

# Set axis labels and title
ax.set_xlabel("X - AXIS")
ax.set_ylabel("Y - AXIS")
ax.set_zlabel("Z - AXIS")
ax.set_title("Line: (x−5)/3 = (y+4)/7 = (z−6)/2")

# Legend and appearance
ax.legend()
ax.set_box_aspect([1,1,1])  # Equal aspect ratio
ax.view_init(elev=20, azim=130)

# Save and show
plt.savefig("fig.png", dpi=300)
plt.show()
