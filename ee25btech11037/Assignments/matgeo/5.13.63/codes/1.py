import sympy as sp

# 1. Define theta as a symbolic variable
theta = sp.Symbol('theta', real=True)

# 2. Define the matrix M with symbolic entries
s, c = sp.sin(theta), sp.cos(theta)
M = sp.Matrix([
    [s**4, -1 - s**2],
    [1 + c**2, c**4]
])

# 3. Calculate alpha and beta symbolically
# alpha = tr(M)
alpha = M.trace()
# beta = -det(M)
beta = -M.det()

print("Original symbolic expressions:")
print(f"alpha(theta) = {alpha}")
print(f"beta(theta) = {beta}\n")

# 4. Simplify the expressions to match the solution
alpha_simplified = sp.simplify(alpha)
beta_simplified = sp.simplify(beta)

print("Simplified symbolic expressions:")
print(f"alpha(theta) = {alpha_simplified}")
print(f"beta(theta) = {beta_simplified}\n")

# 5. Find the minimum values over the interval [0, 2*pi)
# Define the interval for theta
interval = sp.Interval(0, 2 * sp.pi)

# Find the minimum of alpha and beta in the interval
alpha_star = sp.minimum(alpha_simplified, theta, interval)
beta_star = sp.minimum(beta_simplified, theta, interval)

print("Minimum values (analytical):")
print(f"alpha* = {alpha_star}")
print(f"beta* = {beta_star}\n")

# 6. Calculate the final result
result = alpha_star + beta_star

print("Final Result:")
print(f"alpha* + beta* = {result}")

# Verify the result from the options
# -29/16 = -1.8125
print(f"Decimal value: {result.evalf()}")
