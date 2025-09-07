# Inspired by code from GVV Sharma
# September 5, 2024
# released under GNU GPL
# Find two vectors of magnitude 6 perpendicular to two given vectors and plot them.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given vectors
a = np.array([2, -1, 2])
b = np.array([4, -1, 3])

# To find a vector perpendicular to both a and b, we compute their cross product.
c = np.cross(a, b)

print(f"Vector 'a': {a}")
print(f"Vector 'b': {b}")
print(f"Vector perpendicular to a and b (a x b = c): {c}")

# Now, we need a vector of magnitude 6 in the direction of c.
# First, find the unit vector in the direction of c.
# Magnitude of c
norm_c = np.linalg.norm(c)
# Unit vector c_hat
c_hat = c / norm_c

print(f"Magnitude of c: {norm_c:.2f}")
print(f"Unit vector in the direction of c: {c_hat}")

# Define the desired magnitude
magnitude = 6

# Calculate the final vector v and its opposite
v1 = magnitude * c_hat
v2 = -v1

print(f"The first required vector 'v1' of magnitude {magnitude} is: {v1}")
print(f"The second required vector 'v2' of magnitude {magnitude} is: {v2}")
print(f"Verification: Magnitude of v1 is {np.linalg.norm(v1):.2f}")
print(f"Verification: Magnitude of v2 is {np.linalg.norm(v2):.2f}")


# --- Plotting the vectors ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Origin point
origin = [0, 0, 0]

# Plotting the vectors as lines from origin
ax.plot([origin[0], a[0]], [origin[1], a[1]], [origin[2], a[2]], color='r', label='A = [2, -1, 2]')
ax.plot([origin[0], b[0]], [origin[1], b[1]], [origin[2], b[2]], color='b', label='B = [4, -1, 3]')
ax.plot([origin[0], v1[0]], [origin[1], v1[1]], [origin[2], v1[2]], color='g', label=f'Result C1 = [{v1[0]:.0f}, {v1[1]:.0f}, {v1[2]:.0f}]')
ax.plot([origin[0], v2[0]], [origin[1], v2[1]], [origin[2], v2[2]], color='m', label=f'Result C2 = [{v2[0]:.0f}, {v2[1]:.0f}, {v2[2]:.0f}]')

# Adding text labels at the end of each vector
ax.text(a[0]*1.1, a[1]*1.1, a[2]*1.1, 'A', color='r', fontsize=12)
ax.text(b[0]*1.1, b[1]*1.1, b[2]*1.1, 'B', color='b', fontsize=12)
ax.text(v1[0]*1.1, v1[1]*1.1, v1[2]*1.1, 'C1', color='g', fontsize=12)
ax.text(v2[0]*1.1, v2[1]*1.1, v2[2]*1.1, 'C2', color='m', fontsize=12)


# Setting the plot limits to be symmetric and encompass all vectors
max_val = np.max(np.abs(np.vstack((a, b, v1)))) * 1.2
ax.set_xlim([-max_val, max_val])
ax.set_ylim([-max_val, max_val])
ax.set_zlim([-max_val, max_val])

# Adding labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Perpendicular Vector Visualization')
ax.legend()
ax.grid(True)

# Change the viewing angle (elevation, azimuth)
ax.view_init(elev=25, azim=-45)

# To make the aspect ratio equal
ax.set_box_aspect([1,1,1]) 

# Save the figure as a PNG file
plt.savefig('vector_plot.png')

# Show the plot
plt.show()

