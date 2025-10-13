from sympy import Matrix

M = Matrix([
    [217, 131, 912],
    [131, 217, 827]
])

M[0, :] = M[0, :] / 217
M[1, :] = M[1, :] - 131 * M[0, :]
M[1, :] = M[1, :] / M[1, 1]
M[0, :] = M[0, :] - M[0, 1] * M[1, :]

print("Reduced matrix:")
print(M)
print("Solution:")
print(M[:, 2])
