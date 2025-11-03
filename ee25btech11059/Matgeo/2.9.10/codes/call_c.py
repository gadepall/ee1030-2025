import ctypes
import os

# locate shared library
_dir = os.path.dirname(__file__)
lib_path = os.path.join(_dir, "libmatrix_vectors.so")

lib = ctypes.CDLL(lib_path)

# declare the argument types and return type
lib.solve_matrix_vectors.argtypes = [
    ctypes.c_double,  # a0 (ax)
    ctypes.c_double,  # a1 (ay)
    ctypes.c_double,  # b0 (bx)
    ctypes.c_double   # b1 (by)
]
lib.solve_matrix_vectors.restype = ctypes.c_int

def solve_matrix_vectors(a0, a1, b0, b1):
    """Wrapper function returning True / False."""
    res = lib.solve_matrix_vectors(ctypes.c_double(a0),
                                   ctypes.c_double(a1),
                                   ctypes.c_double(b0),
                                   ctypes.c_double(b1))
    return bool(res)

if __name__ == "__main__":
    # Examples
    a0, a1 = 2.0, 1.0
    b0, b1 = 1.0, 2.0

    if solve_matrix_vectors(a0, a1, b0, b1):
        print("(a + 2b) is perpendicular to a under the condition ||a + b|| = ||b||")
    else:
        print("Condition fails or not perpendicular.")


