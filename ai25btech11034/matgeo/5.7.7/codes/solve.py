import sympy as sp

# Define 'n' as a symbol for the matrix dimension (e.g., n x n)
n = sp.Symbol('n')

# Define A as a matrix symbol and I as the identity matrix
A = sp.MatrixSymbol('A', n, n)
I = sp.Identity(n)

# Define the expression to be simplified
expression = (I + A)**3 - 7*A

print(f"Original Expression: {expression}\n")

# Since I (Identity) commutes with A, SymPy can expand this correctly.
expanded_expression = sp.expand(expression)

print(f"Expanded Expression: {expanded_expression}\n")

# Now, we apply the given condition A^2 = A.
# This also implies that A^3 = A^2 * A = A * A = A^2 = A.
# We substitute all powers of A greater than 1 with A.
simplified_expression = expanded_expression.subs({A**2: A, A**3: A})

# Print the final simplified result
print("Final Result after applying A^2 = A:")
sp.pprint(simplified_expression)
