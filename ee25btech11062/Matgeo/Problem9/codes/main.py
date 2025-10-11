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

A = np.array([8, 2]).reshape(-1,1)
m = np.array([1, -1/2]).reshape(-1,1)

p_l1 = line_gen(A-8*m, A+4*m)

plt.plot(p_l1[0, :], p_l1[1, :], label = 'Line with min OP+OQ')

pts = np.block([A-8*m, A+4*m, A])
labels = ['P(0,6)', 'Q(12,0)', 'A(8,2)']
plt.scatter(pts[0, :], pts[1, :])
for i, txt in enumerate(labels):
        plt.annotate(txt, (pts[0, i], pts[1, i]), textcoords="offset points", xytext=(20,5), ha='center')

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position('zero')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')

plt.savefig('../figs/fig.png')
print('Saved figure to ../figs/fig.png')

if(y == 'y'):
    subprocess.run(shlex.split('termux-open ../figs/fig.png'))
else:
    subprocess.run(["open",  "../figs/fig.png"])
