import numpy as np

def f(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0, 0, 1]
    ])

# Take input
alpha = float(input("Enter alpha (in radians): "))
beta = float(input("Enter beta (in radians): "))

# Compute both sides
lhs = f(alpha) @ f(-beta)
rhs = f(alpha - beta)

# Check equality (within tolerance, since floats may not be exact)
if np.allclose(lhs, rhs, atol=1e-9):
    print("Verified: f(alpha) f(-beta) = f(alpha - beta)")
else:
    print(" Not equal")
    print("LHS =\n", lhs)
    print("RHS =\n", rhs)

