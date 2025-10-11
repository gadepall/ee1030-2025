# ellipse_improved.py

import ctypes, numpy as np, matplotlib.pyplot as plt

# Load compiled library
lib = ctypes.CDLL('./main.so')
lib.get_ellipse_params.argtypes = (ctypes.POINTER(ctypes.c_double),)
params = (ctypes.c_double * 4)()
lib.get_ellipse_params(params)

h, k, a, b = params

# Compute focus distance & directrices
e = np.sqrt(1 - (b/a)**2)
c = a * e

F1, F2 = (h - c, k), (h + c, k)
d1, d2 = h - a/e, h + a/e

# Calculate vertices
V1, V2 = (h - a, k), (h + a, k)

# Parameterize ellipse
theta = np.linspace(0, 2*np.pi, 400)
x = h + a * np.cos(theta)
y = k + b * np.sin(theta)

plt.figure(figsize=(12,10))

# Plot ellipse
plt.plot(x, y, color='blue', linewidth=2, label='Ellipse')

# Plot and label vertices
plt.scatter([V1[0], V2[0]], [V1[1], V2[1]], color='black', s=80, label='Vertices', zorder=5)
plt.text(V1[0]-0.3, V1[1]+0.3, f'V₁({V1[0]:.1f},{V1[1]:.1f})', fontsize=12, fontweight='bold', ha='center')
plt.text(V2[0]+0.3, V2[1]+0.3, f'V₂({V2[0]:.1f},{V2[1]:.1f})', fontsize=12, fontweight='bold', ha='center')

# Plot and label foci
plt.scatter([F1[0], F2[0]], [F1[1], F2[1]], color='red', s=80, label='Foci', zorder=5)
plt.text(F1[0]-0.3, F1[1]-0.5, f'F₁({F1[0]:.1f},{F1[1]:.1f})', color='red', fontsize=12, fontweight='bold', ha='center')
plt.text(F2[0]+0.3, F2[1]-0.5, f'F₂({F2[0]:.1f},{F2[1]:.1f})', color='red', fontsize=12, fontweight='bold', ha='center')

# Plot and label directrices
plt.axvline(d1, color='green', linestyle='--', linewidth=2, label='Directrices')
plt.axvline(d2, color='green', linestyle='--', linewidth=2)
plt.text(d1, k + b + 1, f'x = {d1:.1f}', color='green', fontsize=12, fontweight='bold', ha='center', 
         bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen", alpha=0.7))
plt.text(d2, k + b + 1, f'x = {d2:.1f}', color='green', fontsize=12, fontweight='bold', ha='center',
         bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen", alpha=0.7))

# Set limits with margin
margin = 1.5
plt.xlim(h - a*margin - 2, h + a*margin + 2)
plt.ylim(k - b*margin - 2, k + b*margin + 2)

# Axes through origin
plt.axhline(0, color='gray', linewidth=0.8, alpha=0.7)
plt.axvline(0, color='gray', linewidth=0.8, alpha=0.7)

# Grid for better visualization
plt.grid(True, alpha=0.3)

plt.title('Ellipse with its Vertices, Foci, and Directrices', fontsize=16, fontweight='bold')
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.legend(loc='upper right', fontsize=12, framealpha=0.9)
plt.gca().set_aspect('equal', 'box')
plt.tight_layout()
plt.savefig('fig1.png', dpi=300, bbox_inches='tight')
plt.show()
