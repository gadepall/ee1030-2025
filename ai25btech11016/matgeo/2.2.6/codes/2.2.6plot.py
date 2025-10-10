import numpy as np
import matplotlib.pyplot as plt

# Vectors in 3D
a = np.array([2, -1, 1])
b = np.array([3, 4, -1])

# Normalize a → treat as new x-axis
u = a / np.linalg.norm(a)

# Remove component of b along u → gives orthogonal direction in plane
b_proj = b - np.dot(b, u) * u
v = b_proj / np.linalg.norm(b_proj)  # normalize → new y-axis

# 2D coordinates in this new basis
a_2d = np.array([np.dot(a, u), np.dot(a, v)])
b_2d = np.array([np.dot(b, u), np.dot(b, v)])

# Plot in 2D
plt.figure(figsize=(6,6))
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.quiver(0, 0, a_2d[0], a_2d[1], angles='xy', scale_units='xy', scale=1, color='r', label="a = (2,-1,1)")
plt.quiver(0, 0, b_2d[0], b_2d[1], angles='xy', scale_units='xy', scale=1, color='b', label="b = (3,4,-1)")

plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.gca().set_aspect('equal', adjustable='box')
plt.savefig("/sdcard/Matrix/ee1030-2025/ai25btech11016/Matgeo/2.2.6/figs/2.2.6.png")
plt.show()
