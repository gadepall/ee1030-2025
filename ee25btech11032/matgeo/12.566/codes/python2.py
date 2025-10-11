import numpy as np
import numpy.linalg as LA
A = np.array([[2,3],
              [0,7]])

A_eigen , A_vectors = LA.eig(A)

print("Matrix A:")
print(A)
print("\Eigen Values Product :")
print(A_eigen[0]*A_eigen[1])

