import ctypes
import numpy as np
import os

# Define the name of the shared library based on the operating system
if os.name == 'nt':  # Windows
    lib_name = 'matrix_ops.dll'
else:  # Linux, macOS, etc.
    lib_name = 'matrix.so'
    
# Check if the library file exists before trying to load it
if not os.path.exists(lib_name):
    print(f"Error: Shared library '{lib_name}' not found.")
    print("Please compile 'matrix_ops.c' first. See README.md for instructions.")
    exit()

# Load the shared library
c_lib = ctypes.CDLL(os.path.abspath(lib_name))

# Define the argument types and return type for the C function.
# This ensures Python sends the data in the correct format.
# The function expects three arguments: pointers to C doubles.
c_lib.multiply_and_transpose.argtypes = [
    ctypes.POINTER(ctypes.c_double), 
    ctypes.POINTER(ctypes.c_double), 
    ctypes.POINTER(ctypes.c_double)
]
# The C function doesn't return a value; it modifies the 'result' array in place.
c_lib.multiply_and_transpose.restype = None

# Define the input matrices using numpy.
# It's crucial to specify the dtype as np.double to match 'c_double' in ctypes.
A = np.array([[2, 4], [1, 3]], dtype=np.double)
B = np.array([[4, 6], [5, 9]], dtype=np.double)

# Create an empty numpy array to store the result from the C function.
result_from_c = np.empty((2, 2), dtype=np.double)

# Convert the numpy arrays into a format that ctypes can use.
# This gets a C-compatible pointer to the underlying data buffer of the array.
A_ptr = A.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
B_ptr = B.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
result_ptr = result_from_c.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

# Call the C function with the pointers to the data
c_lib.multiply_and_transpose(A_ptr, B_ptr, result_ptr)

# Print the original matrices and the final result
print("Matrix A:\n", A)
print("\nMatrix B:\n", B)
print("\nResult from C function (AB)T:\n", result_from_c)

