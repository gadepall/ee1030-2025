
import math
import numpy as np
import numpy.linalg as LA

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
print(N.T@np.array([[1],[2008]]))

