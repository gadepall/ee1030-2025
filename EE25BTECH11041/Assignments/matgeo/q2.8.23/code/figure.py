import numpy as np
import matplotlib.pyplot as plt

# Example direction cosines (2D projection)
l, m = 0.6, 0.8
dl, dm = 0.1, -0.05

# Vectors
v1 = np.array([l, m])
v2 = np.array([l+dl, m+dm])

# Normalize
v1_u = v1 / np.linalg.norm(v1)
v2_u = v2 / np.linalg.norm(v2)

# Compute their angles w.r.t x-axis
angle1 = np.arctan2(v1_u[1], v1_u[0])
angle2 = np.arctan2(v2_u[1], v2_u[0])

# Ensure correct order (draw smaller arc between them)
start_angle = min(angle1, angle2)
end_angle = max(angle1, angle2)

# Plot
fig, ax = plt.subplots(figsize=(6,6))

# Draw vectors
ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='b', label='(l, m)')
ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='r', label='(l+δl, m+δm)')

# Draw arc for angle θ
arc_radius = 0.3
arc_angles = np.linspace(start_angle, end_angle, 100)
arc_x = arc_radius * np.cos(arc_angles)
arc_y = arc_radius * np.sin(arc_angles)
ax.plot(arc_x, arc_y, 'k-')

# Label θ at midpoint of arc
mid_angle = (start_angle + end_angle) / 2
ax.text(0.35*np.cos(mid_angle), 0.35*np.sin(mid_angle), r'$\theta$', fontsize=14)

# Formatting
ax.set_xlim(0, 1.2)
ax.set_ylim(0, 1.2)
ax.set_aspect('equal')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Angle between Two Vectors in 2D")
ax.legend()
ax.grid(True)

# Save figure
plt.savefig("vectors.png", dpi=300)
plt.show()
