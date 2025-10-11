import numpy as np
import ctypes

# Define a pointer type for a double array
DOUBLE_PTR = ctypes.POINTER(ctypes.c_double)

c_lib = ctypes.CDLL('./inverse.so')

# Define argtypes for add_scaled_row(double*, double*, double, size_t)
c_lib.add_scaled_row.argtypes = [DOUBLE_PTR, DOUBLE_PTR, ctypes.c_double, ctypes.c_size_t]
c_lib.add_scaled_row.restype = None

# Define argtypes for scale_row(double*, double, size_t)
c_lib.scale_row.argtypes = [DOUBLE_PTR, ctypes.c_double, ctypes.c_size_t]
c_lib.scale_row.restype = None


def invert_matrix_with_c(A):
    """
    Inverts a 2x2 matrix using Python logic and C row operations.
    """
    if A.shape != (2, 2):
        return "Input must be a 2x2 matrix.", False
    
    # 1. Create the 2x4 augmented matrix [A|I]
    I = np.identity(2)
    aug = np.concatenate((A, I), axis=1).astype(np.float64)
    num_cols = aug.shape[1]

    # Get C-compatible pointers to the start of each row's data
    row0_ptr = aug[0].ctypes.data_as(DOUBLE_PTR)
    row1_ptr = aug[1].ctypes.data_as(DOUBLE_PTR)

    # --- Python Logic controlling C Functions ---
    
    # 2. Forward Elimination
    # Python calculates the factor
    factor = -aug[1, 0] / aug[0, 0]
    # C performs the operation: R2 -> R2 + factor * R1
    c_lib.add_scaled_row(row1_ptr, row0_ptr, factor, num_cols)
    
    # 3. Check for Singularity (in Python)
    if abs(aug[1, 1]) < 1e-9:
        return "Matrix is singular; inverse does not exist.", False

    # 4. Backward Elimination
    # Python calculates the factor
    factor = -aug[0, 1] / aug[1, 1]
    # C performs the operation: R1 -> R1 + factor * R2
    c_lib.add_scaled_row(row0_ptr, row1_ptr, factor, num_cols)

    # 5. Normalization
    # Python calculates the scaling factor for row 0
    scale_factor_r0 = 1.0 / aug[0, 0]
    # C scales the row: R1 -> R1 / aug[0, 0]
    c_lib.scale_row(row0_ptr, scale_factor_r0, num_cols)
    
    # Python calculates the scaling factor for row 1
    scale_factor_r1 = 1.0 / aug[1, 1]
    # C scales the row: R2 -> R2 / aug[1, 1]
    c_lib.scale_row(row1_ptr, scale_factor_r1, num_cols)
    
    # 6. Extract the inverse
    inverse = aug[:, 2:]
    return inverse, True


# --- Main execution ---
if __name__ == "__main__":
    matrix = np.zeros((2, 2))
    print("Enter the elements of the 2x2 matrix:")
    for i in range(2):
        for j in range(2):
            value = float(input(f"Enter element [{i}][{j}]: "))
            matrix[i, j] = value

    print("\nInput Matrix:\n", matrix)
    print("--------------------------------")
    
    result, success = invert_matrix_with_c(matrix)
    
    if success:
        print("Inverse Matrix Found:\n", result)
    else:
        print("Result:", result)
