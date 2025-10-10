# 3D plot: perpendicular from P(0,1,2) to the X-axis with foot Q(0,0,0)
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (needed for 3D)

# Data
P = np.array([0.0, 1.0, 2.0])
Q = np.array([0.0, 0.0, 0.0])

# X-axis as a parametric line
t = np.linspace(-3, 3, 200)
x_axis = np.vstack([t, np.zeros_like(t), np.zeros_like(t)])

# Figure
fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(111, projection='3d')

# Plot X-axis, points, and perpendicular segment
ax.plot(x_axis[0], x_axis[1], x_axis[2], linewidth=2, label='X-axis')
ax.scatter(*P, s=60, label='P(0,1,2)')
ax.scatter(*Q, s=60, label='Q(0,0,0)')
ax.plot([P[0], Q[0]], [P[1], Q[1]], [P[2], Q[2]], linewidth=2, label='Perpendicular')

# Axes labels and view
ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
ax.view_init(elev=24, azim=-52)
ax.legend(loc='upper right')
ax.set_box_aspect((1.6, 1, 1))  # aspect ratio

# Save to figs folder for LaTeX include
os.makedirs('figs', exist_ok=True)
plt.tight_layout()
plt.savefig('figs/4.8.35_3d.png', dpi=300, bbox_inches='tight')
plt.show()
