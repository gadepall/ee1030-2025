import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import ctypes
import numpy.linalg as LA

c_lib=ctypes.CDLL("./code.so")

c_lib.Solve_for_x.argtypes = [
        ctypes.c_float,
        ctypes.c_float,
        ctypes.c_float,
        ctypes.c_float
        ]

c_lib.Solve_for_x.restype = ctypes.c_float


A= np.array([1,3]).reshape(-1,1)
B= np.array([4,5]).reshape(-1,1)

x = c_lib.Solve_for_x(
        ctypes.c_float(A[0]),
        ctypes.c_float(A[1]),
        ctypes.c_float(B[0]),
        ctypes.c_float(B[1])
        )

#P is the point on X-axis that divides the given line segment in the ratio k:1

P = np.array([x,0]).reshape(-1,1)

#x_PB = line_gen_num(P,B,20)

plt.plot([P[0,0], B[0,0]], [P[1,0], B[1,0]], label="Line Segment AB (Extended to P)")

plot_coords = np.block([[A, B, P]])
plt.scatter(plot_coords[0,:], plot_coords[1,:], color="red")


vert_labels = [
    f'A({A[0,0]}, {A[1,0]})',
    f'B({B[0,0]}, {B[1,0]})',
    f'P({P[0,0]:.2f}, {P[1,0]})'
]

for i, txt in enumerate(vert_labels):
    plt.annotate(txt,
            (plot_coords[0,i],plot_coords[1,i]),
            textcoords="offset points",
            xytext=(0,10),
            ha='center')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title("Line Segment AB Divided by X-axis")
plt.legend(loc='upper left')
plt.grid()
plt.axis('equal')

plt.savefig("../Figs/plot(py+C).png")

plt.show()
