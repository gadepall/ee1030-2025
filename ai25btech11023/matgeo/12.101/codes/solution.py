import ctypes

# Load the compiled shared library
matfun = ctypes.CDLL('./libmatfun.so')  # or .dll on Windows

# Function prototypes
matfun.compute_eigenvalues.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
matfun.characteristic_b.argtypes = [ctypes.c_double, ctypes.c_double]
matfun.characteristic_c.argtypes = [ctypes.c_double, ctypes.c_double]
matfun.ratio_b_c.argtypes = [ctypes.c_double, ctypes.c_double]

matfun.characteristic_b.restype = ctypes.c_double
matfun.characteristic_c.restype = ctypes.c_double
matfun.ratio_b_c.restype = ctypes.c_double

# Given values
tr = 5.0
det = 6.0
lambda1 = ctypes.c_double()
lambda2 = ctypes.c_double()

# Step 1: Compute eigenvalues
matfun.compute_eigenvalues(tr, det, ctypes.byref(lambda1), ctypes.byref(lambda2))
print(f"Eigenvalues: {lambda1.value:.1f}, {lambda2.value:.1f}")

# Step 2: Calculate b and c
b = matfun.characteristic_b(lambda1.value, lambda2.value)
c = matfun.characteristic_c(lambda1.value, lambda2.value)
print(f"b = {b}")
print(f"c = {c}")

# Step 3: Compute b/c
bc = matfun.ratio_b_c(b, c)
print(f"b/c = {bc}")
