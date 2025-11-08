import numpy as np
import numpy.linalg as LA
import sympy as sp
# Augmented matrix for the mesh equations:
# 71I1 - 41I2 = 45
# -41I1 + 62I2 = 35
A = np.array([
    [71, -41, 45],
    [-41, 62, 35]
], dtype=np.float64)
rank=LA.matrix_rank(A)
M=sp.Matrix(A)
R=M.rref()
print("Row Reduced Matrix:\n",R)
print("Rank of the matrix:",rank)

