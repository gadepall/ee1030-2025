# plot_line_fig1.py
# Produces a 3D plot of the line through A = (2, -1, 4) with direction d = (1, 1, -2)
# Saves output as "line_fig1.png"

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Given point and direction
A = np.array([2, -1, 4])
d = np.array([1, 1, -2])

# Parameter t for the line
t = np.linspace(-5, 5, 400)
line = A.reshape(3,1) + np.outer(d, t)  # shape (3, len(t))

# Create 3D plot (no explicit Axes3D import required)
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')

# Plot the line
ax.plot(line[0], line[1], line[2], linewidth=2, label='Line through A in direction d')

# Mark the point A
ax.scatter([A[0]], [A[1]], [A[2]], s=60, label='Point A (2,-1,4)')

# Annotate point A
ax.text(A[0], A[1], A[2], '  A(2,-1,4)', fontsize=10)

# Axis labels
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Try to set equal aspect ratio (works on matplotlib >= 3.3)
try:
    ax.set_box_aspect([1,1,1])
except Exception:
    # Fallback: approximate equal aspect by setting limits manually
    all_pts = np.hstack((line, A.reshape(3,1)))
    mins = all_pts.min(axis=1) - 1
    maxs = all_pts.max(axis=1) + 1
    ax.set_xlim(mins[0], maxs[0])
    ax.set_ylim(mins[1], maxs[1])
    ax.set_zlim(mins[2], maxs[2])

ax.legend()

# Save image
out_path = Path('line_fig1.png')
plt.tight_layout()
plt.savefig(out_path, dpi=200)
plt.show()

print(f"Saved image to: {out_path.resolve()}")



