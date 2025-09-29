import ctypes

# Load the shared library (make sure parallel.so is in the same folder)
lib = ctypes.CDLL("./parallel.so")

# Define argument and return types
lib.check_parallel.argtypes = [
    ctypes.POINTER(ctypes.c_double),  # a
    ctypes.POINTER(ctypes.c_double),  # b
    ctypes.POINTER(ctypes.c_double),  # c
    ctypes.POINTER(ctypes.c_double)   # d
]
lib.check_parallel.restype = ctypes.c_int

def check_parallel(a, b, c, d):
    """
    Calls the C function check_parallel(a, b, c, d).
    Each of a, b, c, d must be length-3 lists or tuples.
    Returns True if (a-2d) || (2b-c), False otherwise.
    """
    # Convert Python lists to C arrays
    A = (ctypes.c_double * 3)(*a)
    B = (ctypes.c_double * 3)(*b)
    C = (ctypes.c_double * 3)(*c)
    D = (ctypes.c_double * 3)(*d)

    # Call the C function
    result = lib.check_parallel(A, B, C, D)
    return bool(result)

# ---------------- Example usage ----------------
if __name__ == "__main__":
    a = [1.0, 2.0, 3.0]
    b = [2.0, -1.0, 0.0]
    c = [0.0, 4.0, 1.0]
    d = [1.0, 0.0, -1.0]

    if check_parallel(a, b, c, d):
        print("(a - 2d) is parallel to (2b - c)")
    else:
        print("(a - 2d) is NOT parallel to (2b - c)")

