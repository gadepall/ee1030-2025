import math
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from line.funcs import *

A = np.array([-2,3]).reshape(-1,1)
B = np.array([8,3]).reshape(-1,1)
C = np.array([6,7]).reshape(-1,1)
D = (A +B )/2
E = (A+C)/2

coords = np.block([[A,B,C,D,E]])

AC = line_gen(A,C)
AB = line_gen(A,B)
BC = line_gen(B,C)
DE = line_gen(D,E)

plt.plot(AC[0,:],AC[1,:])
plt.plot(AB[0,:],AB[1,:])
plt.plot(BC[0,:],BC[1,:])
plt.plot(DE[0,:],DE[1,:])
plt.scatter(coords[0,:],coords[1,:])


plt.text(A[0],A[1],"A(-2,3)")
plt.text(B[0],B[1],"B(8,3)")
plt.text(C[0],C[1],"C(6,7)")
plt.text(D[0],D[1],f"D{D}")
plt.text(E[0],E[1],f"E{E}")
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.savefig('../figs/img.png')
