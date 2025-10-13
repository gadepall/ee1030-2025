import ctypes

# Load the shared library
lib = ctypes.CDLL("./solution.so")

# Define argument and return types for the function
lib.reflect_point.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                              ctypes.POINTER(ctypes.c_double),
                              ctypes.POINTER(ctypes.c_double),
                              ctypes.POINTER(ctypes.c_double)]

# Wrapper function
def reflect_point(x, y, z):
    alpha = ctypes.c_double()
    beta  = ctypes.c_double()
    gamma = ctypes.c_double()

    # Call C function
    lib.reflect_point(x, y, z,
                      ctypes.byref(alpha),
                      ctypes.byref(beta),
                      ctypes.byref(gamma))
    return alpha.value, beta.value, gamma.value


# --- Main ---
if __name__ == "__main__":
    x, y, z = map(float, input("Enter coordinates of Q (x y z): ").split())
    alpha, beta, gamma = reflect_point(x, y, z)
    print(f"Reflected point S = ({alpha:.6f}, {beta:.6f}, {gamma:.6f})")

