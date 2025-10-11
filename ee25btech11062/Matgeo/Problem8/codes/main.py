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

m1 = np.array([2, 3]).reshape(-1,1)
m2 = np.array([-3, 2]).reshape(-1,1)
m3 = np.array([5, 1]).reshape(-1,1)
A = np.array([3, 5]).reshape(-1,1)
B = np.array([6, 3]).reshape(-1,1)
C = np.array([1, 2]).reshape(-1,1)


p_l1 = line_gen(A-1.5*m1, A+1.5*m1)
p_l2 = line_gen(B-1.5*m2, B+1.5*m2)
p_l3 = line_gen(C-1.5*m3, C+1.5*m3)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(p_l1[0, :], p_l1[1, :], label = '3x-2y+1=0')
ax.plot(p_l2[0, :], p_l2[1, :], label = '2x+3y-21=0')
ax.plot(p_l3[0, :], p_l3[1, :], label = 'x-5y+9=0')

pts = np.block([A, B, C])
labels = ['A(3,5)', 'B(6,3)', 'C(1,2)']
ax.scatter(pts[0, :], pts[1, :])
for i, txt in enumerate(labels):
        ax.text(pts[0, i], pts[1, i], s=txt)

ax.set_xlabel('$X$')
ax.set_ylabel('$Y$')
ax.legend(loc='best')
ax.grid(True) 
ax.axis('equal')

fig.savefig('../figs/fig.png')
print('Saved figure to ../figs/fig.png')

if(y == 'y'):
    subprocess.run(shlex.split('termux-open ../figs/fig.png'))
else:
    subprocess.run(["open",  "../figs/fig.png"])

