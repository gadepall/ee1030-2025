from sympy import Matrix, sqrt

P = Matrix([3, 2, 1])
N = Matrix([2, -1, 1])

num = N.dot(P) - 1
den = N.dot(N)

Q = P - (num / den) * N
dist = (num / den) * sqrt(den)
R = P - 2 * (num / den) * N

print("Q =", Q)
print("Distance =", dist)
print("Image =", R)
