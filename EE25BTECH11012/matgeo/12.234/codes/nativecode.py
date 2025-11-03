import numpy as np

# Define the vectors
v1 = np.array([1, 1, 1])
v2 = np.array([1, -1, 1])
v3 = np.array([1, 1, -1])

# Form the matrix with given vectors as columns
A = np.column_stack((v1, v2, v3))

# 1. Check Linear Independence using determinant
det_A = np.linalg.det(A)
if abs(det_A) > 1e-9:
    print("S is a linearly independent set.")
else:
    print("S is not a linearly independent set.")

# 2. Check if S is a basis for R³
if A.shape == (3,3) and abs(det_A) > 1e-9:
    print("S is a basis for R³.")
else:
    print("S is not a basis for R³.")

# 3. Check if vectors are orthogonal
def is_orthogonal(u, v):
    return np.dot(u, v) == 0

print("Dot products:")
print("v1·v2 =", np.dot(v1, v2))
print("v1·v3 =", np.dot(v1, v3))
print("v2·v3 =", np.dot(v2, v3))

if is_orthogonal(v1, v2) and is_orthogonal(v1, v3) and is_orthogonal(v2, v3):
    print("The vectors in S are orthogonal.")
else:
    print("The vectors in S are not orthogonal.")

# 4. Generate an orthogonal set using Gram-Schmidt process
def gram_schmidt(vectors):
    ortho = []
    for v in vectors:
        for u in ortho:
            v = v - np.dot(v, u) / np.dot(u, u) * u
        ortho.append(v)
    return ortho

orthogonal_set = gram_schmidt([v1, v2, v3])
print("\nOrthogonal set generated using Gram-Schmidt:")
for vec in orthogonal_set:
    print(vec)
