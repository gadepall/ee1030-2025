import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given magnitudes
norm_a = 1
norm_b = 2
norm_c = 3

# Define vectors satisfying the problem's conditions
a = np.array([1.0, 0.0, 0.0])   # |a| = 1
b = np.array([0.5, 1.94, 0.0])  # |b| ≈ 2
c = np.array([0.5, -0.13, 2.96]) # |c| ≈ 3

# Calculate result vector
result = 3 * a - 2 * b + 2 * c

# Create figure and 3D axes
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

# Origin
origin = np.array([0, 0, 0])

# Plot vectors with arrows and annotations
def plot_vector(vec, color, label, text_offset):
    ax.quiver(*origin, *vec, color=color, arrow_length_ratio=0.1, linewidth=2)
    # Position the text slightly away from the vector tip
    text_pos = vec + text_offset
    ax.text(*text_pos, label, color=color, fontsize=12, weight='bold')

# Plot each vector with offsets to avoid clutter
plot_vector(a, 'red', 'a (1.00, 0.00, 0.00)', np.array([0.2, 0, 0]))
plot_vector(b, 'blue', 'b (0.50, 1.94, 0.00)', np.array([0.2, 0.2, 0]))
plot_vector(c, 'green', 'c (0.50, -0.13, 2.96)', np.array([0.2, -0.2, 0.2]))
plot_vector(result, 'magenta', f'result {tuple(np.round(result, 2))}', np.array([0.3, 0.3, 0.3]))

# Set labels
ax.set_xlabel('X axis', fontsize=12)
ax.set_ylabel('Y axis', fontsize=12)
ax.set_zlabel('Z axis', fontsize=12)

# Set a viewing angle to separate vectors
ax.view_init(elev=20, azim=30)

# Set equal aspect ratio dynamically
max_range = np.array([a, b, c, result]).ptp(axis=0).max() / 2.0
mid_x = (np.max([a[0], b[0], c[0], result[0]]) + np.min([a[0], b[0], c[0], result[0]])) * 0.5
mid_y = (np.max([a[1], b[1], c[1], result[1]]) + np.min([a[1], b[1], c[1], result[1]])) * 0.5
mid_z = (np.max([a[2], b[2], c[2], result[2]]) + np.min([a[2], b[2], c[2], result[2]])) * 0.5

ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

# Add grid and title
ax.grid(True)
ax.set_title("3D Vector Visualization", fontsize=16, weight='bold')

# Add legend manually using empty plots
ax.plot([], [], [], color='red', label='Vector a')
ax.plot([], [], [], color='blue', label='Vector b')
ax.plot([], [], [], color='green', label='Vector c')
ax.plot([], [], [], color='magenta', label='Result vector')

ax.legend(loc='upper left')

# Save the figure with high resolution
plt.savefig("vector_plot_clean.png", dpi=300, bbox_inches='tight')

# Show plot
plt.show()

