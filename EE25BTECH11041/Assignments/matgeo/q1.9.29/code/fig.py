import numpy as np
import matplotlib.pyplot as plt
import math

# --- 1. Define the given points and distance ---
p_a = np.array([3, -1])
x_b = 11
distance = 10

# --- 2. Solve for y ---
# We have the equation: distance^2 = (x_b - p_a[0])^2 + (y - p_a[1])^2
# 10^2 = (11 - 3)^2 + (y - (-1))^2
# 100 = 8^2 + (y + 1)^2
# 100 = 64 + (y + 1)^2
# 36 = (y + 1)^2
# So, y + 1 = +/- 6

# First solution for y
y1 = 6 - 1
# Second solution for y
y2 = -6 - 1

p_b1 = np.array([x_b, y1])
p_b2 = np.array([x_b, y2])

# --- 3. Plot the results ---
# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(10, 10))

# Plot the points A, B1, and B2
ax.scatter(p_a[0], p_a[1], color='red', s=100, zorder=5)
ax.scatter(p_b1[0], p_b1[1], color='blue', s=100, zorder=5)
ax.scatter(p_b2[0], p_b2[1], color='green', s=100, zorder=5)

# Annotate the points directly on the graph
ax.text(p_a[0] + 0.3, p_a[1], f'A ({p_a[0]}, {p_a[1]})', fontsize=12, verticalalignment='center', color='red')
ax.text(p_b1[0] + 0.3, p_b1[1], f'B1 ({p_b1[0]}, {p_b1[1]})', fontsize=12, verticalalignment='center', color='blue')
ax.text(p_b2[0] + 0.3, p_b2[1], f'B2 ({p_b2[0]}, {p_b2[1]})', fontsize=12, verticalalignment='center', color='green')


# Draw the lines representing the distance
ax.plot([p_a[0], p_b1[0]], [p_a[1], p_b1[1]], 'b--', label=f'Distance = {distance} units')
ax.plot([p_a[0], p_b2[0]], [p_a[1], p_b2[1]], 'g--')

# --- Visualization Aid: Draw a circle centered at A with radius 10 ---
# The solution points B1 and B2 must lie on this circle.
circle = plt.Circle(p_a, distance, color='red', fill=False, linestyle=':', alpha=0.5)
ax.add_artist(circle)

# --- Visualization Aid: Draw the vertical line x = 11 ---
# Point B must lie on this line.
ax.axvline(x=x_b, color='purple', linestyle='-.', alpha=0.5)

# --- 4. Formatting the plot ---
ax.set_title('Geometric Solution for the Distance Problem', fontsize=16)
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)

# Set equal aspect ratio to ensure the circle is not distorted
ax.set_aspect('equal', adjustable='box')

# Add grid and legend
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.legend(fontsize=10)

# Set axis limits to give some padding around the points
plt.xlim(p_a[0] - distance - 2, p_a[0] + distance + 2)
plt.ylim(p_a[1] - distance - 2, p_a[1] + distance + 2)

# Save the plot as a PNG file
plt.savefig('distance_plot.png')

# Show the plot
plt.show()

