import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os
import sys

D1 = np.array([1, 1, 1], dtype=np.float64)
k1 = 6.0
D2 = np.array([0, 1, 3], dtype=np.float64)
k2 = 11.0
D3 = np.array([1, -2, 1], dtype=np.float64)
k3 = 0.0

A = np.block([[D1], [D2], [D3]])
b = np.array([k1, k2, k3])

P = np.linalg.solve(A, b)

x_vals = np.linspace(-5, 5, 50)
y_vals = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x_vals, y_vals)
Z1 = (k1 - D1[0]*X - D1[1]*Y) / D1[2]
Z2 = (k2 - D2[0]*X - D2[1]*Y) / D2[2]
Z3 = (k3 - D3[0]*X - D3[1]*Y) / D3[2]

fig = plt.figure(figsize=(10, 8))
ax = plt.axes(projection='3d')

ax.plot_surface(X, Y, Z1, color='blue', alpha=0.5)
ax.plot_surface(X, Y, Z2, color='cyan', alpha=0.5)
ax.plot_surface(X, Y, Z3, color='yellow', alpha=0.5)

ax.scatter(P[0], P[1], P[2], color='black', s=100)
ax.text(P[0], P[1], P[2], f'        P {tuple(P)}', color='black')

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.set_title('The Planes and their Solution')
ax.view_init(-5,108)
plt.grid()
plt.tight_layout()

plt.savefig("../figs/plot_p.jpg")
plt.show()
