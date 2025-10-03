import matplotlib.pyplot as plt
import numpy as np

# 1. Set up the figure and axes
fig, ax = plt.subplots(figsize=(10, 8))

# 2. Define and plot the square boundary (Set A)
# We define the corner points in order to draw the lines connecting them.
# The last point is the same as the first to close the square.
a_square = [4, 6, 6, 4, 4]
b_square = [4, 4, 6, 6, 4]
ax.plot(
    a_square, b_square,
    color='red',
    linestyle='dotted',
    linewidth=2,
    label='Set A Boundary (Square)'
)

# 3. Define and plot the ellipse boundary (Set B)
# We generate points for the ellipse using its parametric equations:
# a = h + a_radius * cos(t)
# b = k + b_radius * sin(t)
t = np.linspace(0, 2 * np.pi, 100) # Create 100 points from 0 to 2*pi
a_ellipse = 6 + 3 * np.cos(t)
b_ellipse = 5 + 2 * np.sin(t)
ax.plot(
    a_ellipse, b_ellipse,
    color='blue',
    linewidth=2,
    label='Set B Boundary (Ellipse)'
)


# 4. Define and mark the key points (centers and corners)
points_to_mark = {
    '(5, 5)': (5, 5),
    '(6, 5)': (6, 5),
    '(4, 4)': (4, 4),
    '(6, 4)': (6, 4),
    '(6, 6)': (6, 6),
    '(4, 6)': (4, 6)
}

# Extract coordinates for plotting markers
x_coords = [p[0] for p in points_to_mark.values()]
y_coords = [p[1] for p in points_to_mark.values()]

# Plot all points as black dots
ax.scatter(x_coords, y_coords, color='black', zorder=5, label='Centers & Corners')

# Add text labels next to each point with a slight offset for clarity
for label, (x, y) in points_to_mark.items():
    ax.text(x + 0.1, y + 0.1, label, fontsize=9, verticalalignment='bottom')

# 5. Formatting the plot for clarity
ax.set_xlabel('a-axis')
ax.set_ylabel('b-axis')
ax.set_xlim(2, 10)
ax.set_ylim(2, 9)
ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend()

plt.savefig('../figs/fig.png')
# 6. Display the plot
plt.show()
