import sys
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from libs.line.funcs import *
from libs.triangle.funcs import *
from libs.conics.funcs import circ_gen

import subprocess
import shlex

print('Using termux?(y/n)')
y = input()

A = np.array([-4, 6]).reshape(-1, 1)
B = np.array([-4, -6]).reshape(-1, 1)
C = np.array([-4, 2]).reshape(-1, 1)

collinearity_matrix = np.column_stack([B-A, C-A]).T
rank = LA.matrix_rank(collinearity_matrix)

if(rank == 1):
    print('The given points are collinear as the rank of the collinearity matrix is 1')
else:
    print('The given points are not collinear as the rank of the collinearity matrix is not 1')

p_AB = line_gen(A, B)
p_AC = line_gen(A, C)
p_CB = line_gen(C, B)

plt.plot(p_AB[0, :], p_AB[1, :], label = 'Line through AB')
plt.plot(p_AC[0, :], p_AC[1, :], label = 'Line through AC')
plt.plot(p_CB[0, :], p_CB[1, :], label = 'Line through CB')

line_coords = np.block([[A,B,C]])
plt.scatter(line_coords[0,:], line_coords[1,:])
vert_labels = ['A','B','C']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, 
                 (line_coords[0,i], line_coords[1,i]),
                 textcoords="offset points", 
                 xytext=(0,10),
                 ha='center')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')

plt.savefig('../figs/fig.png')
print('Saved figure to ../figs/fig.png')

if(y == 'y'):
    subprocess.run(shlex.split('termux-open ../figs/fig.png'))
else:
    subprocess.run(["open",  "../figs/fig.png"])

