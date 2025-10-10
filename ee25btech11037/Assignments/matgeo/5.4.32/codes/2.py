import numpy as np

A=np.array([
    [1,0,1],
    [0,1,2],
    [0,0,4]
    ],dtype=float)

A_inv=np.linalg.inv(A)

print(A_inv)
