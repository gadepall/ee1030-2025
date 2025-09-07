import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os
import sys

project_lib = ctypes.CDLL('./project.so')
project_lib.project.argtypes = [
        ctypes.POINTER(ctypes.c_double),
        ctypes.POINTER(ctypes.c_double),
        ctypes.POINTER(ctypes.c_double),
        ctypes.c_int
]

project_lib.project.restype = ctypes.c_double

#E = B+C

A=np.array([2, -2, 1], dtype=np.float64)
B=np.array([1, 2, -2], dtype=np.float64)
C=np.array([2, -1, 4], dtype=np.float64)
D=np.zeros(3, dtype=np.float64)
E=B+C

m=len(A)

project=project_lib.project(
        D.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        E.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        m
)


fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')

ax.quiver(0, 0, 0, E[0], E[1], E[2], color='b', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, A[0], A[1], A[2], color='r', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, D[0], D[1], D[2], color='g', arrow_length_ratio=0.2)

label = f'({A[0]}, {A[1]}, {A[2]})'
ax.text(A[0], A[1], A[2], s=label, color='b', fontsize=10)

label = f'({E[0]}, {E[1]}, {E[2]})'
ax.text(E[0], E[1], E[2], s=label, color='b', fontsize=10)

label = f'({D[0]}, {D[1]}, {D[2]})'
ax.text(D[0], D[1], D[2], s=label, color='b', fontsize=10)



ax.scatter(A[0], A[1], A[2], color='r', s=50)
ax.scatter(E[0], E[1], E[2], color='b', s=50)
ax.scatter(D[0], D[1], D[2], color='g', s=50)

ax.set_xlim([0, 4])
ax.set_ylim([-4, 4])
ax.set_zlim([-4, 4])

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

plt.title('Vector Projection')

plt.savefig('/home/shreyas/GVV_Assignments/matgeo/2.5.5/figs/fig1.png')

plt.show()
