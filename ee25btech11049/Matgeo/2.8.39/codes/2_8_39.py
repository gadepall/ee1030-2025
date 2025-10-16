# Code by GVV Sharma
# July 22, 2024
# Released under GNU GPL
# This script finds the angle between two lines whose direction cosines
# are given by the equations:
# l + m + n = 0
# l^2 + m^2 - n^2 = 0

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# From the mathematical derivation, we found the direction ratios for the two lines.
# Case 1 (l=0) gives direction ratios proportional to (0, 1, -1)
d1_ratios = np.array([0, 1, -1])

# Case 2 (m=0) gives direction ratios proportional to (1, 0, -1)
d2_ratios = np.array([1, 0, -1])

print(f"Direction ratios for Line 1: {d1_ratios}")
print(f"Direction ratios for Line 2: {d2_ratios}")
print("-" * 30)

# --- Calculate Direction Cosines ---
# To get the direction cosines, we normalize the direction ratio vectors (divide by their magnitude).
norm_d1 = np.linalg.norm(d1_ratios)
norm_d2 = np.linalg.norm(d2_ratios)

# The direction cosines are the components of the unit vectors.
d1 = d1_ratios / norm_d1
d2 = d2_ratios / norm_d2

print(f"Direction cosines for Line 1: [{d1[0]:.4f}, {d1[1]:.4f}, {d1[2]:.4f}]")
print(f"Direction cosines for Line 2: [{d2[0]:.4f}, {d2[1]:.4f}, {d2[2]:.4f}]")
print("-" * 30)

# --- Calculate the angle using the dot product of direction cosines ---
# The dot product of two unit vectors (direction cosines) is the cosine of the angle between them.
cos_theta = np.dot(d1, d2)

# Calculate the angle in radians
angle_rad = np.arccos(cos_theta)

# Convert the angle to degrees
angle_deg = np.degrees(angle_rad)

print(f"Cosine of the angle (from dot product of cosines): {cos_theta:.4f}")
print("-" * 30)
print(f"The angle between the lines is {angle_rad:.4f} radians.")
print(f"The angle between the lines is {angle_deg:.2f} degrees.")

# --- Plotting the vectors in 3D ---
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Origin point
origin = [0, 0, 0]

# Plot the direction cosine vectors (unit vectors) as arrows from the origin
label1 = f'Line 1 DC: ({d1[0]:.2f}, {d1[1]:.2f}, {d1[2]:.2f})'
label2 = f'Line 2 DC: ({d2[0]:.2f}, {d2[1]:.2f}, {d2[2]:.2f})'
ax.quiver(*origin, *d1, color='r', label=label1)
ax.quiver(*origin, *d2, color='b', label=label2)


# Set the plot limits to be consistent
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 1.5])

# Add labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Visualization of the Two Lines in 3D')
ax.legend()
ax.grid(True)

# To make the aspect ratio equal
ax.set_box_aspect([1,1,1]) 

# Show the plot
plt.show()


