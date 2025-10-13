import numpy as np
import numpy.linalg as LA
A = np.array([[3,0,-1],
              [2,3,0],
              [0,4,1]])

A_inv = LA.inv(A)

print("Matrix A:")
print(A)
print("\nInverse of A:")
print(A_inv)
