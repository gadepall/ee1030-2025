import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the shared library
lib_vector = ctypes.CDLL("/code5.so")

# Define argument types and return types for C functions

# cross_product(ax, ay, az, bx, by, bz, *rx, *ry, *rz)
lib_vector.cross_product.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
]
lib_vector.cross_product.restype = None

# dot_product(ax, ay, az, bx, by, bz)
lib_vector.dot_product.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double, ctypes.c_double
]
lib_vector.dot_product.restype = ctypes.c_double

# term1_calc(ax, ay, az, bx, by, bz, cx, cy, cz, dx, dy, dz, *term1_rx, *term1_ry, *term1_rz)
lib_vector.calculate_vector_quad_cross.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
]
lib_vector.calculate_vector_quad_cross.restype = None

# calculate_full_expression(ax, ay, az, bx, by, bz, cx, cy, cz, dx, dy, dz, *result_x, *result_y, *result_z)
lib_vector.calculate_full_expression.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
]
lib_vector.calculate_full_expression.restype = None

# scalar_triple_product(bx, by, bz, cx, cy, cz, dx, dy, dz)
lib_vector.scalar_triple_product.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double, ctypes.c_double
]
lib_vector.scalar_triple_product.restype = ctypes.c_double


# Define arbitrary non-coplanar vectors b, c, d
# To ensure non-coplanarity, their scalar triple product should not be zero.
# Let's pick some simple non-coplanar vectors.
b_np = np.array([1.0, 0.0, 0.0])
c_np = np.array([0.0, 1.0, 0.0])
d_np = np.array([0.0, 0.0, 1.0]) # These form a basis, definitely non-coplanar

# Test coplanarity (should be close to 1 for our chosen b,c,d as they form a unit cube volume)
stp_val = lib_vector.scalar_triple_product(
    b_np[0], b_np[1], b_np[2],
    c_np[0], c_np[1], c_np[2],
    d_np[0], d_np[1], d_np[2]
)
print(f"Scalar Triple Product of b, c, d: {stp_val}")
if np.isclose(stp_val, 0.0):
    print("Warning: Vectors b, c, d might be coplanar. Please choose different vectors.")
else:
    print("Vectors b, c, d are not coplanar (as required).")


# Define an arbitrary vector a
a_np = np.array([2.0, 3.0, 4.0])

# Ctypes doubles to hold the result
result_x = ctypes.c_double()
result_y = ctypes.c_double()
result_z = ctypes.c_double()

# Call the C function to calculate the full expression
lib_vector.calculate_full_expression(
    a_np[0], a_np[1], a_np[2],
    b_np[0], b_np[1], b_np[2],
    c_np[0], c_np[1], c_np[2],
    d_np[0], d_np[1], d_np[2],
    ctypes.byref(result_x), ctypes.byref(result_y), ctypes.byref(result_z)
)

calculated_vector_np = np.array([result_x.value, result_y.value, result_z.value])

print(f"\nVector a: {a_np}")
print(f"Calculated expression vector: {calculated_vector_np}")

# Prove parallelism: The calculated vector should be a scalar multiple of 'a'.
# This means calculated_vector = k * a for some scalar k.
# We can find k by dividing corresponding components (if 'a' components are non-zero).
# Or, check if the cross product of 'a' and the calculated vector is zero (or very close to zero).

is_parallel = False
if np.allclose(calculated_vector_np, np.array([0,0,0])) and np.allclose(a_np, np.array([0,0,0])):
    is_parallel = True # Both are zero vectors
elif np.allclose(calculated_vector_np, np.array([0,0,0])):
    is_parallel = True # The calculated vector is zero, it's parallel to any vector.
elif np.allclose(a_np, np.array([0,0,0])):
    is_parallel = True # Vector 'a' is zero, the calculated vector would need to be zero as well for parallelism
    # However, the expression is always parallel to 'a', so if 'a' is zero, the expression must also be zero.
    # We should have ensured 'a' is not zero for a more meaningful "parallel" proof.
    # For this specific proof, if a is zero, the expression is also zero, so it is parallel to a.
else:
    # Check if cross product is zero
    cross_prod_check = np.cross(a_np, calculated_vector_np)
    if np.allclose(cross_prod_check, np.array([0, 0, 0])):
        is_parallel = True
        # Calculate the scalar multiple k
        # We can use numpy's norm for a robust calculation if 'a' is not zero.
        if np.linalg.norm(a_np) > 1e-9: # Avoid division by zero
            k = np.dot(calculated_vector_np, a_np) / np.dot(a_np, a_np)
            print(f"Scalar multiple k: {k:.4f}")
            print(f"Check: k * a = {k * a_np}")

if is_parallel:
    print("\nResult: The calculated vector is parallel to vector 'a'.")
else:
    print("\nResult: The calculated vector is NOT parallel to vector 'a'. (This indicates an issue with the C code or the setup)")


# --- Plotting the vectors in 3D ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Origin for vectors
origin = [0, 0, 0]

# Plot vector 'a'
ax.quiver(*origin, a_np[0], a_np[1], a_np[2], color='blue', arrow_length_ratio=0.1, label='Vector a')
ax.text(a_np[0], a_np[1], a_np[2], 'a', color='blue')

# Plot vector 'b'
ax.quiver(*origin, b_np[0], b_np[1], b_np[2], color='red', arrow_length_ratio=0.2, label='Vector b')
ax.text(b_np[0], b_np[1], b_np[2], 'b', color='red')

# Plot vector 'c'
ax.quiver(*origin, c_np[0], c_np[1], c_np[2], color='green', arrow_length_ratio=0.2, label='Vector c')
ax.text(c_np[0], c_np[1], c_np[2], 'c', color='green')

# Plot vector 'd'
ax.quiver(*origin, d_np[0], d_np[1], d_np[2], color='purple', arrow_length_ratio=0.2, label='Vector d')
ax.text(d_np[0], d_np[1], d_np[2], 'd', color='purple')

scale_factor = 0.5   # adjust as needed (0.2 = very short, 1.0 = full length)
calculated_vector_scaled = calculated_vector_np * scale_factor

# Plot the scaled black vector
ax.quiver(*origin,
          calculated_vector_scaled[0], calculated_vector_scaled[1], calculated_vector_scaled[2],
          color='black', arrow_length_ratio=0.05)

ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.legend()
plt.grid(True)
plt.show()
