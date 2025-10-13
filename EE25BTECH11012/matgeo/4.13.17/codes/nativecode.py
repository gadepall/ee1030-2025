import matplotlib.pyplot as plt
import numpy as np

# --- 1. Define the geometric elements ---

# The two fixed points from the problem
f1 = np.array([1, 0])
f2 = np.array([-1, 0])

# The locus of points P such that dist(P, F1) / dist(P, F2) = 1/3 is a circle.
# By solving the distance equation, we find the circle's properties:
# 9 * ((x-1)^2 + y^2) = (x+1)^2 + y^2
# 8x^2 - 20x + 8y^2 + 8 = 0
# x^2 - (5/2)x + y^2 + 1 = 0
# (x - 5/4)^2 + y^2 = (3/4)^2
# The center of this circle is the circumcenter of triangle ABC.
circumcenter = np.array([5/4, 0])
radius = 3/4

# --- 2. Generate points for plotting ---

# Create points for the circle (the circumcircle)
theta = np.linspace(0, 2 * np.pi, 200)
circle_x = circumcenter[0] + radius * np.cos(theta)
circle_y = circumcenter[1] + radius * np.sin(theta)

# Create three arbitrary, distinct points (A, B, C) on the circle for visualization
angles = np.array([np.pi/4, 5*np.pi/6, 3*np.pi/2])
A = circumcenter + radius * np.array([np.cos(angles[0]), np.sin(angles[0])])
B = circumcenter + radius * np.array([np.cos(angles[1]), np.sin(angles[1])])
C = circumcenter + radius * np.array([np.cos(angles[2]), np.sin(angles[2])])
triangle_points = np.array([A, B, C, A]) # Add A at the end to close the triangle

# --- 3. Create the plot ---

# Set up the plot style and figure
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the circumcircle
ax.plot(circle_x, circle_y, 'b-', label='Locus of A, B, C (Circumcircle)')

# Plot the example triangle ABC
ax.plot(triangle_points[:, 0], triangle_points[:, 1], 'g--', marker='o', markersize=8, label='Example Triangle ABC')

# Plot the two fixed points
ax.plot(f1[0], f1[1], 'ro', markersize=10, label='Fixed Point F1 (1, 0)')
ax.plot(f2[0], f2[1], 'mo', markersize=10, label='Fixed Point F2 (-1, 0)')

# Plot and highlight the circumcenter
ax.plot(circumcenter[0], circumcenter[1], 'k*', markersize=15, label=f'Circumcenter ({circumcenter[0]}, {circumcenter[1]})')

# --- 4. Add labels and formatting ---

# Annotate the points on the graph
ax.text(A[0], A[1] + 0.1, 'A', fontsize=14, color='green')
ax.text(B[0] - 0.15, B[1], 'B', fontsize=14, color='green')
ax.text(C[0], C[1] - 0.15, 'C', fontsize=14, color='green')
ax.text(circumcenter[0], circumcenter[1] + 0.05, 'Circumcenter', fontsize=12, ha='center')


# Set plot title and axis labels
ax.set_title('Solution for Finding the Circumcenter', fontsize=16)
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)

# Ensure the aspect ratio is equal to prevent the circle from looking like an ellipse
ax.set_aspect('equal', adjustable='box')
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

# Add legend and grid
ax.legend(loc='upper right')
ax.grid(True)

# Set axis limits for a clean view
ax.set_xlim(-2, 3)
ax.set_ylim(-1.5, 1.5)

# Display the final plot
plt.show()