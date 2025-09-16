import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import ctypes

triple_product = ctypes.CDLL('/home/puniaditya/GitHub/ee1030-2025/ee25btech11046/matgeo/2.10.74/codes/triple_product.so')

triple_product.function.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]

triple_product.function.restype = ctypes.c_double

A = np.array([1, -1, 0], dtype=np.float64)
B = np.array([1, 0, -1], dtype=np.float64)
C = np.array([0, 1, -1], dtype=np.float64)
X = np.array([1, 1, 1], dtype=np.float64)

tp = triple_product.function(
    A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    B.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    C.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    X.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
)

O = np.array([0, 0, 0])

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot([O[0], A[0]], [O[1], A[1]], [O[2], A[2]], 'r-', label=r'Vector $\vec{A}$')
ax.plot([O[0], B[0]], [O[1], B[1]], [O[2], B[2]], 'g-', label=r'Vector $\vec{B}$')
ax.plot([O[0], C[0]], [O[1], C[1]], [O[2], C[2]], 'b-', label=r'Vector $\vec{C}$')
ax.plot([O[0], X[0]], [O[1], X[1]], [O[2], X[2]], 'k-', label=r'Vector $\vec{X}$')

ax.scatter(O[0], O[1], O[2], color='k', s=100)
ax.scatter(A[0], A[1], A[2], color='r', s=50)
ax.scatter(B[0], B[1], B[2], color='g', s=50)
ax.scatter(C[0], C[1], C[2], color='b', s=50)
ax.scatter(X[0], X[1], X[2], color='k', s=50)

ax.text(O[0], O[1], O[2], f'({O[0]}, {O[1]}, {O[2]})', color='k')
ax.text(A[0], A[1], A[2], f'({A[0]}, {A[1]}, {A[2]})', color='r')
ax.text(B[0], B[1], B[2], f'({B[0]}, {B[1]}, {B[2]})', color='g')
ax.text(C[0], C[1], C[2], f'({C[0]}, {C[1]}, {C[2]})', color='b')
ax.text(X[0], X[1], X[2], f'({X[0]}, {X[1]}, {X[2]})', color='k')

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.set_title('Plot')

ax.legend()
plt.grid(True)

ax.view_init(25,-50)

plt.savefig("../figs/plot_c.jpg")
plt.show()
