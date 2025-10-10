# Code corrected by Gemini
# Based on the script by GVV Sharma
# September 12, 2025
# To plot the intersection of a line and a plane, ensuring the plane stays within the plot box.

import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- Define the Plane from the problem: r . (i+j+k) = 3 => x + y + z = 3 ---
# The plane equation is ax + by + cz = d
a, b, c, d = 1, 1, 1, 3 

# --- Define the Line from the problem: r = (1,-1,1) + lambda(3,-1,2) ---
line_point = np.array([1, -1, 1])
line_direction = np.array([3, -1, 2])

# --- Calculate the Intersection Point ---
# (1+3L) + (-1-L) + (1+2L) = 3  => 1 + 4L = 3 => L = 0.5
lam = 0.5
intersection_point = line_point + lam * line_direction

# --- Plotting Setup ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Define the boundaries of our 3D box
plot_lim = 8

# Generate grid points for the plane's X and Y coordinates
x_plane = np.linspace(-plot_lim, plot_lim, 50)
y_plane = np.linspace(-plot_lim, plot_lim, 50)
X, Y = np.meshgrid(x_plane, y_plane)

# Calculate corresponding Z values for the plane
Z = (d - a*X - b*Y) / c

# *** CRUCIAL STEP: MASKING ***
# Set Z values outside the plot limits to NaN so they are not plotted
Z[(Z > plot_lim) | (Z < -plot_lim)] = np.nan

# Plot the plane surface. The NaN values will create "holes" where the plane
# would have gone out of the box.
ax.plot_surface(X, Y, Z, alpha=0.6, color='cyan', label='Plane: x+y+z=3')

# Generate points for the line segment to be plotted
t = np.linspace(-3, 3, 100)
line_x = line_point[0] + t * line_direction[0]
line_y = line_point[1] + t * line_direction[1]
line_z = line_point[2] + t * line_direction[2]

# Plot the line
ax.plot(line_x, line_y, line_z, label='Line', color='magenta', linewidth=3)

# Plot the intersection point
ax.scatter(intersection_point[0], intersection_point[1], intersection_point[2], 
           color='red', s=150, label=f'Intersection Point', zorder=10)

# --- Formatting the Plot ---
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)
ax.set_zlabel('Z-axis', fontsize=12)
ax.set_title('Angle between a Line and a Plane', fontsize=16)

# Set plot limits to create the 3D box
ax.set_xlim([-plot_lim, plot_lim])
ax.set_ylim([-plot_lim, plot_lim])
ax.set_zlim([-plot_lim, plot_lim])

# Adding a legend
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
legend_elements = [Line2D([0], [0], color='magenta', lw=3, label='Line'),
                   Patch(facecolor='cyan', edgecolor='k', label='Plane'),
                   Line2D([0], [0], marker='o', color='w', label='Intersection Point',
                          markerfacecolor='red', markersize=10)]
ax.legend(handles=legend_elements)

plt.grid(True)
ax.set_box_aspect([1,1,1])  # Equal aspect ratio for a cubic view

# Save the figure
plt.savefig('plane_line_intersection_clipped.pdf')
plt.show()