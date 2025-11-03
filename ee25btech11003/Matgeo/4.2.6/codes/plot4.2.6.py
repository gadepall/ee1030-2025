import matplotlib.pyplot as plt
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(6, 6))

# Set axis limits and aspect ratio to match the TikZ plot
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2, 2.5)
ax.set_aspect('equal', adjustable='box')

# Draw the grid
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Draw the main axes lines
ax.axhline(y=0, color='k', linewidth=0.8)
ax.axvline(x=0, color='k', linewidth=0.8)

# --- Plot the elements from the TikZ diagram ---

# 1. The line x = -2/3
x_line = -2/3
ax.axvline(x=x_line, color='blue', linewidth=2, label='$3x+2=0$')

# 2. The point P on the line
p_coords = np.array([x_line, 0.5])
ax.plot(p_coords[0], p_coords[1], 'o', color='black', markersize=6)

# 3. The normal vector n
# Vector starts at P and has direction (1, 0)
ax.quiver(p_coords[0], p_coords[1], 1, 0, angles='xy', scale_units='xy', scale=1, color='red', width=0.01)

# 4. The direction vector m
# Vector starts at P and has direction (0, 1)
ax.quiver(p_coords[0], p_coords[1], 0, 1, angles='xy', scale_units='xy', scale=1, color='green', width=0.01)


# --- Add labels ---

# Label axes
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

# Label origin 'O'
ax.text(-0.2, -0.2, '$O$', fontsize=12)

# Label vectors 'n' and 'm'
ax.text(p_coords[0] + 1.1, p_coords[1], '$\\mathbf{n}$', fontsize=14, color='red', va='center')
ax.text(p_coords[0] + 0.1, p_coords[1] + 1.1, '$\\mathbf{m}$', fontsize=14, color='green', va='center')

# Add legend for the line label
ax.legend()

# Set the title (acting as the caption)
ax.set_title('The line $3x+2=0$ with its normal vector $\\mathbf{n}$ and direction vector $\\mathbf{m}$')

# Save the figure
plt.savefig('line_and_vectors.png', bbox_inches='tight')
plt.show()
