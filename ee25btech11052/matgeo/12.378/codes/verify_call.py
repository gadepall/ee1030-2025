import ctypes

# 1. Load the shared library from the current directory
lib = ctypes.CDLL('./eigen_solver.so')

# 2. Define the argument types for the C function
#    It expects: double, double, double, double, pointer(double), pointer(double)
lib.find_eigenvalues.argtypes = [
    ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]

# 3. Create C-type variables to store the results
eig1 = ctypes.c_double()
eig2 = ctypes.c_double()

# 4. Call the C function with the matrix values (6, 1, -2, 3)
#    ctypes.byref() passes the variables as pointers
lib.find_eigenvalues(6.0, 1.0, -2.0, 3.0, ctypes.byref(eig1), ctypes.byref(eig2))

# 5. Print the results stored in the C-type variables
#    Access the value using the .value attribute
print(f"The eigenvalues are: {eig1.value} and {eig2.value}")