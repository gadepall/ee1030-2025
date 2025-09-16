import math
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from line.funcs import *

A = np.array([0,0]).reshape(-1,1)
B = np.array([6,0]).reshape(-1,1)
C = np.array([3,3*math.sqrt(3)]).reshape(-1,1)

coords = np.block([[A,B,C]])

AC = line_gen(A,C)
AB = line_gen(A,B)
BC = line_gen(B,C)

plt.plot(AC[0,:],AC[1,:])
plt.plot(AB[0,:],AB[1,:])
plt.plot(BC[0,:],BC[1,:])
plt.scatter(coords[0,:],coords[1,:])


plt.text(A[0],A[1],"A(0,0)")
plt.text(B[0],B[1],"B(6,0)")
plt.text(C[0],C[1],"C(6cos(60),6sin(60))")
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.savefig('../figs/fig1.png')

