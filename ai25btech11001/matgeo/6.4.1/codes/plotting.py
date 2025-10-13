import math
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from line.funcs import *

X = np.ones((6,2))

X[:,1] = [2001 ,2002 ,2003,2004,2005,2006]
print(X)

D = np.array(
[30,35,36,32,37,40]
        ).reshape(-1,1)
print((X.T@D))
print(X.T@X)
print(LA.inv(X.T@X))
N = (LA.inv(X.T@X))@(X.T@D)
print(N)
print(N.T@np.array([[1],[0]]))
print(N.T@np.array([[1],[2008]]))
x = np.ones((2,50))
x[1,:] = np.linspace(2000 , 2009,50)
print(X.shape,N.shape)
y = x.T@(N)
Y = X@(N)

plt.plot(x[1,:],y,color="green")
plt.scatter(X[:,1],D)
plt.scatter(2008,np.array([1,2008])@N,color="red")

plt.legend(loc='best')
plt.savefig('../figs/img.png')
