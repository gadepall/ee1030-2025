import ctypes

# Load shared library
lib = ctypes.CDLL("./code.so")

# Define argument and return types
lib.solveSystem.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double)
]

# Prepare result array
sol = (ctypes.c_double * 2)()

# ---- Fixed values ----
a = -3
lam = 2
mu = -2

# ---- Call C function ----
lib.solveSystem(a, lam, mu, sol)

# ---- Display result (if unique) ----
if a != -3:
    print(f"x = {sol[0]:.3f}, y = {sol[1]:.3f}")
