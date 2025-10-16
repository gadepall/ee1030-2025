import numpy as np
import ctypes
import os

def print_matrix(name, mat):
    """Helper function to print a matrix with a given name."""
    print(f"Matrix {name}:")
    # Set print options to match the output format
    np.set_printoptions(suppress=True, precision=8)
    print(mat)
    print()

def print_vector(name, vec):
    """Helper function to print a vector."""
    print(f"{name} = {vec.flatten()}")

def main():
    """
    Main function to perform calculations and call the C library.
    """
    # --- 1. Initial Setup and Calculations in Python ---

    # Define matrices R and P from the problem
    R = np.array([
        [0.22751661, 0.95187796, 0.90271902],
        [0.16238862, 0.50450366, 0.25222053],
        [0.3357095,  0.57062374, 0.8009969 ]
    ])

    P = np.array([
        [2, 0, 0],
        [0, 3, 4],
        [0, 4, 9]
    ])

    print_matrix("R", R)

    # Calculate the inverse of R using numpy
    R_inv = np.linalg.inv(R)
    print_matrix("R⁻¹ (R_inv)", R_inv)

    print_matrix("P", P)

    # Calculate eigenvalues and eigenvectors of P
    eigenvalues, eigenvectors = np.linalg.eig(P)

    # The eigenvalues of P are [11, 1, 2]. We select the one specified.
    selected_lambda = 11.0
    # Find the index of the selected eigenvalue
    lambda_index = np.where(np.isclose(eigenvalues, selected_lambda))[0][0]

    # Get the corresponding eigenvector
    x = eigenvectors[:, lambda_index]

    print(f"Eigenvalues of P: {eigenvalues}")
    print(f"Selected eigenvalue (λ) of P: {selected_lambda:.4f}")
    print(f"Corresponding eigenvector (x) of P:\n{x}\n")

    # --- 2. Verification Check in Python (P*x = λ*x) ---
    print("Verification Check:")
    px_vec = P @ x
    lambda_x_vec = selected_lambda * x
    print_vector("P * x      ", px_vec)
    print_vector("λ * x      ", lambda_x_vec)
    print(f"Is Px ≈ λx?  {np.allclose(px_vec, lambda_x_vec)}\n")


    # Calculate matrix Q = R⁻¹ * P * R
    Q = R_inv @ P @ R
    print_matrix("Q (calculated as R⁻¹PR)", Q)


    # --- 3. Calling the C Library for Final Verification ---
    print("--- Testing the Options ---")

    # Determine library file extension based on OS
    lib_ext = ".dll" if os.name == 'nt' else ".so"
    lib_path = "./matrix_ops" + lib_ext
    
    if not os.path.exists(lib_path):
        print(f"Error: Shared library '{lib_path}' not found.")
        print("Please compile the C code first (see README.md).")
        return

    # Load the shared library
    c_lib = ctypes.CDLL(lib_path)

    # Define the argument types for the C function
    # All arguments are pointers to doubles, except for lambda (double) and n (int)
    c_double_p = ctypes.POINTER(ctypes.c_double)
    c_lib.perform_verification.argtypes = [
        c_double_p, c_double_p, c_double_p, c_double_p,
        ctypes.c_double, ctypes.c_int,
        c_double_p, c_double_p, c_double_p, c_double_p
    ]
    c_lib.perform_verification.restype = None

    # Prepare data for C function
    n = 3
    # Convert numpy arrays to the ctypes format
    Q_c = Q.astype(np.float64).ctypes.data_as(c_double_p)
    R_c = R.astype(np.float64).ctypes.data_as(c_double_p)
    R_inv_c = R_inv.astype(np.float64).ctypes.data_as(c_double_p)
    x_c = x.astype(np.float64).ctypes.data_as(c_double_p)
    lambda_c = ctypes.c_double(selected_lambda)

    # Create empty numpy arrays to hold the results from the C function
    q_rx_result = np.zeros(n, dtype=np.float64)
    lambda_rx_result = np.zeros(n, dtype=np.float64)
    q_rinvx_result = np.zeros(n, dtype=np.float64)
    lambda_rinvx_result = np.zeros(n, dtype=np.float64)

    # Call the C function
    c_lib.perform_verification(
        Q_c, R_c, R_inv_c, x_c, lambda_c, n,
        q_rx_result.ctypes.data_as(c_double_p),
        lambda_rx_result.ctypes.data_as(c_double_p),
        q_rinvx_result.ctypes.data_as(c_double_p),
        lambda_rinvx_result.ctypes.data_as(c_double_p)
    )

    # --- 4. Print the results from the C function ---
    print("a) Is Q(Rx) ≈ λ(Rx)?", np.allclose(q_rx_result, lambda_rx_result))
    print_vector("  Q(Rx) ", q_rx_result)
    print_vector("  λ(Rx) ", lambda_rx_result)
    print()

    print("c) Is Q(R⁻¹x) ≈ λ(R⁻¹x)?", np.allclose(q_rinvx_result, lambda_rinvx_result))
    print_vector("  Q(R⁻¹x) ", q_rinvx_result)
    print_vector("  λ(R⁻¹x) ", lambda_rinvx_result)


if __name__ == "__main__":
    main()

