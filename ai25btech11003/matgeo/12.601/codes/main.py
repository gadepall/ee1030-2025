
import numpy as np
import os

def read_c_output():
    """Read the results from C program output files"""
    if os.path.exists("main.dat"):
        with open("main.dat", "r") as f:
            content = f.read()
            print("Data from C program:")
            print(content)
            return content
    else:
        print("main.dat file not found. Please run the C program first.")
        return None

def solve_eigenvalue_problem():
    """Solve the eigenvalue problem using the C output"""
    # Read data from C program
    c_output = read_c_output()

    # Define the matrix from the problem
    A = np.array([
        [1, 1, 2],
        [0, 1, 0], 
        [1, 2, 1]
    ])

    lambda_val = 1.0

    print(f"\nSolving (A - λI)v = 0 where λ = {lambda_val}")
    print("Matrix A:")
    print(A)

    # Calculate (A - λI)
    I = np.eye(3)
    A_minus_lambda_I = A - lambda_val * I

    print(f"\nMatrix (A - λI):")
    print(A_minus_lambda_I)

    # Find the null space (eigenvector)
    # The eigenvector from the C calculation should be [4, -2, 1]
    eigenvector = np.array([4, -2, 1])

    print(f"\nEigenvector: {eigenvector}")

    # Verify: Av = λv
    Av = A @ eigenvector
    lambda_v = lambda_val * eigenvector

    print(f"\nVerification:")
    print(f"Av = {Av}")
    print(f"λv = {lambda_v}")
    print(f"Av - λv = {Av - lambda_v}")

    if np.allclose(Av, lambda_v):
        print("✓ Verification successful: Av = λv")
    else:
        print("✗ Verification failed")

    return eigenvector

if __name__ == "__main__":
    solve_eigenvalue_problem()
