import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os
import sys
norm = ctypes.CDLL('./norm.so')
norm.norm.argtypes = [
     ctypes.POINTER(ctypes.c_double),
     ctypes.c_int
]
norm.norm.restype = ctypes.c_double

O = np.array([0, 0], dtype=np.float64)
P = np.array([-6, 8], dtype=np.float64)
m = len(P)

d = norm.norm(
    P.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    m
)

plt.plot([O[0], P[0]], [O[1], P[1]], 'g-', label=f'distance = {d:.2f}')
plt.text(P[0]/2 + 0.2, P[1]/2, f'd = {d:.2f}', color='blue', fontsize=12)

plot_coords = np.array([O, P]).T
plt.scatter(plot_coords[0, :], plot_coords[1, :], color='blue')

vert_labels = [
    f'O({O[0]}, {O[1]})',
    f'P({P[0]}, {P[1]})'
]

for i, txt in enumerate(vert_labels):
    plt.annotate(txt, (plot_coords[0, i], plot_coords[1, i]),
                 textcoords="offset points", xytext=(0, 10), ha='center')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title("Point Vector P")
plt.legend(loc='best')
plt.grid()
plt.axis('equal')

plt.savefig("../figs/plot_c.jpg")
plt.show()
