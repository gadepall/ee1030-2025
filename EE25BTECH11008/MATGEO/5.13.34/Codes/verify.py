import ctypes
import numpy as np
import os

# Path to compiled shared library
libname = "./verify.so"

# Load the shared library
lib = ctypes.CDLL(libname)

# Define argument and return types for the C functions
c_double_p = ctypes.POINTER(ctypes.c_double)

lib.matmul.argtypes = [c_double_p, c_double_p, c_double_p,
                       ctypes.c_int, ctypes.c_int, ctypes.c_int]
lib.transpose.argtypes = [c_double_p, c_double_p,
                          ctypes.c_int, ctypes.c_int]
lib.adj.argtypes = [c_double_p, c_double_p, ctypes.c_int]

# Determinant (optional if present)
if hasattr(lib, "det"):
    lib.det.argtypes = [c_double_p, ctypes.c_int]
    lib.det.restype = ctypes.c_double


# --- Wrappers around C functions ---
def matmul(A, B):
    """Matrix multiplication using C matmul."""
    a, b = A.shape
    b2, c = B.shape
    assert b == b2
    C = np.zeros((a, c), dtype=np.float64)
    lib.matmul(A.ctypes.data_as(c_double_p),
               B.ctypes.data_as(c_double_p),
               C.ctypes.data_as(c_double_p),
               ctypes.c_int(a), ctypes.c_int(b), ctypes.c_int(c))
    return C


def transpose(A):
    """Transpose using C transpose."""
    m, n = A.shape
    AT = np.zeros((n, m), dtype=np.float64)
    lib.transpose(A.ctypes.data_as(c_double_p),
                  AT.ctypes.data_as(c_double_p),
                  ctypes.c_int(m), ctypes.c_int(n))
    return AT


def adj(A):
    """Adjugate using C adj."""
    n, m = A.shape
    assert n == m
    Adj = np.zeros_like(A, dtype=np.float64)
    lib.adj(A.ctypes.data_as(c_double_p),
            Adj.ctypes.data_as(c_double_p),
            ctypes.c_int(n))
    return Adj


# --- Verification of statements (a)-(d) ---

def check_statements(n=3, tol=1e-6):
    M = np.random.randint(-5, 6, (n, n)).astype(np.float64)
    N = np.random.randint(-5, 6, (n, n)).astype(np.float64)

    print("M =\n", M)
    print("N =\n", N)

    MT = transpose(M)
    NT = transpose(N)

    # (a)
    symM = 0.5 * (M + MT)
    skewM = 0.5 * (M - MT)

    A1 = matmul(matmul(NT, symM), N)
    A2 = matmul(matmul(NT, skewM), N)

    print("\n(a)")
    print("Symmetric M -> N^T M N symmetric?", np.allclose(A1, transpose(A1), atol=tol))
    print("Skew-symmetric M -> N^T M N skew-symm?", np.allclose(A2, -transpose(A2), atol=tol))

    # (b)
    MN = matmul(M, N)
    NM = matmul(N, M)
    comm = MN - NM
    print("\n(b)")
    print("MN - NM skew-symmetric?", np.allclose(transpose(comm), -comm, atol=tol))

    # (c)
    symN = 0.5 * (N + NT)
    prod = matmul(symM, symN)
    print("\n(c)")
    print("Product of symmetric M,N symmetric?", np.allclose(prod, transpose(prod), atol=tol))

    # (d)
    adjM = adj(M)
    adjN = adj(N)
    left = matmul(adjM, adjN)
    MN = matmul(M, N)
    adjMN = adj(MN)
    print("\n(d)")
    print("adj(M)adj(N) == adj(MN)?", np.allclose(left, adjMN, atol=tol))

if __name__ == "__main__":
    check_statements(3)
