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

m1 = np.array([0, 2/3, -2]).reshape(-1, 1)
r1 = np.array([5, 0, 0]).reshape(-1, 1)
m2 = np.array([0, -1, -1/3]).reshape(-1,1)
r2 = np.array([2, 0, 0]).reshape(-1, 1)
O = np.zeros(3).reshape(-1, 1)
if(m1.T@m2 == 0):
    print('The two lines are perpendicular')
else:
    print('The two lines are not perpendicular')

p_m1 = line_gen(r1-8*m1, r1+8*m1)
p_m2 = line_gen(r2-8*m2, r2+8*m2)

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

ax.plot(p_m1[0, :], p_m1[1, :], p_m1[2, :], label = 'Line L1')
ax.plot(p_m2[0, :], p_m2[1, :], p_m2[2, :], label = 'Line L2')

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.legend(loc='best')
ax.grid(True) 
ax.axis('equal')

fig.savefig('../figs/fig.png')
print('Saved figure to ../figs/fig.png')

if(y == 'y'):
    subprocess.run(shlex.split('termux-open ../figs/fig.png'))
else:
    subprocess.run(["open",  "../figs/fig.png"])

