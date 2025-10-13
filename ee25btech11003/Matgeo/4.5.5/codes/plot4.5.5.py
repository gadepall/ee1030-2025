import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- 1. Setup for the Plot ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# --- 2. Define the Line's Equation ---
# CHANGED: Increased t_range to extend the line
t_range = 20
t = np.linspace(-t_range, t_range, 200) # Increased points for a smooth line

# Base point h = (1, -2, 3)
h = np.array([1, -2, 3])
# Direction vector m = <3, -2, 6>
m = np.array([3, -2, 6])

# Parametric equations for the line
x_coords = h[0] + m[0] * t
y_coords = h[1] + m[1] * t
z_coords = h[2] + m[2] * t

# --- 3. Plot the Components ---
# Plot the line itself
ax.plot(x_coords, y_coords, z_coords, color='blue', linewidth=3, label='Line: $\\mathbf{x} = \\mathbf{h} + t\\mathbf{m}$')

# Plot the specific point h = (1, -2, 3)
ax.scatter(h[0], h[1], h[2], color='red', s=150, label='Point $\\mathbf{h}$ (1, -2, 3)', depthshade=True)

# Plot the direction vector m as a green arrow
ax.quiver(h[0], h[1], h[2],  # Starting point
          m[0], m[1], m[2],  # Direction
          color='green', arrow_length_ratio=0.15, linewidth=2, label='Direction vector $\\mathbf{m}$',
          length=np.linalg.norm(m) * 1.5)

# --- 4. Finalize the Plot ---
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)
ax.set_zlabel('Z-axis', fontsize=12)
ax.set_title('3D Plot of the Vector Equation of a Line (Extended)', fontsize=14)

ax.grid(True)

# Set an initial view angle
ax.view_init(elev=20, azim=-60)

ax.legend(fontsize=10, loc='lower right')
plt.tight_layout()
plt.show()
