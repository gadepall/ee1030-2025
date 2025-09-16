import sys
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

from libs.line.funcs import *
from libs.triangle.funcs import *
from libs.conics.funcs import circ_gen

import subprocess
import shlex

print('Using termux?(y/n)')
y = input()

A = np.array([3/2, 3*math.sqrt(3)/2]).reshape(-1, 1)
B = np.array([0, 0]).reshape(-1, 1)
C = np.array([5, 0]).reshape(-1, 1)
D = np.array([13/2, 3*math.sqrt(3)/2]).reshape(-1,1)

p_A = line_gen(A, B)
p_B = line_gen(B, C)
p_C = line_gen(C, D)
p_D = line_gen(D, A)
p_BD = line_gen(B, D)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(p_A[0, :], p_A[1, :], label = 'Line AB')
ax.plot(p_B[0, :], p_B[1, :], label = 'Line BC')
ax.plot(p_C[0, :], p_C[1, :], label = 'Line CD')
ax.plot(p_D[0, :], p_D[1, :], label = 'Line DA')
ax.plot(p_BD[0, :], p_BD[1, :], label = 'Line BD')

pts = np.block([A, B, C, D])
names = ['A', 'B', 'C', 'D']
for i in range(4):
    X = pts[:, i]
    ax.text(X[0], X[1], s=f'{names[i]}({round(X[0], 3)}, {round(X[1],3)})')

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.legend(loc='best')
ax.grid(True) 
ax.axis('equal')
ax.set_xlim([-5, 10])
ax.set_ylim([-5, 10])

fig.savefig('../figs/fig.png')
print('Saved figure to ../figs/fig.png')

if(y == 'y'):
    subprocess.run(shlex.split('termux-open ../figs/fig.png'))
else:
    subprocess.run(["open",  "../figs/fig.png"])

