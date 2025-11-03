import ctypes
import numpy as np

# Load the shared library
lib = ctypes.CDLL("./libmatrix.so")

# Define function signature: int inverse2x2(const double A[2][2], double Inv[2][2])
lib.inverse2x2.argtypes = [
    (ctypes.c_double * 2) * 2,   # input matrix
    (ctypes.c_double * 2) * 2    # output matrix
]
lib.inverse2x2.restype = ctypes.c_int

def inverse2x2(A):
    """
    Call the C function to compute inverse of 2x2 matrix.
    A: numpy array (2x2)
    Returns: numpy array (2x2) or None if singular
    """
    A_c = ((ctypes.c_double * 2) * 2)()
    Inv_c = ((ctypes.c_double * 2) * 2)()

    # Fill input matrix
    for i in range(2):
        for j in range(2):
            A_c[i][j] = A[i, j]

    # Call C function
    status = lib.inverse2x2(A_c, Inv_c)
    if status != 0:
        return None  # singular

    # Convert back to numpy
    Inv = np.zeros((2, 2))
    for i in range(2):
        for j in range(2):
            Inv[i, j] = Inv_c[i][j]
    return Inv

# ---- Example Usage without plotting ----
m_values = np.linspace(0.1, 5, 50)
determinants = []
inverse_norms = []

for m in m_values:
    A = np.array([[1, m], [4, 2]], dtype=float)  # parametric family of matrices
    det = np.linalg.det(A)
    Inv = inverse2x2(A)

    determinants.append(det)
    if Inv is not None:
        inverse_norms.append(np.linalg.norm(Inv))
    else:
        inverse_norms.append(np.nan)

# Print results
for i, m in enumerate(m_values):
    print(f"m = {m:.2f}, det(A) = {determinants[i]:.4f}, ||A^-1|| = {inverse_norms[i]}")

