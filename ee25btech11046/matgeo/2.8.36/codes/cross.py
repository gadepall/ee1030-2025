import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import ctypes

cross = ctypes.CDLL('/home/puniaditya/GitHub/ee1030-2025/ee25btech11046/matgeo/2.8.36/codes/cross.so')

cross.cross.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]
cross.cross.restype = None

cross.function.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]

cross.function.restype = ctypes.c_double

A = np.array([0, 1, 0], dtype=np.float64)
B = np.array([-1, 1, 0], dtype=np.float64)
P = np.zeros(3, dtype=np.float64)

cross.cross(
    A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    B.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    P.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
)

d = cross.function(
    A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    B.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
)

O = np.array([0, 0, 0])

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot([O[0], A[0]], [O[1], A[1]], [O[2], A[2]], 'r-', label=r'Vector $\vec{a}$')
ax.plot([O[0], B[0]], [O[1], B[1]], [O[2], B[2]], 'g-', label=r'Vector $\vec{b}$')
ax.plot([O[0], P[0]], [O[1], P[1]], [O[2], P[2]], 'b-', label=r'Vector $\vec{a}\times\vec{b}$')

ax.scatter(O[0], O[1], O[2], color='k', s=100)
ax.scatter(A[0], A[1], A[2], color='r', s=50)
ax.scatter(B[0], B[1], B[2], color='g', s=50)
ax.scatter(P[0], P[1], P[2], color='b', s=50)

ax.text(O[0] - 0.3, O[1] - 0.2, O[2], 'O (0,0,0)', color='k')
ax.text(A[0] + 0.1, A[1], A[2], f'({A[0]}, {A[1]}, {A[2]})', color='r')
ax.text(B[0] - 0.5, B[1], B[2], f'({B[0]}, {B[1]}, {B[2]})', color='g')
ax.text(P[0] + 0.1, P[1], P[2], f'({P[0]}, {P[1]}, {P[2]})', color='b')


ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.set_title('Plot')

ax.legend()
plt.grid(True)

ax.view_init(20,30)

plt.savefig("../figs/plot_c.jpg")
plt.show()
