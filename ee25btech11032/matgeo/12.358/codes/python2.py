import numpy as np
import numpy.linalg as LA
A = np.array([[1,2],
              [5,7]])

A_inv = LA.inv(A)

print("Matrix A:")
print(A)
print("\nInverse of A:")
print(A_inv)
