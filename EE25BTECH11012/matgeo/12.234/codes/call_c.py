import ctypes
import math

# Define C-like types
c_float = ctypes.c_float
c_float_p = ctypes.POINTER(c_float)

# Define C-like array types
# float[3] is analogous to C float v[3]
FloatArray3 = c_float * 3
# float[3][3] is analogous to C float A[3][3]
FloatMatrix3x3 = (c_float * 3) * 3

# Function to calculate determinant of 3x3 matrix
# Takes a 3x3 array/matrix of c_float
def determinant(a):
    """Calculates the determinant of a 3x3 matrix represented by a ctypes array."""
    # Access elements using a[row][col]
    det = a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1]) \
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0]) \
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    return det.value if isinstance(det, c_float) else det

# Function to compute dot product of two 3D vectors
# Takes two 3-element arrays/vectors of c_float
def dot_product(a, b):
    """Computes the dot product of two 3D vectors represented by ctypes arrays."""
    # Access elements using a[index]
    result = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
    return result.value if isinstance(result, c_float) else result

# Main execution block
def main():
    # Define vectors using the C-like FloatArray3 type
    v1 = FloatArray3(1.0, 1.0, 1.0)
    v2 = FloatArray3(1.0, -1.0, 1.0)
    v3 = FloatArray3(1.0, 1.0, -1.0)
    
    # Define the tolerance (epsilon) used for floating-point comparisons
    TOLERANCE = 1e-6
    
    # Form matrix A with vectors as columns using the C-like FloatMatrix3x3 type
    A = FloatMatrix3x3(
        FloatArray3(v1[0], v2[0], v3[0]), # Row 0: x-components
        FloatArray3(v1[1], v2[1], v3[1]), # Row 1: y-components
        FloatArray3(v1[2], v2[2], v3[2])  # Row 2: z-components
    )

    print("--- Linear Algebra Calculations with ctypes ---")
    
    # 1. Check linear independence using determinant
    det = determinant(A)
    print(f"Determinant = {det:.2f}")

    if abs(det) > TOLERANCE:
        print("S is a linearly independent set.")
    else:
        print("S is NOT a linearly independent set.")

    # 2. Check if it is a basis for R^3
    if abs(det) > TOLERANCE:
        print("S is a basis for R^3.")
    else:
        print("S is NOT a basis for R^3.")

    # 3. Check orthogonality
    d12 = dot_product(v1, v2)
    d13 = dot_product(v1, v3)
    d23 = dot_product(v2, v3)

    print("\nDot products:")
    print(f"v1·v2 = {d12:.2f}")
    print(f"v1·v3 = {d13:.2f}")
    print(f"v2·v3 = {d23:.2f}")

    is_orthogonal = abs(d12) < TOLERANCE and abs(d13) < TOLERANCE and abs(d23) < TOLERANCE

    if is_orthogonal:
        print("Vectors are orthogonal.")
    else:
        print("Vectors are NOT orthogonal.")

    # 4. Based on results, print the correct option
    print("\nCorrect statement:")
    if abs(det) > TOLERANCE and not is_orthogonal:
        print("Option (b): S is a basis for R^3.")
    elif abs(det) < TOLERANCE:
        print("Option (a): S is not a linearly independent set.")
    elif is_orthogonal:
        print("Option (c): The vectors in S are orthogonal.")
    else:
        # This else block should theoretically not be reached if the previous logic is exhaustive
        print("Option (d): An orthogonal set cannot be generated from S.")

if __name__ == "__main__":
    main()