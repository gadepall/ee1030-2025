import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os
import sys

norm = np.linalg.norm

isosceles = ctypes.CDLL('./isosceles.so')
isosceles.function.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]
isosceles.function.restype = None

a = np.array([7, -1], dtype=np.float64)
b = np.array([1, 1], dtype=np.float64)
p = np.array([1, -10], dtype=np.float64)

n1 = np.array([ - (a[1] / norm(a) + b[1] / norm(b)), a[0] / norm(a) + b[0] / norm(b)], dtype=np.float64)
n2 = np.array([ - (a[1] / norm(a) - b[1] / norm(b)), a[0] / norm(a) - b[0] / norm(b)], dtype=np.float64)

c1 = n1[0] * p[0] + n1[1] * p[1]
c2 = n2[0] * p[0] + n2[1] * p[1]

ca = -3.0
cb = 3.0

V_ab = np.linalg.solve(np.array([a, b]), np.array([ca, cb]))
V_an1 = np.linalg.solve(np.array([a, n1]), np.array([ca, c1]))
V_bn1 = np.linalg.solve(np.array([b, n1]), np.array([cb, c1]))
V_an2 = np.linalg.solve(np.array([a, n2]), np.array([ca, c2]))
V_bn2 = np.linalg.solve(np.array([b, n2]), np.array([cb, c2]))

plt.figure(figsize=(10, 10))

plt.plot([V_ab[0], V_an1[0]], [V_ab[1], V_an1[1]], 'k-', label=f' 7x - y + 3 = 0')
plt.plot([V_ab[0], V_bn1[0]], [V_ab[1], V_bn1[1]], 'k-', label=f' x + y - 3 = 0')
plt.plot([V_an1[0], V_bn1[0]], [V_an1[1], V_bn1[1]], 'r-', label=f' 3x + y + 7 = 0')
plt.plot([V_bn2[0], p[0]], [V_bn2[1], p[1]], 'r-', label=f' x - 3y = 31')

plt.scatter(p[0], p[1], color='blue', s=100, zorder=5)
plt.text(p[0], p[1], f'     P {tuple(p)}', color='blue')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Plot')
plt.grid()
plt.axhline()
plt.axvline()
plt.gca().set_aspect('equal', adjustable='box')
plt.legend(loc='best')
plt.tight_layout()

plt.savefig("../figs/plot_p.jpg")
plt.show()
