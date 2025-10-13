import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Vector components
a, b, c = 3, -2, 6
v = np.array([a, b, c])

# Magnitude of vector
magnitude = np.linalg.norm(v)

# Direction cosines
cos_alpha = a / magnitude
cos_beta  = b / magnitude
cos_gamma = c / magnitude

# Direction angles in degrees
alpha = np.degrees(np.arccos(cos_alpha))
beta  = np.degrees(np.arccos(cos_beta))
gamma = np.degrees(np.arccos(cos_gamma))

# Print direction cosines and angles
print(f"Direction cosines: ({cos_alpha:.2f}, {cos_beta:.2f}, {cos_gamma:.2f})")
print(f"Direction angles (degrees): α = {alpha:.2f}°, β = {beta:.2f}°, γ = {gamma:.2f}°")

# 3D Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the vector
ax.quiver(0, 0, 0, a, b, c, color='r', label='Vector v = 3i - 2j + 6k')

# Plot projections on axes
ax.quiver(0, 0, 0, a, 0, 0, color='blue', linestyle='dashed', label='x-component')
ax.quiver(0, 0, 0, 0, b, 0, color='green', linestyle='dashed', label='y-component')
ax.quiver(0, 0, 0, 0, 0, c, color='purple', linestyle='dashed', label='z-component')

# Annotate angles with adjusted positions to avoid overlap
ax.text(a + 0.5, 0, 0, f'α = {alpha:.1f}°', color='blue', fontsize=10)
ax.text(0, b - 1.5, 0, f'β = {beta:.1f}°', color='green', fontsize=10)
ax.text(0, 0, c + 0.5, f'γ = {gamma:.1f}°', color='purple', fontsize=10)

# Axes limits
max_val = max(abs(a), abs(b), abs(c)) + 2
ax.set_xlim([0, max_val])
ax.set_ylim([min(0, b) - 3, max_val])
ax.set_zlim([0, max_val])

# Labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Direction Cosines and Angles of Vector 3i - 2j + 6k')
ax.legend()

plt.tight_layout()

# Save the figure
plt.savefig('direction_cosines_vector.png', dpi=300)
print("Plot saved as 'direction_cosines_vector.png'")

plt.show()

