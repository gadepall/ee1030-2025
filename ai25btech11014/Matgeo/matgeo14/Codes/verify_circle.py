from sympy import Matrix, simplify

P = Matrix([[-2], [4]])
C = Matrix([[3], [5]])
r_squared = 36

diff = P - C
distance_squared = simplify(diff.T * diff)[0]

print("Distance squared:", distance_squared)
print("Radius squared:", r_squared)
print("Point lies on circle:", distance_squared == r_squared)

