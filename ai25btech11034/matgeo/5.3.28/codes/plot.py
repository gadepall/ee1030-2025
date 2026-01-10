# plot.py

import numpy as np
import matplotlib.pyplot as plt
import os

# -----------------------------
# 1. Define the planes
# -----------------------------
A = np.array([
    [1, -1, 1],
    [1, -2, -2],  # x - 2y - 2z = 9
    [2, 1, 3]     # 2x + y + 3z = 1
], dtype=float)

b = np.array([4, 9, 1], dtype=float)

# Solve system
solution = np.linalg.solve(A, b)
print("Intersection point (x, y, z):", solution)

# -----------------------------
# 2. Prepare 3D plot
# -----------------------------
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Limit the plot range around the intersection for clarity
x_range = np.linspace(solution[0]-5, solution[0]+5, 25)
y_range = np.linspace(solution[1]-5, solution[1]+5, 25)
xx, yy = np.meshgrid(x_range, y_range)

# Plane equations
z1 = 4 - xx + yy         # Plane 1: x - y + z = 4
z2 = (xx - 2*yy - 9)/2   # Plane 2: x - 2y - 2z = 9
z3 = (1 - 2*xx - yy)/3   # Plane 3: 2x + y + 3z = 1

# Plot planes with light transparency
ax.plot_surface(xx, yy, z1, alpha=0.3, color='salmon')
ax.plot_surface(xx, yy, z2, alpha=0.3, color='lightgreen')
ax.plot_surface(xx, yy, z3, alpha=0.3, color='skyblue')

# Plot intersection point with large bright marker
ax.scatter(solution[0], solution[1], solution[2], color='red', s=120)
ax.text(solution[0], solution[1], solution[2],
        f'  P({solution[0]:.2f},{solution[1]:.2f},{solution[2]:.2f})',
        color='red', fontsize=12, fontweight='bold')

# Labels
ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_zlabel('Z', fontsize=12)
ax.set_title('Intersection of Three Planes', fontsize=14, fontweight='bold')

# Viewing angle
ax.view_init(elev=35, azim=50)

# Legend for planes
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='salmon', edgecolor='k', label='Plane 1: x - y + z = 4'),
    Patch(facecolor='lightgreen', edgecolor='k', label='Plane 2: x - 2y - 2z = 9'),
    Patch(facecolor='skyblue', edgecolor='k', label='Plane 3: 2x + y + 3z = 1'),
    Patch(facecolor='red', edgecolor='k', label='Intersection Point')
]
ax.legend(handles=legend_elements, loc='upper left')

# -----------------------------
# 3. Save figure
# -----------------------------
save_path = os.path.join("..", "figures", "planes_intersection.png")
plt.savefig(save_path)
print(f"Figure saved at: {save_path}")

plt.show()

