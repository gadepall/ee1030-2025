import math
import sys   
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from function import *
#from triangle.funcs import *
#from conics.funcs import circ_gen
#if using termux
import subprocess
import shlex

A = np.array([3,1]).reshape(-1,1)
B = np.array([5,1]).reshape(-1,1)
C = np.array([6,3]).reshape(-1,1)
D = np.array([4,3]).reshape(-1,1)

coords = np.block([[A,B,C,D]])

AB = line_gen(A,B)
BC = line_gen(B,C)
CD = line_gen(C,D)
DA = line_gen(D,A)

plt.plot(AB[0,:],AB[1,:])
plt.plot(BC[0,:],BC[1,:])
plt.plot(CD[0,:],CD[1,:])
plt.plot(DA[0,:],DA[1,:])

plt.scatter(coords[0,:],coords[1,:])

plt.text(A[0],A[1],"A(3,1)")
plt.text(B[0],B[1],"B(5,1)")
plt.text(C[0],C[1],"C(6,3)")
plt.text(D[0],D[1],"D(4,3)")
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid()
plt.axis('equal')

plt.savefig('../figs/img.png')
