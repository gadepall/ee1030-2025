import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define vectors
a = np.array([3, 1, 2])
b = np.array([2, -2, 4])

# Compute angle
dot = np.dot(a, b)
mag_a = np.linalg.norm(a)
mag_b = np.linalg.norm(b)
cos_theta = dot / (mag_a * mag_b)
theta = np.degrees(np.arccos(cos_theta))

print(f"Angle between vectors = {theta:.2f} degrees")

# Create 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot vectors
ax.quiver(0, 0, 0, a[0], a[1], a[2], color='r', label='Vector a', linewidth=2, arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, b[0], b[1], b[2], color='b', label='Vector b', linewidth=2, arrow_length_ratio=0.1)

# Plot angle arc (fix broadcasting)
t = np.linspace(0, np.arccos(cos_theta), 100)
arc = (mag_a/2) * (np.cos(t)[:,None] * (a/mag_a) + np.sin(t)[:,None] * (b/mag_b))
ax.plot(arc[:,0], arc[:,1], arc[:,2], 'g--', label=f'Angle ≈ {theta:.2f}°')

# Labels and formatting
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.set_title("Angle Between Vectors a and b")

# Save figure
plt.savefig("vector_angle.png", dpi=300)   # Saves image
plt.show()

