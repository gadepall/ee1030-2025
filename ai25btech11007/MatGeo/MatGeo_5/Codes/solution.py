import numpy as np

# Given vectors
b = np.array([ -3, -1, 2 ])
c = np.array([ 3, 1, -2 ])

# Compute a = b + c
a = b + c

# Cross product of b and c
cross_product = np.cross(b, c)

# Magnitude of the cross product
area = 0.5 * np.linalg.norm(cross_product)

# Output vectors and area
print(f"Vector a = b + c = {a}")
print(f"Cross product (b x c) = {cross_product}")
print(f"Area of triangle = {area:.4f}")
print(f"Expected area = {5 * np.sqrt(6):.4f}")

# Check consistency
if np.all(a == 0) and area == 0:
    print("✅ Vectors are collinear. Triangle is degenerate. Area = 0.")
else:
    print("❌ Vectors form a triangle with nonzero area. Inconsistent with a = 0.")
