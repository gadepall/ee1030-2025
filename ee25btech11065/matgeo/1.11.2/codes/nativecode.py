import matplotlib.pyplot as plt
import numpy as np

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Coordinates of points P and Q
p = np.array([2, 1, -1])
q = np.array([4, 4, -7])

# Plot the points
# Plot P in blue
ax.scatter(p[0], p[1], p[2], color='blue', s=100, label='Point P (2, 1, -1)')
# Plot Q in red
ax.scatter(q[0], q[1], q[2], color='red', s=100, label='Point Q (4, 4, -7)')

# Add text labels next to the points for clarity
ax.text(p[0] + 0.3, p[1] + 0.3, p[2], 'P', size=15, zorder=1, color='k')
ax.text(q[0] + 0.3, q[1] + 0.3, q[2], 'Q', size=15, zorder=1, color='k')


# Calculate the vector PQ
vector_pq = q - p

# Plot the vector PQ starting from point P
# The quiver function plots arrows. We specify the start (p) and direction (vector_pq).
ax.quiver(p[0], p[1], p[2],
          vector_pq[0], vector_pq[1], vector_pq[2],
          color='green', length=np.linalg.norm(vector_pq),
          arrow_length_ratio=0.1, label='Vector PQ')

# --- Plotting Aesthetics ---

# Set labels for the axes
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)
ax.set_zlabel('Z-axis', fontsize=12)

# Set a title for the plot
ax.set_title('3D Plot of Points P, Q, and Vector PQ', fontsize=16)

# Set axis limits to ensure the plot is well-framed
ax.set_xlim([0, 6])
ax.set_ylim([0, 6])
ax.set_zlim([-8, 1])

# Add a grid for better visualization
ax.grid(True)

# Add a legend to identify the points and vector
ax.legend(fontsize=10)

# Invert the Z-axis to match the typical coordinate system view if needed
# ax.invert_zaxis()

# Show the plot
plt.show()

