import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os
import sys

A = np.array([2, -3, -1], dtype=np.float64)
B = np.array([1, -1, 2], dtype=np.float64)
m = len(A)
n = np.array([3, 1, -1], dtype=np.float64)
c = -2

scale_factor = 3
line_points = np.array([A - 2 * scale_factor * B, A + scale_factor * B])

x_vals = np.linspace(-5, 5, 50)
y_vals = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x_vals, y_vals)
Z = (c - n[0]*X - n[1]*Y) / n[2]

fig = plt.figure(figsize=(10, 8))
ax = plt.axes(projection='3d')

ax.plot_surface(X, Y, Z, alpha=0.5)
ax.plot(line_points[:, 0], line_points[:, 1], line_points[:, 2], 'b-', label='Line L')

ax.scatter(A[0], A[1], A[2], color='blue', s=100)
ax.text(A[0], A[1], A[2], f'  A{tuple(A)}', color='blue')

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.set_title('Line L and Plane P')
ax.legend()
ax.view_init(28,28)
plt.grid()
plt.tight_layout()

plt.savefig("../figs/plot_p.jpg")
plt.show()

#if using termux
#plt.savefig('./fig.pdf')
#subprocess.run(shlex.split("termux-open fig.pdf"))

