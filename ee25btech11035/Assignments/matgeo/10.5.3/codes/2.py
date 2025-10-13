import numpy as np
import matplotlib.pyplot as plt

circle_center = (0, 0)
radius = 5.0
tangent_intersection_point = (10, 0)

# Points of contact calculated in the solution
poc1 = (2.5, 5 * np.sqrt(3) / 2)
poc2 = (2.5, -5 * np.sqrt(3) / 2)

# Create x-values for the lines
x_vals = np.linspace(0, 12, 400)

# Equation 1: x - sqrt(3)y = 10  =>  y = (x - 10) / sqrt(3)
y_tangent1 = (x_vals - 10) / np.sqrt(3)

# Equation 2: x + sqrt(3)y = 10  =>  y = (10 - x) / sqrt(3)
y_tangent2 = (10 - x_vals) / np.sqrt(3)

fig, ax = plt.subplots(figsize=(12, 10))

# Plot the circle
circle = plt.Circle(circle_center, radius, color='skyblue', fill=False, linewidth=2, label='Circle (radius=5)')
ax.add_patch(circle)

# Plot the tangent lines
ax.plot(x_vals, y_tangent1, color='green', label='$x - \\sqrt{3}y = 10$')
ax.plot(x_vals, y_tangent2, color='orange', label='$x + \\sqrt{3}y = 10$')

# Plot the key points
ax.plot(circle_center[0], circle_center[1], 'ko', markersize=8, label='Center O(0,0)')
ax.plot(tangent_intersection_point[0], tangent_intersection_point[1], 'ro', markersize=8, label='Intersection h(10,0)')
ax.plot(poc1[0], poc1[1], 'mo', markersize=8, label='Point of Contact')
ax.plot(poc2[0], poc2[1], 'mo')

# Plot lines from center to points of contact (radii)
ax.plot([circle_center[0], poc1[0]], [circle_center[1], poc1[1]], 'k--', linewidth=1)
ax.plot([circle_center[0], poc2[0]], [circle_center[1], poc2[1]], 'k--', linewidth=1)

ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle=':')
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

# Set the limits for better visualization
ax.set_xlim(-6, 12)
ax.set_ylim(-8, 8)

ax.set_title('Tangents to a Circle Inclined at 60°', fontsize=16)
ax.set_xlabel('x-axis', fontsize=12)
ax.set_ylabel('y-axis', fontsize=12)
ax.legend()

# Save the plot to a file and display it
plt.savefig('2.png')
plt.show()