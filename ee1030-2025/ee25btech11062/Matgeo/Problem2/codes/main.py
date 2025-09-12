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

R = np.array([2, 2, -1]).reshape(-1, 1)
O = np.zeros(3).reshape(-1, 1)
norm_R = LA.norm(R)
X = R/norm_R
print(f"The direction cosines of the given vector is \n{X}")

p_OR = line_gen(O, R)
p_OX = line_gen(O, X)

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

ax.plot(p_OR[0, :], p_OR[1, :], p_OR[2, :], label = 'Line through OR')
ax.plot(p_OX[0, :], p_OX[1, :], p_OX[2, :], label = 'Direction cosines of OR')

line_coords = np.block([[O, R, X]])
ax.scatter(line_coords[0,:], line_coords[1,:], line_coords[2, :])
vert_labels = ['O','R','X']
for i, txt in enumerate(vert_labels):
    ax.text(line_coords[0][i], line_coords[1][i], line_coords[2][i], txt, color='red')

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

