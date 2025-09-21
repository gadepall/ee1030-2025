import numpy as np

# Input vectors
a = np.array(list(map(int, input("Enter vector a (3 integers separated by space): ").split())))
b = np.array(list(map(int, input("Enter vector b (3 integers separated by space): ").split())))
dot_val = int(input("Enter value of a · c: "))

# Unknown vector c = (c1, c2, c3)
# Setup equations:
# a x c = b  => gives 3 linear equations
# a · c = dot_val => 1 equation
# Total: 4 equations, 3 unknowns -> solve system

# Coefficient matrix (augmented form)
# Let c = (x,y,z)
# Equations:
#   a2*z - a3*y = b1
#   a3*x - a1*z = b2
#   a1*y - a2*x = b3
#   a1*x + a2*y + a3*z = dot_val

A = np.array([
    [0, -a[2], a[1]],     # from a2*z - a3*y = b1
    [a[2], 0, -a[0]],     # from a3*x - a1*z = b2
    [-a[1], a[0], 0],     # from a1*y - a2*x = b3
    [a[0], a[1], a[2]]    # dot product
], dtype=float)

rhs = np.array([b[0], b[1], b[2], dot_val], dtype=float)

# Solve least squares (in case overdetermined)
c, residuals, rank, s = np.linalg.lstsq(A, rhs, rcond=None)

print("Vector c =", np.round(c, 4))

