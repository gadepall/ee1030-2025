import sympy as sp

A = sp.Matrix([[1, -1, 2], [0, 2, -3], [3, -2, 4]])
A_inv = A.inv()
sp.pprint(A_inv)

