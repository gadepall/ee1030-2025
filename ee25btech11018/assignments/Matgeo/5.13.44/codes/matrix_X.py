import ctypes
import numpy as np

# Load shared library
lib = ctypes.CDLL("./libmatrix_X.so")

# Define types
N = 3
DoubleArray3 = ctypes.c_double * N
DoubleMatrix3 = (DoubleArray3 * N)

# Function signatures
lib.compute_X.argtypes = [DoubleMatrix3]
lib.trace.argtypes = [DoubleMatrix3]
lib.trace.restype = ctypes.c_double
lib.is_symmetric.argtypes = [DoubleMatrix3, ctypes.c_double]
lib.is_symmetric.restype = ctypes.c_int
lib.mat_vec_mul.argtypes = [DoubleMatrix3, DoubleArray3, DoubleArray3]
lib.subtract_scalar_I.argtypes = [DoubleMatrix3, ctypes.c_double, DoubleMatrix3]
lib.determinant.argtypes = [DoubleMatrix3]
lib.determinant.restype = ctypes.c_double

# Initialize matrices
X = DoubleMatrix3()
lib.compute_X(X)

# Convert to numpy for easier viewing
X_np = np.array([[X[i][j] for j in range(N)] for i in range(N)])
print("Matrix X =\n", X_np)

# Compute trace
trace_val = lib.trace(X)
print("\nTrace(X) =", trace_val)

# Check symmetry
sym = lib.is_symmetric(X, 1e-9)
print("Symmetric:", "Yes" if sym else "No")

# Compute α for X*[1 1 1]^T
v = DoubleArray3(1.0, 1.0, 1.0)
y = DoubleArray3()
lib.mat_vec_mul(X, v, y)
y_vals = [y[i] for i in range(N)]
alpha = y_vals[0]
print("\nX*[1 1 1]^T =", y_vals)
print("Alpha =", alpha)

# Compute determinant of (X - 30I)
Y = DoubleMatrix3()
lib.subtract_scalar_I(X, 30.0, Y)
det_val = lib.determinant(Y)
print("\nDeterminant of (X - 30I):", det_val)
if abs(det_val) < 1e-9:
    print("=> (X - 30I) is NOT invertible (singular)")
else:
    print("=> (X - 30I) is invertible")

