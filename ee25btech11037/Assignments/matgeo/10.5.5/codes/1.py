import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
mat = ctypes.CDLL('./mat.so')
mat.tangent.restype = ctypes.c_double
mat.tangent.argtypes = [ctypes.c_float, ctypes.c_float]

# Radii
r_small = 4.0
r_large = 6.0

# Compute tangent length from C
PT = mat.tangent(ctypes.c_float(r_large), ctypes.c_float(r_small))
PO = r_large
TO = r_small

# Geometry
O = np.array([0, 0])
P = np.array([r_large, 0])

# Find tangent point T using right triangle geometry
theta = np.arccos(r_small / r_large)
T = np.array([r_small * np.cos(theta), r_small * np.sin(theta)])

# Circles
theta_vals = np.linspace(0, 2*np.pi, 400)
x_small = r_small * np.cos(theta_vals)
y_small = r_small * np.sin(theta_vals)
x_large = r_large * np.cos(theta_vals)
y_large = r_large * np.sin(theta_vals)

plt.figure(figsize=(7,7))
plt.plot(x_small, y_small, 'b', label='Smaller Circle (r=4)')
plt.plot(x_large, y_large, 'g', label='Larger Circle (r=6)')

# Draw triangle lines
plt.plot([O[0], P[0]], [O[1], P[1]], 'k--', label='PO')
plt.plot([O[0], T[0]], [O[1], T[1]], 'k--', label='TO')
plt.plot([P[0], T[0]], [P[1], T[1]], 'r-', linewidth=2, label='Tangent PT')

# Mark points
plt.scatter(*O, color='k')
plt.scatter(*P, color='r')
plt.scatter(*T, color='m')

# Labels
plt.text(O[0]-0.3, O[1]-0.3, 'O', fontsize=12)
plt.text(P[0]+0.2, P[1], 'P', fontsize=12, color='r')
plt.text(T[0]+0.2, T[1]+0.2, 'T', fontsize=12, color='m')

# Length labels
plt.text(2, 0.3, f"TO = {TO}", fontsize=11, color='blue')
plt.text(3.2, 2, f"PT = {PT:.2f}", fontsize=11, color='red')
plt.text(3, -0.8, f"PO = {PO}", fontsize=11, color='green')

plt.gca().set_aspect('equal', adjustable='box')
plt.axhline(0, color='k', linewidth=0.5)
plt.axvline(0, color='k', linewidth=0.5)

# Legend outside
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.title("Tangent from P to Smaller Circle")
plt.tight_layout()
plt.savefig('1.png')
plt.show()

