# hyperbola.py
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

# Parameterize hyperbola branches
t = np.linspace(-3, 3, 400)
x1 = h + a * np.cosh(t); y1 = k + b * np.sinh(t)
x2 = h - a * np.cosh(t); y2 = k + b * np.sinh(t)
x3 = h + a * np.cosh(t); y3 = k - b * np.sinh(t)
x4 = h - a * np.cosh(t); y4 = k - b * np.sinh(t)

plt.figure(figsize=(10,10))
plt.plot(x1, y1, color='purple', linewidth=2)
plt.plot(x2, y2, color='purple', linewidth=2, label='Hyperbola')
plt.plot(x3, y3, color='purple', linewidth=2)
plt.plot(x4, y4, color='purple', linewidth=2)
plt.scatter([F1[0], F2[0]], [F1[1], F2[1]], color='red', s=50, label='Foci')
plt.scatter([h - a, h + a], [k, k], color='black', s=50, label='Vertices')
plt.axvline(d1, color='green', linestyle='--', linewidth=1.5, label='Directrices')
plt.axvline(d2, color='green', linestyle='--', linewidth=1.5)

# Set limits with margin
x_extent = c + a
y_extent = b * 3
plt.xlim(h - x_extent - 3, h + x_extent + 3)
plt.ylim(k - y_extent - 3, k + y_extent + 3)

plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.title('Hyperbola', fontsize=16)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.legend(loc='upper right', fontsize=12, framealpha=0.8)
plt.gca().set_aspect('equal', 'box')
plt.tight_layout()
plt.savefig('fig3.png', dpi=300)

