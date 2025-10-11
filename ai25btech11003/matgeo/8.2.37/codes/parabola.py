# parabola_improved.py

import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library and parameters
lib = ctypes.CDLL('./main.so')
lib.get_parabola_params.argtypes = (ctypes.POINTER(ctypes.c_double),)
params = (ctypes.c_double * 3)()
lib.get_parabola_params(params)

h, k, p = params

# Focus and directrix
F = (h + p, k)
directrix_x = h - p

# Vertex
V = (h, k)

# Parameterize x so that (x - h) ≥ 0
x = np.linspace(h, h + 4 * p, 500)
y = np.sqrt(4 * p * (x - h))
y_neg = -y

plt.figure(figsize=(12, 10))

# Parabola branches
plt.plot(x, y, color='red', linewidth=2, label='Parabola')
plt.plot(x, y_neg, color='red', linewidth=2)

# Plot and label vertex
plt.scatter([V[0]], [V[1]], color='black', s=80, label='Vertex', zorder=5)
plt.text(V[0]-0.5, V[1]+1, f'V({V[0]:.1f},{V[1]:.1f})', fontsize=12, fontweight='bold', ha='center')

# Plot and label focus
plt.scatter([F[0]], [F[1]], color='blue', s=80, label='Focus', zorder=5)
plt.text(F[0]+0.5, F[1]+1, f'F({F[0]:.1f},{F[1]:.1f})', color='blue', fontsize=12, fontweight='bold', ha='center')

# Plot and label directrix
plt.axvline(directrix_x, color='green', linestyle='--', linewidth=2, label='Directrix')

# Calculate appropriate y-position for directrix label
y_max = np.max(y) + 2
plt.text(directrix_x, y_max - 1, f'x = {directrix_x:.1f}', color='green', fontsize=12, fontweight='bold', ha='center',
         bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen", alpha=0.7))

# Axes through origin
plt.axhline(0, color='gray', linewidth=0.8, alpha=0.7)
plt.axvline(0, color='gray', linewidth=0.8, alpha=0.7)

# Adjust limits with margins
x_min, x_max = h - 3, h + 5 * p + 1
y_max_plot = np.max(y) + 3
plt.xlim(x_min, x_max)
plt.ylim(-y_max_plot, y_max_plot)

# Grid for better visualization
plt.grid(True, alpha=0.3)

# Title and labels
plt.title('Parabola with its Vertex, Focus, and Directrix', fontsize=16, fontweight='bold')
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)

# Legend in top-right without overlapping
plt.legend(loc='upper right', fontsize=12, framealpha=0.9)

# Equal aspect and layout
plt.gca().set_aspect('equal', 'box')
plt.tight_layout()

# Save figure
plt.savefig('fig2.png', dpi=300, bbox_inches='tight')
plt.show()
