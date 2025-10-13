import numpy as np
import numpy.linalg as LA
A = np.array([[4,-5],
              [2,-5]])

A_eigen , A_vectors = LA.eig(A)

print("Matrix A:")
print(A)
print("\Eigen Values of A:")
print(A_eigen)
print("\Eigen Vectors of A:")
print(A_vectors)
