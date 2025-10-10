import sys
import math
sys.path.insert(0, '/home/sai-sreevallabh/Matrix_Theory/Matgeo/codes/CoordGeo')
import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA

#local imports
from line.funcs import *

A = np.array([1,3])
B = np.array([4,5])

k = -(A[1])/(B[1])

x = (A[0] + k*B[0])/(k+1)

x = np.round(x,1)

P = np.array([x,0.0])

A = A.reshape(-1,1)
B = B.reshape(-1,1)
P = P.reshape(-1,1)

x_PB = line_gen_num(P, B, 20)
plt.plot(x_PB[0,:],x_PB[1,:], color='green', label="Line Segment AB (Extended to P)")

plot_coords = np.block([[A, B, P]])
plt.scatter(plot_coords[0,:], plot_coords[1,:], color='red')

vert_labels = [
    f'A({A[0,0]}, {A[1,0]})',
    f'B({B[0,0]}, {B[1,0]})',
    f'P({P[0,0]:.2f}, {P[1,0]})'
]

for i, txt in enumerate(vert_labels):
    plt.annotate(txt,
            (plot_coords[0,i], plot_coords[1,i]),
            textcoords="offset points",
            xytext=(0,10),
            ha='center')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title("Line Segment AB Divided by X-axis")
plt.legend(loc='upper left')
plt.grid()
plt.axis('equal')

plt.savefig("../Figs/plot(py).png")
plt.show()
