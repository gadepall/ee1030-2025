# 2D illustrative plot for |a x b| with vectors a and b.
# Uses matplotlib only (no seaborn), single plot, default colors.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Given vectors
a = np.array([2, 1, 3], dtype=float)
b = np.array([3, 5, -2], dtype=float)

# Cross product magnitude (true 3D area of parallelogram)
axb = np.cross(a, b)
area = np.linalg.norm(axb)  # = |a x b|

# 2D projection onto xy-plane for a clean diagram
a2 = a[:2]
b2 = b[:2]

# Parallelogram vertices in 2D
O = np.array([0.0, 0.0])
A = a2
B = b2
C = a2 + b2

plt.figure(figsize=(6, 6))

# Draw vectors from origin
plt.quiver(0, 0, A[0], A[1], angles='xy', scale_units='xy', scale=1)
plt.quiver(0, 0, B[0], B[1], angles='xy', scale_units='xy', scale=1)

# Draw the parallelogram spanned by a and b (2D projection)
poly = Polygon([O, A, C, B], closed=True, alpha=0.15)
plt.gca().add_patch(poly)

# Annotations
plt.text(A[0]*1.02, A[1]*1.02, r'$\vec a$', fontsize=12)
plt.text(B[0]*1.02, B[1]*1.02, r'$\vec b$', fontsize=12)
plt.text(C[0]*1.01, C[1]*1.01, r'$\vec a+\vec b$', fontsize=11)

# Axes and layout
plt.axhline(0, linewidth=1)
plt.axvline(0, linewidth=1)
plt.grid(True, linewidth=0.5)

max_x = max(abs(np.array([O[0], A[0], B[0], C[0]])).max(), 1)
max_y = max(abs(np.array([O[1], A[1], B[1], C[1]])).max(), 1)
pad = 1.5
plt.xlim(-max_x - pad, max_x + pad)
plt.ylim(-max_y - pad, max_y + pad)
plt.gca().set_aspect('equal', adjustable='box')

plt.title(r'2D Illustration (xy-projection): Parallelogram spanned by $\vec a$ and $\vec b$'+'\n'
          + rf'$|\vec a \times \vec b| = {area:.3f} \; (= 13\sqrt{{3}})$')

plt.tight_layout()
plt.show()
