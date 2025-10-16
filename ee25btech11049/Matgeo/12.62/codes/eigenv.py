import ctypes
import numpy as np
import os
import platform

# --- Step 1: Compile the C code into a shared library ---
# This script will attempt to compile the C code automatically.
# The C source file is expected to be 'eigen_lib.c'.

c_file_name = 'eigenv.c'

# Determine the correct file extension for the shared library based on the OS
if platform.system() == "Windows":
    lib_name = 'eigen_lib.dll'
    compile_command = f"gcc -shared -o {lib_name} -fPIC {c_file_name}"
elif platform.system() == "Darwin": # macOS
    lib_name = 'eigen_lib.dylib'
    compile_command = f"gcc -shared -o {lib_name} -fPIC {c_file_name}"
else: # Linux
    lib_name = 'eigenv.so'
    compile_command = f"gcc -shared -o {lib_name} -fPIC {c_file_name}"

# Compile the C code if the library file doesn't exist
if not os.path.exists(lib_name):
    print(f"Shared library '{lib_name}' not found. Attempting to compile '{c_file_name}'...")
    exit_code = os.system(compile_command)
    if exit_code != 0:
        print(f"\nError: Compilation failed. Please ensure GCC is installed and in your system's PATH.")
        print(f"Manual compile command: {compile_command}")
        exit()
    print("Compilation successful.")

# --- Step 2: Load the shared library using ctypes ---
try:
    # Use the absolute path to ensure the library is found
    eigen_lib = ctypes.CDLL(os.path.abspath(lib_name))
except OSError as e:
    print(f"Error loading shared library: {e}")
    exit()

# --- Step 3: Define the function signature (argument and return types) ---
# The C function is:
# void find_2x2_eigenvalues(double a, double b, double c, double d, double* eig1, double* eig2)
find_2x2_eigenvalues_c = eigen_lib.find_2x2_eigenvalues
find_2x2_eigenvalues_c.argtypes = [
    ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]
find_2x2_eigenvalues_c.restype = None  # Corresponds to a 'void' return type in C

# --- Step 4: Prepare data and call the C function ---

# The full 3x3 matrix is block-diagonal, so we can analyze it in parts.
# [[2, 3, 0],
#  [3, 2, 0],
#  [0, 0, 1]]
# One eigenvalue is 1. The other two come from the top-left 2x2 sub-matrix.
sub_matrix = np.array([[2, 3], [3, 2]])
a, b = sub_matrix[0]
c, d = sub_matrix[1]

# Create C-compatible double variables to hold the results from the C function
eig1_c = ctypes.c_double()
eig2_c = ctypes.c_double()

print(f"Calling C function to find eigenvalues of the sub-matrix:\n{sub_matrix}\n")

# Call the C function, passing pointers to the result variables
find_2x2_eigenvalues_c(a, b, c, d, ctypes.byref(eig1_c), ctypes.byref(eig2_c))

# --- Step 5: Retrieve the results and combine them ---
eigenvalues_from_c = [eig1_c.value, eig2_c.value]
third_eigenvalue = 1.0
all_eigenvalues = eigenvalues_from_c + [third_eigenvalue]

# Sort for consistent output
all_eigenvalues.sort(reverse=True)

print(f"Eigenvalues from C function: {eigenvalues_from_c}")
print(f"Third eigenvalue from observation: {third_eigenvalue}")
print(f"\nFinal eigenvalues for the 3x3 matrix are: {all_eigenvalues}")

