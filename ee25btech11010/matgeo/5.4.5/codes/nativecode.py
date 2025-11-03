import numpy as np

#given matrix
A = np.array([[1, 2],[2, 1]])

#computed inverse
A_inverse= np.array([[2/3, -1/3], [-1/3, 2/3]])

#verification
B = A@A_inverse
print(B)