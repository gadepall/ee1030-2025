import math
import sys   
 #path t    o my scripts
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
#end if

A = np.array([2,3]).reshape(-1,1)
B = np.array([7,8]).reshape(-1,1)
P = np.array([4,5]).reshape(-1,1)

coords = np.block([[A,B,P]])

AB = line_gen(A,B)

plt.plot(AB[0,:],AB[1,:])
plt.scatter(coords[0,:],coords[1,:])


plt.text(A[0],A[1],"A(2,3)")
plt.text(B[0],B[1],"B(7,8)")
plt.text(P[0],P[1],"P(4,5)")
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.savefig('../figs/img.png')
