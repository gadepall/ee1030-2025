import numpy as np

A = np.array([[2, 3], [4, 7]])
I = np.eye(2)

A_inv = np.linalg.inv(A)

# Verify Cayley-Hamilton theorem
A2 = np.dot(A, A)
lhs = A2 - 9 * A + 2 * I
print("LHS of Cayley-Hamilton theorem (should be zero matrix):\n", lhs)

# Verify that A^-1 = 1/2 (9I - A)
print("A^-1 (from calculation) =\n", A_inv)
print("A^-1 (from Cayley-Hamilton) =\n", 1/2 * (9*I - A))
print("equality: ", np.allclose(A_inv, 1/2 * (9*I - A)))