import numpy as np
import ctypes
import os

c_lib = ctypes.CDLL('./code.so')

# Define the argument and return types for the C function to ensure compatibility.
# The function expects a pointer to a C double array and returns a C double.
c_calculate_determinant = c_lib.calculate_determinant
c_calculate_determinant.argtypes = [ctypes.POINTER(ctypes.c_double)]
c_calculate_determinant.restype = ctypes.c_double


def solve_matrix_problem_with_c():
    """
    Solves the matrix problem by first calculating the Q matrix in Python,
    and then calling the external C function to compute its determinant.
    """

    # --- Step 1: Define a sample 3x3 matrix P with a determinant of 2 ---
    P = np.array([[2, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]], dtype=float)

    det_P = np.linalg.det(P)
    print("--- Input Matrix P ---")
    print(f"Matrix P:\n{P}")
    print(f"Determinant of P (verified by numpy): {det_P:.0f}\n")


    # --- Step 2: Create the 3x3 matrix Q in Python ---
    Q = np.zeros((3, 3))
    for i in range(3):  # Corresponds to 1-based row index i=1, 2, 3
        for j in range(3):  # Corresponds to 1-based column index j=1, 2, 3
            exponent = (i + 1) + (j + 1)
            Q[i, j] = (2**exponent) * P[i, j]

    print("--- Resulting Matrix Q ---")
    print(f"Matrix Q (calculated in Python):\n{Q}\n")


    # --- Step 3: Calculate the determinant using the C library ---
    # Flatten the 2D numpy array into a 1D sequence for C
    q_flat = Q.flatten()
    
    # Convert the Python sequence into a C-compatible array of doubles
    q_c_array = (ctypes.c_double * 9)(*q_flat)
    
    # Call the C function with the prepared C array
    det_Q_from_c = c_calculate_determinant(q_c_array)
    
    print("--- Solution (Calculated via C function) ---")
    print(f"The calculated determinant of Q is: {det_Q_from_c:.0f}")

    # --- Step 4: Verify the result ---
    expected_result = 2**13
    print(f"\nThe expected result is 2^13, which is: {expected_result}")

    if np.isclose(det_Q_from_c, expected_result):
        print("\nConclusion: The C function's result matches the expected value.")
    else:
        print("\nConclusion: There is a discrepancy in the result.")

solve_matrix_problem_with_c()
