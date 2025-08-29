import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import ctypes

problem = ctypes.CDLL('/home/ganachari-vishwmabhar/ee1030-2025/EE25BTECH11025/ASSIGNMENTS/matgeo/1.5.13/codes/problem.so')

problem.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_int,
    ctypes.c_int,
]
problem.restype = None  # void function

m = 2
k = 5

A = np.array([[5, -6]], dtype=np.float64)
B = np.array([[-1, -4]], dtype=np.float64)
P = np.zeros(m, dtype=np.float64)

problem.function(
    P.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    B.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    m, #len(P) alternate
    k
)

A = np.array([5, -6]).reshape(-1,1)
B = np.array([-1, -4]).reshape(-1,1)
P = P.reshape(-1,1)

plt.plot([A[0,0], B[0,0]], [A[1,0], B[1,0]], 'g--', label="Line Segment AB")

plot_coords = np.block([[A, B, P]])
plt.scatter(plot_coords[0,:], plot_coords[1,:], color='blue')

vert_labels = [
    f'A({A[0,0]}, {A[1,0]})',
    f'B({B[0,0]}, {B[1,0]})',
    f'P({P[0,0]}, {P[1,0]:.2f})'
]

for i, txt in enumerate(vert_labels):
    plt.annotate(txt,
            (plot_coords[0,i],plot_coords[1,i]),
            textcoords="offset points",
            xytext=(0,10),
            ha='center')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title("Line Segment AB Divided by Y-axis")
plt.legend(loc='best')
plt.grid()
plt.axis('equal')

plt.savefig("../figs/plot.png")
plt.show()
