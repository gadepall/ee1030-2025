import numpy as np

# Given values
a = 4.0        # |a|
lhs = 144.0    # |a × b|^2 + (a · b)^2

# Using numpy
b_squared = lhs / np.power(a, 2)
b = np.sqrt(b_squared)

print(f"|b| = {b}")
