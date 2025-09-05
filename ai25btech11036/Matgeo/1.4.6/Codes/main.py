# 3D visualization for A(4,2), B(8,4), P(2,1) in the z=0 plane
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 for 3D projection
import numpy as np

A = np.array([4, 2, 0])
B = np.array([8, 4, 0])
P = np.array([2, 1, 0])

# Line segment A->B
t_seg = np.linspace(0, 1, 100)
seg = (1 - t_seg)[:, None] * A + t_seg[:, None] * B

# Extension beyond A toward P (to show collinearity if outside the segment)
t_ext = np.linspace(-0.6, 0.0, 40)
ext = (1 - t_ext)[:, None] * A + t_ext[:, None] * B

fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(111, projection='3d')

# Segment and extension
ax.plot(seg[:, 0], seg[:, 1], seg[:, 2], linewidth=2)
ax.plot(ext[:, 0], ext[:, 1], ext[:, 2], linestyle='--', linewidth=1.5)

# Points
ax.scatter(A[0], A[1], A[2], s=60)
ax.scatter(B[0], B[1], B[2], s=60)
ax.scatter(P[0], P[1], P[2], s=60)

# Labels
ax.text(A[0], A[1], A[2], "  A(4,2)")
ax.text(B[0], B[1], B[2], "  B(8,4)")
ax.text(P[0], P[1], P[2], "