import sympy as sp

# Define symbols
λ = sp.symbols('lambda')
x, y, z = sp.symbols('x y z')

# Given point
P = sp.Matrix([2, 1, λ])

# Plane: 3x + 5y + 4z = 11
normal_vec = sp.Matrix([3, 5, 4])
plane_constant = 11

# Distance formula from point to plane
# D = |n · P - d| / ||n||
numerator = abs(normal_vec.dot(P) - plane_constant)
denominator = sp.sqrt(normal_vec.dot(normal_vec))
distance = numerator / denominator

# Set the distance equal to 2√2 and solve
eq = sp.Eq(distance, 2 * sp.sqrt(2))
solutions = sp.solve(eq, λ)

# Display result
print("Values of lambda for which the distance is 2√2:")
for sol in solutions:
    print(f"λ = {sol}")

