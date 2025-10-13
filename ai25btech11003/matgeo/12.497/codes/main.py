import ctypes

# Load shared library
lib = ctypes.CDLL('./main.so')

# Signature: compute_char_eq(int n, double* A, char* filename)
lib.compute_char_eq.argtypes = [ctypes.c_int,
                                ctypes.POINTER(ctypes.c_double),
                                ctypes.c_char_p]

# Matrix A = [3 2; 4 1]
n = 2
# Flattened row-major
arr = (ctypes.c_double * 4)(3.0, 2.0, 4.0, 1.0)

# Call and write to main.dat
lib.compute_char_eq(n, arr, b"main.dat")

# Read and display
with open("main.dat", "r") as f:
    print("Characteristic equation:", f.read().strip())

