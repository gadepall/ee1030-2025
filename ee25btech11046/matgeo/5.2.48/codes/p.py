import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os
import sys

D1 = np.array([1, 1, 1], dtype=np.float64)
k1 = 1.0
D2 = np.array([2, 3, 2], dtype=np.float64)
k2 = 2.0
D3 = np.array([2, 2, 4], dtype=np.float64)
k3 = 4.0

A = np.block([[D1], [D2], [D3]])
b = np.array([k1, k2, k3])

P = np.linalg.solve(A, b)

y_vals = np.linspace(-5, 5, 50)
z_vals = np.linspace(-5, 5, 50)
Y, Z = np.meshgrid(y_vals, z_vals)
X1 = (k1 - D1[1]*Y - D1[2]*Z) / D1[0]
X2 = (k2 - D2[1]*Y - D2[2]*Z) / D2[0]
X3 = (k3 - D3[1]*Y - D3[2]*Z) / D3[0]

fig = plt.figure(figsize=(10, 8))
ax = plt.axes(projection='3d')

ax.plot_surface(X1, Y, Z, color='blue', alpha=0.5)
ax.plot_surface(X2, Y, Z, color='cyan', alpha=0.5)
ax.plot_surface(X3, Y, Z, color='yellow', alpha=0.5)

ax.scatter(P[0], P[1], P[2], color='red', s=100)
ax.text(P[0], P[1], P[2], f'        P {tuple(P)}', color='red')


ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.set_title('The Planes and their Solution')
ax.view_init(-5,108)
plt.grid()
plt.tight_layout()

plt.savefig("../figs/plot_p.jpg")
plt.show()
