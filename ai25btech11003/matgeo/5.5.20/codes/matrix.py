import numpy as np
import struct
import os

def read_matrix_from_binary(filename):
    """Read the 3x3 matrix from binary file"""
    if not os.path.exists(filename):
        print(f"Error: {filename} not found. Please run the C program first.")
        return None

    matrix = np.zeros((3, 3))
    with open(filename, 'rb') as f:
        for i in range(3):
            for j in range(3):
                data = f.read(8)  # 8 bytes for double
                if len(data) == 8:
                    matrix[i][j] = struct.unpack('d', data)[0]
    return matrix

def verify_inverse():
    """Verify that A * A^(-1) = I"""
    # Original matrix A
    A = np.array([
        [3.0, 0.0, -1.0],
        [2.0, 3.0,  0.0],
        [0.0, 4.0,  1.0]
    ])

    print("Original Matrix A:")
    print(A)
    print()

    # Read the computed inverse from binary file
    A_inv = read_matrix_from_binary("main.dat")

    if A_inv is None:
        return

    print("Computed Inverse Matrix A^(-1):")
    print(A_inv)
    print()

    # Expected inverse from the PDF solution
    expected_inv = np.array([
        [7/3, -25/27, 7/3],
        [-2, 11/9, -2],
        [8, -4, 9]
    ])

    print("Expected Inverse Matrix (from PDF):")
    print(expected_inv)
    print()

    # Verify A * A^(-1) = I
    identity_check = np.dot(A, A_inv)
    print("Verification: A * A^(-1) =")
    print(identity_check)
    print()

    # Check if it's close to identity matrix
    identity = np.eye(3)
    is_correct = np.allclose(identity_check, identity, atol=1e-10)
    print(f"Is the inverse correct? {is_correct}")

    # Compare with expected result
    is_expected = np.allclose(A_inv, expected_inv, atol=1e-6)
    print(f"Does it match expected result? {is_expected}")

    # Additional verification using NumPy's built-in inverse
    numpy_inv = np.linalg.inv(A)
    print("\nNumPy computed inverse:")
    print(numpy_inv)

    matches_numpy = np.allclose(A_inv, numpy_inv, atol=1e-6)
    print(f"Matches NumPy result? {matches_numpy}")

def check_files():
    """Check if required files exist"""
    files_exist = {
        "main.so": os.path.exists("main.so"),
        "main.dat": os.path.exists("main.dat")
    }

    print("File Status:")
    for filename, exists in files_exist.items():
        status = "✓ Found" if exists else "✗ Missing"
        print(f"{filename}: {status}")

    return all(files_exist.values())

if __name__ == "__main__":
    print("Matrix Inverse Verification Program")
    print("=" * 40)
    print()

    # Check if files exist
    if not check_files():
        print("\nPlease run the C program first to generate main.so and main.dat files.")
        
    else:
        print("\nAll required files found. ")
        print()
        verify_inverse()
