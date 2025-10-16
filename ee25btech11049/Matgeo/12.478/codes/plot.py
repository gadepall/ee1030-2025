import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Problem Data based on the image
# Using NumPy arrays for vector operations
force_P = np.array([2, -5, 6])
position_A = np.array([6, 1, -3])
position_B = np.array([4, -3, -2])

# --- Calculation using NumPy ---

# 1. Calculate the displacement vector (d = B - A)
# NumPy allows for direct vector subtraction.
displacement = position_B - position_A

# 2. Calculate the work done (Work = Force · Displacement)
# Using the dot product function from NumPy.
work_done = np.dot(force_P, displacement)

# --- Output the result ---
print(f"Force Vector (P): {force_P}")
print(f"Position Vector (A): {position_A}")
print(f"Position Vector (B): {position_B}")
print("-" * 20)
print(f"Calculated Displacement Vector (d): {displacement}")
print(f"Work Done: {work_done} Joules")


# --- 3D Visualization ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotting points A and B
ax.scatter(*position_A, color='blue', s=100, label='Point A')
ax.scatter(*position_B, color='red', s=100, label='Point B')

# Drawing vectors using quiver
# Origin for vectors
origin = [0, 0, 0]

# Position vectors from origin
ax.quiver(*origin, *position_A, color='cyan', arrow_length_ratio=0.1, label='Position Vector A')
ax.quiver(*origin, *position_B, color='magenta', arrow_length_ratio=0.1, label='Position Vector B')

# Displacement vector from A to B
ax.quiver(*position_A, *displacement, color='green', arrow_length_ratio=0.1, label='Displacement Vector (d)')

# Force vector acting on the particle (shown at point A for context)
ax.quiver(*position_A, *force_P, color='orange', arrow_length_ratio=0.1, label='Force Vector (P)')


# Setting plot labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Visualization of Force and Displacement')

# Setting axis limits to be equal for a better aspect ratio
max_val = np.max(np.abs(np.concatenate(([0], position_A, position_B, position_A + force_P))))
ax.set_xlim([-max_val, max_val])
ax.set_ylim([-max_val, max_val])
ax.set_zlim([-max_val, max_val])


ax.legend()
ax.grid(True)

# Show plot
plt.show()


