# independent_solver.py
import numpy as np
from math import sqrt

def solve_orthonormal_independent():
    """
    Solution for finding values of a, b, c that render matrix Q orthonormal.

    Matrix Q:
    Q = [1/√3   1/√2    a ]
        [1/√3     0     b ]
        [1/√3  -1/√2    c ]

    For orthonormal matrix: Q^T * Q = I
    """
    
    print("=" * 30)

    sqrt_3 = sqrt(3)
    sqrt_2 = sqrt(2)
    sqrt_6 = sqrt(6)

    # Mathematical derivation:
    # For Q^T * Q = I, we need:
    # 1. Each column has unit norm
    # 2. Columns are orthogonal to each other

    # Column 1: [1/√3, 1/√3, 1/√3] - already unit norm
    # Column 2: [1/√2, 0, -1/√2] - already unit norm
    # Column 3: [a, b, c] - must have unit norm: a² + b² + c² = 1

    # Orthogonality constraints:
    # Column 1 · Column 3 = 0: (1/√3)a + (1/√3)b + (1/√3)c = 0
    #                          => a + b + c = 0
    # Column 2 · Column 3 = 0: (1/√2)a + 0·b + (-1/√2)c = 0
    #                          => a - c = 0 => a = c

    # Solving the system:
    # From a = c and a + b + c = 0:
    # a + b + a = 0 => b = -2a

    # From normalization a² + b² + c² = 1:
    # a² + (-2a)² + a² = 1
    # a² + 4a² + a² = 1
    # 6a² = 1
    # a = ±1/√6

    # Solution 1
    a1 = 1 / sqrt_6
    b1 = -2 / sqrt_6
    c1 = 1 / sqrt_6

    # Solution 2
    a2 = -1 / sqrt_6
    b2 = 2 / sqrt_6
    c2 = -1 / sqrt_6

    print(f"Solution 1: a = {a1:.6f}, b = {b1:.6f}, c = {c1:.6f}")
    print(f"Solution 2: a = {a2:.6f}, b = {b2:.6f}, c = {c2:.6f}")

   
def main():
    """Main function for solution"""
    
    print("The matrix Q can be made orthonormal with two possible solutions:")
    print(f"a = 1/√6, b = -2/√6, c = 1/√6")
    print(f"a = -1/√6, b = 2/√6, c = -1/√6")

if __name__ == "__main__":
    main()
