# parabola.py
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

# Parameterize x so that (x - h) ≥ 0
x = np.linspace(h, h + 4 * p, 500)
y = np.sqrt(4 * p * (x - h))
y_neg = -y

plt.figure(figsize=(15, 10))
# Parabola branches
plt.plot(x, y, color='red', linewidth=2, label='Parabola')
plt.plot(x, y_neg, color='red', linewidth=2)

# Mark focus and vertex
plt.scatter([F[0]], [F[1]], color='red', s=50, label='Focus')
plt.scatter([h], [k], color='black', s=50, label='Vertex')

# Directrix line
plt.axvline(directrix_x, color='green', linestyle='--', linewidth=1.5, label='Directrix')

# Axes through origin
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Adjust limits with margins
x_min, x_max = h - 5, h + 5 * p + 1
y_max = np.max(y) + 5
plt.xlim(x_min, x_max)
plt.ylim(-y_max, y_max)

# Title and labels
plt.title('Parabola', fontsize=16)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)

# Legend in top-right without overlapping
plt.legend(loc='upper right', fontsize=12, framealpha=0.8)

# Equal aspect and layout
plt.gca().set_aspect('equal', 'box')
plt.tight_layout()

# Save figure
plt.savefig('fig2.png', dpi=300)

