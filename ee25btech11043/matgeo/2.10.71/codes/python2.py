import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def vector_triple_product_expansion(A, B, C):
    """
    Calculates the vector triple product A x (B x C) using the identity:
    A x (B x C) = (A . C) B - (A . B) C
    """
    return np.dot(A, C) * B - np.dot(A, B) * C

def prove_parallel_to_a(a, b, c, d):
    """
    Proves that (a x b) x (c x d) + (a x c) x (d x b) + (a x d) x (b x c)
    is parallel to a, given that b, c, d are not coplanar.
    """

    # Term 1: (a x b) x (c x d)
    # Using the identity (P x Q) x R = (P . R) Q - (Q . R) P (rearranged for clarity)
    # Let P = (a x b), Q = c, R = d. This is not directly applicable.
    # We need to expand (a x b) x (c x d) using the vector quadruple product identity
    # (A x B) x (C x D) = [A B D] C - [A B C] D
    # Here, A=a, B=b, C=c, D=d
    term1 = np.dot(np.cross(a, b), d) * c - np.dot(np.cross(a, b), c) * d

    # Term 2: (a x c) x (d x b)
    # Here, A=a, B=c, C=d, D=b
    term2 = np.dot(np.cross(a, c), b) * d - np.dot(np.cross(a, c), d) * b

    # Term 3: (a x d) x (b x c)
    # Here, A=a, B=d, C=b, D=c
    term3 = np.dot(np.cross(a, d), c) * b - np.dot(np.cross(a, d), b) * c

    # Sum of the three terms
    result_vector = term1 + term2 + term3

    return result_vector

# --- Example Usage and Visualization ---

# Define non-coplanar vectors b, c, d
# For b, c, d to be non-coplanar, their scalar triple product [b c d] should not be zero.
b = np.array([1, 0, 0])
c = np.array([0, 1, 0])
d = np.array([0, 0, 1]) # These are orthogonal and thus non-coplanar

# Define vector a
a = np.array([2, 3, 4])

# Prove the identity
result_vector = prove_parallel_to_a(a, b, c, d)

# Check if result_vector is parallel to a
# Two vectors u and v are parallel if u = k*v for some scalar k.
# This means their cross product should be the zero vector.
# Or, if one is a scalar multiple of the other.
cross_product_check = np.cross(result_vector, a)

print(f"Vector a: {a}")
print(f"Resulting vector: {result_vector}")
print(f"Cross product of result_vector and a (should be close to zero for parallel): {cross_product_check}")

# Calculate a scalar multiple to show parallelism
# If result_vector = k * a, then k = result_vector[i] / a[i] (for non-zero a[i])
# We can use the scalar triple product [a b c] = a . (b x c)
# The identity simplifies to [b c d] * a
scalar_multiple = np.dot(b, np.cross(c, d))
expected_result = scalar_multiple * a

print(f"Expected result based on identity [b c d] * a: {expected_result}")

# Numerical check for parallelism
is_parallel = np.allclose(np.cross(result_vector, a), [0, 0, 0])
print(f"Is the resulting vector parallel to a? {is_parallel}")

# --- 3D Plotting ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot vectors a, b, c, d
origin = [0, 0, 0]
ax.quiver(*origin, *a, color='red', label='a', arrow_length_ratio=0.1)
ax.quiver(*origin, *b, color='blue', label='b', arrow_length_ratio=0.2)
ax.quiver(*origin, *c, color='green', label='c', arrow_length_ratio=0.2)
ax.quiver(*origin, *d, color='purple', label='d', arrow_length_ratio=0.2)

# Plot the resulting vector
ax.quiver(*origin, *result_vector, color='black', label='Result Vector', arrow_length_ratio=0.1)

# Set plot limits
max_val = np.max(np.abs(np.array([a, b, c, d, result_vector])))
ax.set_xlim([-max_val, max_val])
ax.set_ylim([-max_val, max_val])
ax.set_zlim([-max_val, max_val])

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title("Vector Identity Proof: Result Vector Parallel to 'a'")
ax.legend()
plt.tight_layout()
plt.savefig("fig2.png")
plt.show()
