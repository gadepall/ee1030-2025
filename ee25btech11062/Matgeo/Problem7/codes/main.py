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

x = np.array([1, -2]).reshape(-1,1)
m1 = np.array([-2, 1]).reshape(-1,1)
m2 = np.array([1/2, 1]).reshape(-1,1)

p_l1 = line_gen(x-5*m1, x+5*m1)
p_l2 = line_gen(x-5*m2, x+5*m2)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(p_l1[0, :], p_l1[1, :], label = 'Given line')
ax.plot(p_l2[0, :], p_l2[1, :], label = 'Required Line')

ax.scatter(np.array([x[0]]), np.array([x[1]]))
ax.text(x[0], x[1], s='(1,-2)')

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

