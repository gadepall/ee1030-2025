import matplotlib.pyplot as plt
import numpy as np

# --- Data Points ---
# Define the coordinates for the vertices of the triangle A, B, and C.
# These are inferred from the grid in the provided image.
point_a = np.array([0, 5])
point_b = np.array([0, 0])
point_c = np.array([12, 0])

# --- Plot Setup ---
# Create a figure and axes for the 2D plot.
# We can adjust figsize to make the plot larger or smaller.
fig, ax = plt.subplots(figsize=(8, 6))

# --- Plotting the Elements ---
# 1. Plot the sides of the triangle
# The plot function takes a list of x-coordinates and a list of y-coordinates.
# Side AB (from A to B)
ax.plot([point_a[0], point_b[0]], [point_a[1], point_b[1]], label='Side AB = 5.00 cm')
# Side BC (from B to C)
ax.plot([point_b[0], point_c[0]], [point_b[1], point_c[1]], label='Side BC = 12.00 cm')
# Side AC (from A to C)
ax.plot([point_a[0], point_c[0]], [point_a[1], point_c[1]], label='Side AC = 13.00 cm')

# 2. Plot the points A, B, and C as red circles
# We use scatter for this. 's' controls size, 'c' is color.
points_x = [point_a[0], point_b[0], point_c[0]]
points_y = [point_a[1], point_b[1], point_c[1]]
ax.scatter(points_x, points_y, s=50, c='red', zorder=5) # zorder makes points appear on top of lines

# 3. Add text labels 'A', 'B', and 'C' near the points
# The coordinates are slightly offset so the text doesn't overlap the point.
ax.text(point_a[0] - 0.5, point_a[1] + 0.1, 'A', fontsize=14)
ax.text(point_b[0] - 0.5, point_b[1] + 0.1, 'B', fontsize=14)
ax.text(point_c[0] + 0.2, point_c[1] + 0.1, 'C', fontsize=14)

# --- Final Touches ---
# 1. Set the labels for the axes
ax.set_xlabel('x')
ax.set_ylabel('y')

# 2. Set the axis limits to match the image
ax.set_xlim(-1, 13)
ax.set_ylim(-2, 7)

# 3. Add a grid
ax.grid(True)

# 4. Make the aspect ratio equal so the triangle isn't distorted
ax.set_aspect('equal', adjustable='box')

# 5. Add a legend to identify the plotted sides
ax.legend()

# --- Display the Plot ---
# This command opens a window to show the plot
plt.show()


