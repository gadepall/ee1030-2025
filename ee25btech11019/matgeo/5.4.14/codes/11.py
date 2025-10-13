import ctypes
import numpy as np
import sympy as sp

# ====== Load Shared Library (.so) ======
lib = ctypes.CDLL("./libinverse.so")

# Define argument types for C function
lib.inverse.argtypes = [
    ctypes.POINTER((ctypes.c_double * 2) * 2),  # Input matrix A
    ctypes.POINTER((ctypes.c_double * 2) * 2)   # Output inverse matrix
]

# ====== Define the Matrix ======
A = np.array([[2, -6],
              [1, -2]], dtype=np.double)

inv = np.zeros((2, 2), dtype=np.double)

# ====== Call the C Function ======
lib.inverse(
    A.ctypes.data_as(ctypes.POINTER((ctypes.c_double * 2) * 2)),
    inv.ctypes.data_as(ctypes.POINTER((ctypes.c_double * 2) * 2))
)

# ====== Convert and Display Results ======
A_sym = sp.Matrix(A)
A_inv_sym = A_sym.inv()           # Sympy inverse (for verification)
A_inv_c = sp.Matrix(inv)          # Inverse from C code

print("Matrix A:")
sp.pprint(A_sym)

print("\nInverse computed in C:")
sp.pprint(A_inv_c)

print("\nInverse computed in Sympy:")
sp.pprint(A_inv_sym)
