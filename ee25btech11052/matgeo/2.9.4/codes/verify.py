import numpy as np

# Given values
a = np.array([1, 1, 1])
b = np.array([1, 0, 0])  # Solution

# Check constraints
dot_product = np.dot(a, b)
cross_product = np.cross(a, b)
magnitude_b = np.linalg.norm(b)

print(f"a·b = {dot_product} (should be 1)")
print(f"a×b = {cross_product} (should be [0, 1, -1])")
print(f"|b| = {magnitude_b}")

# Verify
print(f"Dot product correct: {abs(dot_product - 1.0) < 1e-9}")
print(f"Cross product correct: {np.allclose(cross_product, [0, 1, -1])}")
print(f"Answer: |b| = {magnitude_b}")