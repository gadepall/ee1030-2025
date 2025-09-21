# Generates fig1.png with the y-axis on the cube's corner edge (x=0, z=0)

import numpy as np
import matplotlib
matplotlib.use("Agg")  # non-interactive backend for file output
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# ---- Parameters (edit as needed) ----
alpha = 2.0
beta  = 3.0
gamma = 1.5

# ---- Points ----
xA, yA, zA = float(alpha), float(beta), float(gamma)
xB, yB, zB = 0.0, float(beta), 0.0  # foot on y-axis

# ---- Figure/axes ----
fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(111, projection="3d")
ax.set_box_aspect((1, 1, 1))  # cubic box

# Choose a cube in the first octant so the y-axis is the corner edge
L = max(1.0, xA, yA, zA) + 1.0
ax.set_xlim(0.0, L)
ax.set_ylim(0.0, L)
ax.set_zlim(0.0, L)

# Helpful view to see the corner clearly
ax.view_init(elev=22, azim=-60)

# ---- Draw the y-axis along the corner edge (x=0, z=0) ----
y_line = np.linspace(0.0, L, 200)
ax.plot(np.zeros_like(y_line), y_line, np.zeros_like(y_line),
        color="k", linewidth=2)

# ---- Plot points A and B ----
ax.scatter([xA], [yA], [zA], color="crimson", s=60)
ax.scatter([xB], [yB], [zB], color="royalblue", s=60)

# ---- Dotted perpendicular AB ----
ax.plot([xA, xB], [yA, yB], [zA, zB],
        color="gray", linestyle=":", linewidth=2)

# ---- Labels/annotations ----
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.text(xA, yA, zA, r"$A(\alpha,\beta,\gamma)$", fontsize=10, color="crimson")
ax.text(xB, yB, zB, r"$B(0,\beta,0)$", fontsize=10, color="royalblue")

plt.tight_layout()
plt.savefig("fig1.png", dpi=200, bbox_inches="tight")
plt.close(fig)

