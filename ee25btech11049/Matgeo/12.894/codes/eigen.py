import numpy as np

# Define the matrix from the image.
# [[0, -1],
#  [1,  0]]
A = np.array([[0, -1],
              [1,  0]])

# Use numpy's linear algebra module to find the eigenvalues.
eigenvalues = np.linalg.eigvals(A)

# Print the original matrix.
print("Matrix:")
print(A)

# --- MODIFIED SECTION ---
# Custom format the eigenvalues for a cleaner look.
# We access the imaginary part (.imag) of each number and cast it to an integer
# to remove the ".0", then append "j".
formatted_vals = [f"{int(val.imag)}j" for val in eigenvalues]

print("\nEigenvalues:")
print(f"The eigenvalues are {formatted_vals[0]} and {formatted_vals[1]}")
