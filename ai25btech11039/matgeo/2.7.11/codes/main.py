# Q 2.7.11 – 2D plot of triangle ABC and area via shoelace formula
# Uses matplotlib only; single plot; default colors.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

A = np.array([1, -1], dtype=float)
B = np.array([-4, 6], dtype=float)
C = np.array([-3, -5], dtype=float)

# Area (shoelace)
pts = np.array([A, B, C, A])
area = 0.5 * abs(np.sum(pts[:-1,0]*pts[1:,1] - pts[:-1,1]*pts[1:,0]))

plt.figure(figsize=(6,6))

# Triangle polygon (default colors; no explicit color settings)
poly = Polygon([A, B, C], closed=True, fill=True, alpha=0.2, linewidth=2)
plt.gca().add_patch(poly)

# Edges and vertices
plt.plot([A[0], B[0]], [A[1], B[1]], linewidth=2)
plt.plot([B[0], C[0]], [B[1], C[1]], linewidth=2)
plt.plot([C[0], A[0]], [C[1], A[1]], linewidth=2)
plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]])
plt.text(A[0]+0.2, A[1]-0.2, 'A(1,-1)', fontsize=11)
plt.text(B[0]+0.2, B[1]+0.2, 'B(-4,6)', fontsize=11)
plt.text(C[0]+0.2, C[1]-0.4, 'C(-3,-5)', fontsize=11)

# Axes and layout
plt.axhline(0, linewidth=1); plt.axvline(0, linewidth=1)
plt.grid(True, linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
pad = 1.5
plt.xlim(min(A[0],B[0],C[0])-pad, max(A[0],B[0],C[0])+pad)
plt.ylim(min(A[1],B[1],C[1])-pad, max(A[1],B[1],C[1])+pad)
plt.title(f"Triangle ABC in 2D; Area = {area:.0f}")
plt.tight_layout()
plt.show()
