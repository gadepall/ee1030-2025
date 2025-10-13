# Solving for the inverse using only python

import sympy as sp

x = sp.symbols('x')
A = sp.Matrix([
    [x**2 - x + 1, x - 1],
    [x + 1, x + 1]
])

A_inv = A.inv()
print(A_inv)