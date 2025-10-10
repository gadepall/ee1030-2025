import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA
import math
from line.funcs import *

r=math.sqrt(3)

A=np.array([-5,0]).reshape(-1,1)
B=np.array([20,(2-r)*25]).reshape(-1,1)

C=np.array([5,(2+r)*(-2)]).reshape(-1,1)
D=np.array([12,(2+r)*(5)]).reshape(-1,1)

AB=line_gen(A,B)
CD=line_gen(C,D)

coords=np.block([[A,B,C,D]])

plt.plot(AB[0,:],AB[1,:])
plt.plot(CD[0,:],CD[1,:])

plt.scatter(coords[0,:],coords[1,:])

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid()
plt.axis('equal')

plt.savefig('../figs/img.png')
