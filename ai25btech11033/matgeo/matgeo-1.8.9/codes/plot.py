import numpy as np
import matplotlib.pyplot as plt

# Define point P and origin O
P = np.array([-6, 8])
O = np.array([0, 0])

# Compute Euclidean distance using NumPy
distance = np.linalg.norm(P - O)

# Print the result
print(f"Distance from origin = {distance}")

# Create the plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect('equal', 'box')  # Ensure equal scaling in both axes

# Plot the origin and point P
ax.plot(O[0], O[1], 'ko', label='Origin (0, 0)')
ax.plot(P[0], P[1], 'ro', label=f'Point P ({P[0]}, {P[1]})')

# Draw the line between them
ax.plot([O[0], P[0]], [O[1], P[1]], 'b--', label=f'Distance = {distance:.1f}')

# Annotate distance at the midpoint
mid_x, mid_y = (O[0] + P[0]) / 2, (O[1] + P[1]) / 2
ax.text(mid_x, mid_y + 0.5, f"{distance:.1f}", color='blue',
        fontsize=12, ha='center')

# Add labels, legend, grid, and title
ax.set_title('Distance from Origin to Point P')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend()
ax.grid(True)

# Set axis limits for better framing
pad = 2
xmin, xmax = min(O[0], P[0]) - pad, max(O[0], P[0]) + pad
ymin, ymax = min(O[1], P[1]) - pad, max(O[1], P[1]) + pad
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)

plt.show()

