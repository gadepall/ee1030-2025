import ctypes


eigen_lib = ctypes.CDLL('./eigen.so')

# Define the function signature (argument types and return type).
# This helps ctypes correctly handle data marshalling.
find_eigs = eigen_lib.find_eigenvalues_2x2
find_eigs.argtypes = [ctypes.c_double, ctypes.c_double, 
                      ctypes.c_double, ctypes.c_double,
                      ctypes.POINTER(ctypes.c_double), 
                      ctypes.POINTER(ctypes.c_double)]
find_eigs.restype = None  # The C function returns void

# Define the matrix elements
a, b = 0.0, 1.0
c, d = 1.0, 0.0

# Create C-compatible double variables to store the results
eig1 = ctypes.c_double()
eig2 = ctypes.c_double()

# Call the C function from Python
# We pass the result variables by reference using byref()
find_eigs(a, b, c, d, ctypes.byref(eig1), ctypes.byref(eig2))

print("Eigenvalues found using Python wrapper for C library:")
# Access the value of the ctypes object with .value
print(f"Lambda 1: {eig1.value}")
print(f"Lambda 2: {eig2.value}")
