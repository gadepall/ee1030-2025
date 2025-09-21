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

A = np.array([3,-4]).reshape(-1,1)
B = np.array([-2,6]).reshape(-1,1)
C = np.array([-3,6]).reshape(-1,1)
D = np.array([9,-18]).reshape(-1,1)
coords = np.block([[A,B,C,D]])

AB = line_gen(A,B)
CD = line_gen(C,D)
plt.plot(AB[0,:],AB[1,:])
plt.plot(CD[0,:],CD[1,:])
plt.scatter(coords[0,:],coords[1,:])


plt.text(A[0],A[1],"A(3,-4)")
plt.text(B[0],B[1],"B(-2,6)")
plt.text(C[0],C[1],"C(-3,6)")
plt.text(D[0],D[1],"D(9,-18)")
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.savefig('../figs/img.png')
