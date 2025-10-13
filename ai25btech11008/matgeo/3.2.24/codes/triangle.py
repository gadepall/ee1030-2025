import matplotlib.pyplot as plt
import numpy as np

# Points based on the solution:
A = np.array([0, 0])
B = np.array([5, 0])
C = np.array([3 * np.sqrt(2), 3 * np.sqrt(2)])

# Create the figure and axis
fig, ax = plt.subplots()

# Plot the triangle edges
triangle_points = np.array([A, B, C, A])  # back to A to close the triangle
ax.plot(triangle_points[:, 0], triangle_points[:, 1], 'b-', marker='o')

# Annotate points
ax.text(A[0], A[1], 'A', fontsize=12, ha='right', va='top')
ax.text(B[0], B[1], 'B', fontsize=12, ha='left', va='top')
ax.text(C[0], C[1], 'C', fontsize=12, ha='left', va='bottom')

# Set equal aspect ratio
ax.set_aspect('equal', 'box')

# Set grid, labels, and title
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_xlabel('x (cm)')
ax.set_ylabel('y (cm)')
ax.set_title('Triangle ABC with CA = 6 cm, AB = 5 cm, and ∠BAC = 45°')

# Set limits for better visualization
padding = 1
min_x, max_x = min(A[0], B[0], C[0]) - padding, max(A[0], B[0], C[0]) + padding
min_y, max_y = min(A[1], B[1], C[1]) - padding, max(A[1], B[1], C[1]) + padding
ax.set_xlim(min_x, max_x)
ax.set_ylim(min_y, max_y)

# Save the plot as 'python_plot.png'
plt.savefig('fig1.png', dpi=300)

# Show the plot
plt.show()


