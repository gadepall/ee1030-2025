import math 
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from line.funcs import *
#from triangle.funcs import *
#from conics.funcs import circ_gen
#if using termux
import subprocess
import shlex

B = np.array([-5,7]).reshape(-1,1)
C = np.array([-4,5]).reshape(-1,1)

coords = np.block([[B,C]])

BC = line_gen(B,C)

plt.plot(BC[0,:],BC[1,:])

plt.scatter(coords[0,:],coords[1,:])

plt.text(B[0],B[1],"B(-5,7)")
plt.text(C[0],C[1],"C(-4,5)")
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid()
plt.axis('equal')
plt.savefig('../figs/img.png')
