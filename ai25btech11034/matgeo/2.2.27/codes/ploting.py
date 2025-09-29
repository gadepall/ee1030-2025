import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Line definitions
P1 = np.array([-3, 1, -3])   # Point on L1
d1 = np.array([3, 5, 4])     # Direction of L1

P2 = np.array([-1, 4, -5])   # Point on L2
d2 = np.array([1, 1, 2])     # Direction of L2

# --- Angle between lines ---
dot_product = np.dot(d1, d2)
magnitude = np.linalg.norm(d1) * np.linalg.norm(d2)
cos_theta = dot_product / magnitude
theta = np.degrees(np.arccos(cos_theta))

print(f"Angle between lines: {theta:.2f} degrees")

# --- Plotting ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate parameter values
t = np.linspace(-2, 2, 20)

# Line 1 points
L1_points = P1[:, None] + d1[:, None] * t
ax.plot(L1_points[0], L1_points[1], L1_points[2], label="Line 1", color="blue")

# Line 2 points
L2_points = P2[:, None] + d2[:, None] * t
ax.plot(L2_points[0], L2_points[1], L2_points[2], label="Line 2", color="red")

# Mark starting points
ax.scatter(*P1, color="blue", s=50)
ax.scatter(*P2, color="red", s=50)

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
ax.set_title(f"Angle = {theta:.2f}°")

# Save figure
import os

# Build the path: one folder out (..), then into figures/
save_path = os.path.join("..", "figures", "lines3d.png")

plt.savefig(save_path, dpi=150)

plt.show()

