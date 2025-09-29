# hyperbola_improved.py

import ctypes, numpy as np, matplotlib.pyplot as plt

lib = ctypes.CDLL('./main.so')
lib.get_hyperbola_params.argtypes = (ctypes.POINTER(ctypes.c_double),)
params = (ctypes.c_double * 4)()
lib.get_hyperbola_params(params)

h, k, a, b = params

# Focus and directrices
e = np.sqrt(1 + (b/a)**2)
c = a * e

F1, F2 = (h - c, k), (h + c, k)
d1, d2 = h - a/e, h + a/e

# Calculate vertices
V1, V2 = (h - a, k), (h + a, k)

# Parameterize hyperbola branches
t = np.linspace(-3, 3, 400)
x1 = h + a * np.cosh(t); y1 = k + b * np.sinh(t)
x2 = h - a * np.cosh(t); y2 = k + b * np.sinh(t)
x3 = h + a * np.cosh(t); y3 = k - b * np.sinh(t)
x4 = h - a * np.cosh(t); y4 = k - b * np.sinh(t)

plt.figure(figsize=(12,10))

# Plot hyperbola branches
plt.plot(x1, y1, color='purple', linewidth=2, label='Hyperbola')
plt.plot(x2, y2, color='purple', linewidth=2)
plt.plot(x3, y3, color='purple', linewidth=2)
plt.plot(x4, y4, color='purple', linewidth=2)

# Plot and label vertices
plt.scatter([V1[0], V2[0]], [V1[1], V2[1]], color='black', s=80, label='Vertices', zorder=5)
plt.text(V1[0]-0.5, V1[1]+1, f'V₁({V1[0]:.1f},{V1[1]:.1f})', fontsize=12, fontweight='bold', ha='center')
plt.text(V2[0]+0.5, V2[1]+1, f'V₂({V2[0]:.1f},{V2[1]:.1f})', fontsize=12, fontweight='bold', ha='center')

# Plot and label foci
plt.scatter([F1[0], F2[0]], [F1[1], F2[1]], color='red', s=80, label='Foci', zorder=5)
plt.text(F1[0]-1, F1[1]-1.5, f'F₁({F1[0]:.1f},{F1[1]:.1f})', color='red', fontsize=12, fontweight='bold', ha='center')
plt.text(F2[0]+1, F2[1]-1.5, f'F₂({F2[0]:.1f},{F2[1]:.1f})', color='red', fontsize=12, fontweight='bold', ha='center')

# Plot and label directrices
plt.axvline(d1, color='green', linestyle='--', linewidth=2, label='Directrices')
plt.axvline(d2, color='green', linestyle='--', linewidth=2)

# Calculate appropriate y-position for directrix labels
y_extent = b * 3
directrix_label_y = k + y_extent - 2

plt.text(d1, directrix_label_y, f'x = {d1:.1f}', color='green', fontsize=12, fontweight='bold', ha='center',
         bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen", alpha=0.7))
plt.text(d2, directrix_label_y, f'x = {d2:.1f}', color='green', fontsize=12, fontweight='bold', ha='center',
         bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen", alpha=0.7))

# Set limits with margin
x_extent = c + a
y_extent = b * 3
plt.xlim(h - x_extent - 3, h + x_extent + 3)
plt.ylim(k - y_extent - 3, k + y_extent + 3)

# Axes through origin
plt.axhline(0, color='gray', linewidth=0.8, alpha=0.7)
plt.axvline(0, color='gray', linewidth=0.8, alpha=0.7)

# Grid for better visualization
plt.grid(True, alpha=0.3)

plt.title('Hyperbola with its Vertices, Foci, and Directrices', fontsize=16, fontweight='bold')
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.legend(loc='upper right', fontsize=12, framealpha=0.9)
plt.gca().set_aspect('equal', 'box')
plt.tight_layout()
plt.savefig('fig3.png', dpi=300, bbox_inches='tight')
plt.show()
