# plot_vectors.py
import matplotlib.pyplot as plt
import numpy as np

# Define vectors
a = np.array([1, 0])
b = np.array([1, np.sqrt(3)])

# Plot setup
fig, ax = plt.subplots()
ax.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy', scale=1, color='blue', label='a')
ax.quiver(0, 0, b[0], b[1], angles='xy', scale_units='xy', scale=1, color='orange', label='b')

# Angle annotation
angle_rad = np.arccos(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))
angle_deg = np.degrees(angle_rad)
ax.text(0.5, 0.2, f"$\\theta = {angle_deg:.0f}^\\circ$", fontsize=12)

# Formatting
ax.set_xlim(-1, 2)
ax.set_ylim(-1, 2)
ax.set_aspect('equal')
ax.grid(True)
ax.legend()
plt.title("Angle Between Vectors")
plt.show()

