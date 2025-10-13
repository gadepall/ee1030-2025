import ctypes
import numpy as np

lib = ctypes.CDLL('./libmatrixops.so')  # Adjust path as needed

# Define float array type for double[N*N]
N = 3
FloatArray = ctypes.c_double * (N * N)

# Define function signature
lib.det_P2_Q2.argtypes = [FloatArray, FloatArray, ctypes.c_int]
lib.det_P2_Q2.restype = ctypes.c_double

# Example matrices P and Q as 1D arrays (row-major)
P = np.array([
    1, 1, 0,
    0, 1, 1,
    0, 0, 1], dtype=np.float64)

Q = np.array([
    1, 0, 1,
    0, 1, 1,
    0, 0, 1], dtype=np.float64)

# Call the C function
det = lib.det_P2_Q2(FloatArray(*P), FloatArray(*Q), N)
if det < 0:
    print("Conditions not satisfied")
else:
    print("det(P^2 + Q^2) =", det)
