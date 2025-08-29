import sys 
import math
sys.path.insert(0, '/home/puniaditya/GitHub/matgeo/codes/CoordGeo')
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from line.funcs import *
from triangle.funcs import *

#if using termux
#import subprocess
#import shlex

def section_formula(A, B, k):
    return (1*A + k*B) / (k + 1)

A = np.array([5, -6]).reshape(-1, 1)
B = np.array([-1, -4]).reshape(-1, 1)

k=5

P = section_formula(A, B, k).reshape(-1,1)

x_AB = line_gen_num(A,B,20)
plt.plot(x_AB[0,:],x_AB[1,:], 'g--', label="Line Segment AB")

plot_coords = np.block([[A, B, P]])
plt.scatter(plot_coords[0,:], plot_coords[1,:], color='blue')

vert_labels = [
    f'A({A[0,0]}, {A[1,0]})',
    f'B({B[0,0]}, {B[1,0]})',
    f'P({P[0,0]}, {P[1,0]:.2f})'
]

for i, txt in enumerate(vert_labels):
    plt.annotate(txt,
            (plot_coords[0,i], plot_coords[1,i]),
            textcoords="offset points",
            xytext=(0,10),
            ha='center')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title("Line Segment AB Divided by Y-axis")
plt.legend(loc='best')
plt.grid()
plt.axis('equal')

plt.savefig("../figs/plot_p.jpg")
plt.show()
