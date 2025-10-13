import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os
import sys
intersect = ctypes.CDLL('./intersect.so')
intersect.function.argtypes = [
     ctypes.POINTER(ctypes.c_double),
     ctypes.POINTER(ctypes.c_double),
     ctypes.POINTER(ctypes.c_double),
     ctypes.c_double,
     ctypes.POINTER(ctypes.c_double)
]
intersect.function.restype = None

p = np.array([3, -4, -5], dtype=np.float64)
m = np.array([-1, 1, 6], dtype=np.float64)
n = np.array([2, 1, 1], dtype=np.float64)
c = 7.0
x = np.zeros(3, dtype=np.float64)
P1 = np.array([3.5, 0, 0], dtype=np.float64)
P2 = np.array([0, 7, 0], dtype=np.float64)
P3 = np.array([0, 0, 7], dtype=np.float64)

intersect.function(
    p.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    m.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    n.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    c,
    x.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
)

scale_factor = 3
line_points = np.array([p - 0.5 * scale_factor * m, p + 1.5 * scale_factor * m])

x_vals = np.linspace(-5, 5, 50)
y_vals = np.linspace(-5, 8, 50)
X, Y = np.meshgrid(x_vals, y_vals)
Z = (c - n[0]*X - n[1]*Y) / n[2]

fig = plt.figure(figsize=(10, 8))
ax = plt.axes(projection='3d')

ax.plot_surface(X, Y, Z, alpha=0.5)
ax.plot(line_points[:, 0], line_points[:, 1], line_points[:, 2], 'g-', label='Line L')

ax.scatter(P1[0], P1[1], P1[2], color='red', s=100)
ax.scatter(P2[0], P2[1], P2[2], color='red', s=100)
ax.scatter(P3[0], P3[1], P3[2], color='red', s=100)
ax.scatter(x[0], x[1], x[2], color='blue', s=100)
ax.text(P1[0], P1[1], P1[2], fr'  $P_1${tuple(P1)}', color='red')
ax.text(P2[0], P2[1], P2[2], fr'  $P_2${tuple(P2)}', color='red')
ax.text(P3[0], P3[1], P3[2], fr'  $P_3${tuple(P3)}', color='red')
ax.text(x[0], x[1], x[2], f'  x {tuple(x)}', color='blue')

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.set_title('Line L and Plane P')
ax.view_init(-19,-25)
plt.grid()
plt.tight_layout()
plt.legend()

plt.savefig("../figs/plot_c.jpg")
plt.show()
