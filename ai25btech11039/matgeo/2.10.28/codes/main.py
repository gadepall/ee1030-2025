# 3D plot for |(a×b)·c| = |a||b||c|
# Uses matplotlib only; single plot; default colors.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Choose orthogonal a,b; let c be parallel to a×b
a = np.array([2.0, 0.0, 0.0])     # x-axis
b = np.array([0.0, 3.0, 0.0])     # y-axis (⊥ a)
axb = np.cross(a, b)              # z-axis direction
c = axb / np.linalg.norm(axb) * 4.0  # parallel to axb

# Numeric check of the equality
triple = abs(np.dot(np.cross(a, b), c))
prod = np.linalg.norm(a) * np.linalg.norm(b) * np.linalg.norm(c)
# triple == prod

# Parallelogram in the a–b plane for context
O = np.zeros(3); A = a; B = b; C = a + b
parallelogram = [O, A, C, B]

fig = plt.figure(figsize=(7,6))
ax = fig.add_subplot(111, projection='3d')

# Vectors
ax.quiver(0,0,0, *a, length=1, normalize=False)
ax.quiver(0,0,0, *b, length=1, normalize=False)
ax.quiver(0,0,0, *c, length=1, normalize=False)

# Parallelogram spanned by a and b
ax.add_collection3d(Poly3DCollection([parallelogram], alpha=0.2))

# Labels
ax.text(*A, r'$\vec a$', fontsize=12)
ax.text(*B, r'$\vec b$', fontsize=12)
ax.text(*c, r'$\vec c \parallel \vec a \times \vec b$', fontsize=11)

# ​:contentReference[oaicite:0]{index=0}​
