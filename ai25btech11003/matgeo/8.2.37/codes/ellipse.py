# elipse.py
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

# Parameterize ellipse
theta = np.linspace(0, 2*np.pi, 400)
x = h + a * np.cos(theta)
y = k + b * np.sin(theta)

plt.figure(figsize=(10,10))
plt.plot(x, y, color='blue', linewidth=2, label='Ellipse')
plt.scatter([F1[0], F2[0]], [F1[1], F2[1]], color='red', s=50, label='Foci')
plt.scatter([h - a, h + a], [k, k], color='black', s=50, label='Vertices')
plt.axvline(d1, color='green', linestyle='--', linewidth=1.5, label='Directrices')
plt.axvline(d2, color='green', linestyle='--', linewidth=1.5)

# Set limits with margin
margin = 1.2
plt.xlim(h - a*margin - 5, h + a*margin + 5)
plt.ylim(k - b*margin - 5, k + b*margin + 5)

# Axes through origin
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.title('Ellipse', fontsize=16)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.legend(loc='upper right', fontsize=12, framealpha=0.8)
plt.gca().set_aspect('equal', 'box')
plt.tight_layout()
plt.savefig('fig1.png', dpi=300)

