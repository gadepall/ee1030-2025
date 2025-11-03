import numpy as np

def calculate_eigenvalues():
    # b = (0, 1, 0)
    # Cross product matrix M for b × x is:
    # |  0   0   1 |
    # |  0   0   0 |
    # | -1   0   0 |

    # Define the 3x3 matrix M using a NumPy array
    M = np.array([
        [0, 0, 1],
        [0, 0, 0],
        [-1, 0, 0]
    ])

    # Calculate the eigenvalues and (optionally) eigenvectors
    # 'w' will contain the eigenvalues (complex numbers)
    w, v = np.linalg.eig(M)

    # Note: The characteristic equation λ(λ^2 + 1) = 0 yields 
    # λ = 0, i, -i. The calculated values should match these.
    
    # Sort the eigenvalues for consistent output order (optional)
    # Sorting a mix of real and complex numbers can be tricky; 
    # we'll just print them as they come out for simplicity, 
    # which is usually (0+0j), (0+1j), (0-1j) or a permutation.

    print("The eigenvalues of matrix M are:")
    # Use a loop to print each eigenvalue
    for i, eigenvalue in enumerate(w):
        # NumPy returns eigenvalues as complex numbers (even if the imaginary part is zero)
        # We can format the output to match the C code style (real + imag*i)
        print(f"λ{i+1} = {eigenvalue.real:.1f} + {eigenvalue.imag:.1f}i")

# Execute the function
if __name__ == "__main__":
    calculate_eigenvalues()