import numpy as np
import numpy.linalg as LA
A = np.array([[2,0,-1],
              [5,1,0],
              [0,1,3]])

A_inv = LA.inv(A)

print("Matrix A:")
print(A)
print("\nInverse of A:")
print(A_inv)
