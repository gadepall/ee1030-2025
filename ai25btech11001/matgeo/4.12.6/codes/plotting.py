import math
import sys   
#sys.path.insert(0, '/storage/emulated/0/Abhisek/Math    /Matrix theory/codes/codes/CoordGeo')        #path t    o my scripts
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

A = np.array([980,14]).reshape(-1,1)
B = np.array([1220,16]).reshape(-1,1)
C = np.array([1340,17]).reshape(-1,1)

coords = np.block([[A,B,C]])

AC = line_gen(A,C)

plt.plot(AC[0,:],AC[1,:])
plt.scatter(coords[0,:],coords[1,:])


plt.text(A[0],A[1],"A(980,14)")
plt.text(B[0],B[1],"B(1220,16)")
plt.text(C[0],C[1],"C(1340,17)")
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.savefig('../figs/fig1.png')
