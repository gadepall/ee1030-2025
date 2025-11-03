import sympy as sp

b1, b2, b3 = sp.symbols('b1 b2 b3')

A = sp.Matrix([[1, 1],
               [1, 3],
               [-2, -3]])

b = sp.Matrix([[b1],
               [b2],
               [b3]])


left_null = A.T.nullspace()

condition = left_null[0].T * b
condition = sp.simplify(condition[0])

equation = sp.Eq(condition, 0)
print("Condition for solvability:")
sp.pprint(equation)

