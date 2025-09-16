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

A = np.array([2, 3, -4]).reshape(-1, 1)
B = np.array([3, -4, -5]).reshape(-1, 1)
C = np.array([3, 2, -3]).reshape(-1, 1)
O = np.zeros(3).reshape(-1,1)

P = A+B+C

norm = LA.norm(P)

print(f'Norm of A+B+C = {norm}')

p_A = line_gen(O, A)
p_B = line_gen(O, B)
p_C = line_gen(O, C)
p_P = line_gen(O, P)

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot(p_A[0, :], p_A[1, :], p_A[2, :], label = 'Vector A')
ax.plot(p_B[0, :], p_B[1, :], p_B[2, :], label = 'Vector B')
ax.plot(p_C[0, :], p_C[1, :], p_C[2, :], label = 'Vector C')
ax.plot(p_P[0, :], p_P[1, :], p_P[2,:], label = 'Vector A+B+C')

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.legend(loc='best')
ax.grid(True) 
ax.axis('equal')
ax.set_xlim([-15, 10])
ax.set_ylim([-15, 10])
ax.set_zlim([-15, 10])

fig.savefig('../figs/fig.png')
print('Saved figure to ../figs/fig.png')

if(y == 'y'):
    subprocess.run(shlex.split('termux-open ../figs/fig.png'))
else:
    subprocess.run(["open",  "../figs/fig.png"])

