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

A = np.array([273, 32]).reshape(-1, 1)
B = np.array([373, 212]).reshape(-1, 1)

K = np.block([A, B]).T
N = LA.solve(K, np.array([1, 1]).reshape(-1,1)).reshape(-1, 1)
R = np.array([1, 0]).reshape(-1, 1)
Q = np.block([N, R]).T
C = LA.solve(Q, np.array([1,0]).T).reshape(-1, 1)
p_AB = line_gen(A, B)
p_BC = line_gen(B, C)
p_CA = line_gen(C, A)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(p_BC[0, :], p_BC[1, :])
ax.plot(p_CA[0, :], p_CA[1, :], label = 'Line CA')
ax.plot(p_AB[0, :], p_AB[1, :], label = 'Line AB')

pts = np.block([A, B, C])
names = ['A', 'B', 'C']
for i in range(3):
    Z = pts[:, i]
    ax.text(Z[0], Z[1], s=f'{names[i]}({round(Z[0], 3)}, {round(Z[1],3)})')

ax.set_xlabel('$K(Kelvin)$')
ax.set_ylabel('$F(Fahrenheit$')
ax.legend(loc='best')
ax.grid(True) 
ax.axis('equal')
ax.set_xlim([-200, 800])
ax.set_ylim([-500, 300])

fig.savefig('../figs/fig.png')
print('Saved figure to ../figs/fig.png')

if(y == 'y'):
    subprocess.run(shlex.split('termux-open ../figs/fig.png'))
else:
    subprocess.run(["open",  "../figs/fig.png"])

