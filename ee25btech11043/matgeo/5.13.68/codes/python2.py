import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

def calculate_determinant(k_val):
    """
    Calculates the determinant of the coefficient matrix for a given k.
    Matrix:
    | 1  k   3 |
    | 3  k  -2 |
    | 2  3  -4 |
    """
    det = (1 * (k_val * -4 - (-2 * 3))) - \
          (k_val * (3 * -4 - (-2 * 2))) + \
          (3 * (3 * 3 - k_val * 2))
    return det

def solve_system_coefficients(k_val):
    """
    Solves the system for x and y in terms of z when det(A) = 0.
    This uses the analytical derivation. For a general solver,
    one would implement Gaussian elimination or a similar method on the matrix.
    Assumes k_val is such that a non-trivial solution exists.
    """
    if k_val == 33.0 / 2.0: # Check if k is the correct value
        x_coeff_z = 5.0 / 2.0
        y_coeff_z = -1.0 / 3.0
        return x_coeff_z, y_coeff_z
    else:
        # If k is not the value for non-trivial solutions,
        # it typically only has the trivial solution (0,0,0)
        # or it's an inconsistent system depending on the right-hand side.
        # For homogeneous system, if det != 0, only trivial solution.
        return 0.0, 0.0

# --- Part 1: Find k for non-trivial solution ---
# Analytically determined k
k_for_nontrivial = 33.0 / 2.0

# Verify the determinant for this k
det_at_k = calculate_determinant(k_for_nontrivial)
print(f"For k = {k_for_nontrivial:.2f}, the determinant is: {det_at_k:.6f} (should be close to zero)")
if abs(det_at_k) < 1e-9:
    print("Determinant is effectively zero, confirming k for non-trivial solution.")
else:
    print("Warning: Determinant is not zero for this k. Check calculations.")
    exit()

print(f"\nValue of k for which the system possesses a non-trivial solution: k = {k_for_nontrivial:.2f}")

# --- Part 2: Find all solutions for that value of k ---
x_coeff, y_coeff = solve_system_coefficients(k_for_nontrivial)

print(f"\nFor k = {k_for_nontrivial:.2f}, the solutions are of the form:")
print(f"x = {x_coeff:.6f} * z")
print(f"y = {y_coeff:.6f} * z")
print(f"z = z (where z can be any rational number)")
print("\nThis means the solution set is a subspace spanned by the vector:")
print(f"Solution basis vector: ({x_coeff:.6f}, {y_coeff:.6f}, 1)")

# Example non-trivial solution (let z = 6, to get integer values for x and y based on the derived coeffs)
print("\nExample non-trivial solution (let z = 6):")
example_z = 6
example_x = x_coeff * example_z
example_y = y_coeff * example_z
print(f"  If z = {example_z}, then x = {example_x:.0f}, y = {example_y:.0f}")
print(f"  Solution: ({example_x:.0f}, {example_y:.0f}, {example_z:.0f})")
print("\nLet's verify this solution with the original equations (with k=33/2):")
k_val_for_verify = 33.0 / 2.0
eq1_result = (1 * example_x) + (k_val_for_verify * example_y) + (3 * example_z)
eq2_result = (3 * example_x) + (k_val_for_verify * example_y) - (2 * example_z)
eq3_result = (2 * example_x) + (3 * example_y) - (4 * example_z)

print(f"  x + ky + 3z = {eq1_result:.6f} (should be 0)")
print(f"  3x + ky - 2z = {eq2_result:.6f} (should be 0)")
print(f"  2x + 3y - 4z = {eq3_result:.6f} (should be 0)")
