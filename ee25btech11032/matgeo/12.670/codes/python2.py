import numpy as np
import numpy.linalg as LA
A = np.array([[1,0,0],
              [0,3**(1/2)/2,-0.5], 
              [0,0.5,3**(1/2)/2]])

A_eigen , A_vectors = LA.eig(A)

print("Matrix A:")
print(A)
print("\Eigen Values of A:")
print(A_eigen)
