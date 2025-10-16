import sympy

# 1. Define the unknown variable and knowns as symbolic objects
# d represents the determinant of A, which we want to find.
d = sympy.Symbol('d')

# tr_A is the trace of A.
tr_A = 3
# tr_A3 is the trace of A^3.
tr_A3 = -18
# For a 2x2 matrix, the trace of the identity matrix (I) is 2.
tr_I = 2

# 2. Set up the equation based on the Cayley-Hamilton theorem
# The derived formula is: tr(A^3) = (tr(A)**2 - d)*tr(A) - d*tr(A)*tr(I)
# We create an equation object that is equal to zero.
equation = sympy.Eq((tr_A**2 - d)*tr_A - d*tr_A*tr_I, tr_A3)

# 3. Solve the equation for our unknown variable 'd'
# sympy.solve takes the equation and the variable to solve for.
solution = sympy.solve(equation, d)

# 4. Print the result
# The solution is a list, so we print the first element.
print(f"The equation to solve is: {equation}")
print(f"The calculated determinant of A is: {solution[0]}")
