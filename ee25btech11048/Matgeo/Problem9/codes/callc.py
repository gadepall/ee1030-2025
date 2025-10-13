import ctypes

# Load shared library
lib = ctypes.CDLL("./points.so")

# Argument and return types
lib.compute.argtypes = [
    ctypes.POINTER(ctypes.c_double),  # a
    ctypes.POINTER(ctypes.c_double),  # b
    ctypes.POINTER(ctypes.c_double),  # c
    ctypes.POINTER(ctypes.c_double),  # lhs
    ctypes.POINTER(ctypes.c_double)   # rhs
]

def compute(a, b, c):
    a_arr = (ctypes.c_double*3)(*a)
    b_arr = (ctypes.c_double*3)(*b)
    c_arr = (ctypes.c_double*3)(*c)
    lhs = ctypes.c_double()
    rhs = ctypes.c_double()
    lib.compute(a_arr, b_arr, c_arr, ctypes.byref(lhs), ctypes.byref(rhs))
    return lhs.value, rhs.value

if __name__ == "__main__":
    # Input vectors
    a = list(map(float, input("Enter vector a (3 values): ").split()))
    b = list(map(float, input("Enter vector b (3 values): ").split()))
    c = list(map(float, input("Enter vector c (3 values): ").split()))

    lhs, rhs = compute(a, b, c)

    print(f"LHS = {lhs:.4f}")
    print(f"RHS = {rhs:.4f}")

    if abs(lhs - rhs) < 1e-6:
        print("✅ The equality holds (both sides are zero).")
    else:
        print("❌ The equality does NOT hold.")

