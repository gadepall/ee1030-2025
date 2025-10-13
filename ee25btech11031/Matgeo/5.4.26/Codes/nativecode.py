import numpy as np
import numpy.linalg as LA

A = np.array([
    [1.0, -3.0, 2.0],
    [-3.0, 0.0, -5.0],
    [2.0, 5.0, 0.0]
])

A_inv = LA.inv(A)

print(A_inv)

