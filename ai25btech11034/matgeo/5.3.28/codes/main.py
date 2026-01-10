# main.py

import ctypes
import numpy as np
import matplotlib.pyplot as plt
import os

# -----------------------------
# 1. Load C library
# -----------------------------
lib = ctypes.CDLL("./function.so")

# Define argument types for rref
lib.rref.argtypes = [ctypes.c_int, ctypes.c_int,
                     np.ctypeslib.ndpointer(dtype=np.float64, ndim=2, flags='C_CONTIGUOUS')]

# -----------------------------
# 2. Define augmented matrix
# -----------------------------
# x - y + z = 4
# x - 2y - 2z = 9
# 2x + y + 3z = 1
aug = np.array([
    [1, -1, 1, 4],
    [1, -2, -2, 9],
    [2, 1, 3, 1]
], dtype=np.float64)

rows, cols = aug.shape

# -----------------------------
# 3. Call C RREF function
# -----------------------------
lib.rref(rows, cols, aug)

print("RREF matrix from C function:")
print(aug)

# Extract solution from last column (since system is 3x3)
solution = aug[:, -1]
print("Intersection point (x, y, z):", solution)

# -----------------------------
# 4. Plotting planes
# -----------------------------
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Meshgrid
x_range = np.linspace(solution[0]-5, solution[0]+5, 25)
y_range = np.linspace(solution[1]-5, solution[1]+5, 25)
xx, yy = np.meshgrid(x_range, y_range)

# Plane equations
z1 = 4 - xx + yy
z2 = (xx - 2*yy - 9)/2
z3 = (1 - 2*xx - yy)/3

# Plot planes
ax.plot_surface(xx, yy, z1, alpha=0.3, color='salmon')
ax.plot_surface(xx, yy, z2, alpha=0.3, color='lightgreen')
ax.plot_surface(xx, yy, z3, alpha=0.3, color='skyblue')

# Plot intersection point
ax.scatter(solution[0], solution[1], solution[2], color='red', s=120)
ax.text(solution[0], solution[1], solution[2],
        f'  P({solution[0]:.2f},{solution[1]:.2f},{solution[2]:.2f})',
        color='red', fontsize=12, fontweight='bold')

# Labels and view
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Intersection of Three Planes')
ax.view_init(elev=35, azim=50)

# Legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='salmon', edgecolor='k', label='Plane 1: x - y + z = 4'),
    Patch(facecolor='lightgreen', edgecolor='k', label='Plane 2: x - 2y - 2z = 9'),
    Patch(facecolor='skyblue', edgecolor='k', label='Plane 3: 2x + y + 3z = 1'),
    Patch(facecolor='red', edgecolor='k', label='Intersection Point')
]
ax.legend(handles=legend_elements, loc='upper left')

# -----------------------------
# 5. Save figure
# -----------------------------
save_path = os.path.join("..", "figures", "planes_intersection_c.png")
plt.savefig(save_path)
print(f"Figure saved at: {save_path}")

plt.show()

