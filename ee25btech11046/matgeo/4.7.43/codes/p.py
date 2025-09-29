import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os
import sys

D = np.array([5, 2, -7], dtype=np.float64)
P1 = np.array([1, -1, 3], dtype=np.float64)
P2 = np.array([3, 3, 3], dtype=np.float64)
k = -9.0

if ((D.T@P1-k)*(D.T@P2-k))<0:
    print('They lie on the opposite side of the plane.')

x_vals = np.linspace(-5, 5, 50)
y_vals = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x_vals, y_vals)
Z = (k - D[0]*X - D[1]*Y) / D[2]

fig = plt.figure(figsize=(10, 8))
ax = plt.axes(projection='3d')

ax.plot_surface(X, Y, Z, alpha=0.5)

ax.scatter(P1[0], P1[1], P1[2], color='blue', s=100)
ax.scatter(P2[0], P2[1], P2[2], color='red', s=100)
ax.text(P1[0], P1[1], P1[2], fr'  $P_1${tuple(P1)}', color='blue')
ax.text(P2[0], P2[1], P2[2], fr'  $P_2${tuple(P2)}', color='red')


ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.set_title(r'Points $P_1$, $P_2$ and Plane P')
ax.view_init(28,28)
plt.grid()
plt.tight_layout()

plt.savefig("../figs/plot_p.jpg")
plt.show()
