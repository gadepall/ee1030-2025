import numpy as np
import scipy.linalg as SA

#Orthogonal matrix
omat = np.array([[0,1],[-1,0]]) 

#Orthogonal matrix
R_o= np.array([[0,-1],[1,0]]) 

#Orthogonal matrix
ref= np.array([[0,1],[1,0]]) 

I = np.eye(2)
e1 = I[:,[0]]
e2 = I[:,[1]]

# Added vector for the unit vector problem
a_vector = np.array([1, 1, 2])


