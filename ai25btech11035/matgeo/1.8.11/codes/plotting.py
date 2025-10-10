import math
import sys   

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

A = np.array([0,3]).reshape(-1,1)
B = np.array([5,0]).reshape(-1,1)
O = np.array([0,0]).reshape(-1,1)
C = np.array([5,3]).reshape(-1,1)
coords = np.block([[A,B,O]])

AO = line_gen(A,O)
AB = line_gen(A,B)
BO = line_gen(B,O)
CO = line_gen(C,O)
AC = line_gen(A,C)
plt.plot(AO[0,:],AO[1,:])
plt.plot(AB[0,:],AB[1,:])
plt.plot(BO[0,:],BO[1,:])
plt.plot(CO[0,:],CO[1,:])
plt.plot(AC[0,:],AC[1,:])
plt.scatter(coords[0,:],coords[1,:])


plt.text(A[0],A[1],"A(0,3)")
plt.text(B[0],B[1],"B(5,0)")
plt.text(C[0],C[1],"C(5,3)")
plt.text(C[0],C[1],"O(0,0)")
plt.xlabel('$x$')
plt.ylabel('$y$')
#plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.savefig('../figs/img.png')
