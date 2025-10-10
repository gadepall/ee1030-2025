import numpy as np

# Solution from the problem
x = -7/58
y = 7/69

print(f"Solution: x = {x:.6f}, y = {y:.6f}")

# Verify by substituting into original equations
eq1 = 2/x + 3/y
eq2 = 5/x + 4/y


# Alternative verification using matrix method
A = np.array([[2, 3], [5, 4]])
b = np.array([13, -2])

# Solve for u, v where u = 1/x, v = 1/y
uv = np.linalg.solve(A, b)
u, v = uv[0], uv[1]

x_calc = 1/u
y_calc = 1/v

print(f"\nMatrix method:")
print(f"u = 1/x = {u:.6f}, v = 1/y = {v:.6f}")
print(f"x = {x_calc:.6f}, y = {y_calc:.6f}")
print(f"Matches analytical solution: {abs(x - x_calc) < 1e-9 and abs(y - y_calc) < 1e-9}")