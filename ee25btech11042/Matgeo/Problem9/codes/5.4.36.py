import sympy as sp

A = sp.Matrix([[2, -1, -2], [0, 2, -1],[3, -5, 0]])
A_inv = A.inv()
sp.pprint(A_inv) 
