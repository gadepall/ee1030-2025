import ctypes
import numpy as np
import os
import platform

# --- Step 1: Compile the C code into a shared library ---
c_file_name = 'eigenv.c'

# Determine the correct file extension for the shared library and compile command
if platform.system() == "Windows":
    lib_name = 'eigen_lib.dll'
    compile_command = f"gcc -shared -o {lib_name} -fPIC {c_file_name}"
elif platform.system() == "Darwin": # macOS
    lib_name = 'eigen_lib.dylib'
    compile_command = f"gcc -shared -o {lib_name} -fPIC {c_file_name}"
else: # Linux
    lib_name = 'eigenv.so'
    # Add -lm to link the math library on Linux/macOS
    compile_command = f"gcc -shared -o {lib_name} -fPIC {c_file_name} -lm"

# Compile the C code if the library file doesn't exist
if not os.path.exists(lib_name):
    print(f"Shared library not found. Compiling '{c_file_name}'...")
    if os.system(compile_command) != 0:
        print(f"\nError: Compilation failed. Please ensure GCC is installed.")
        exit()
    print("Compilation successful.")

# --- Step 2: Load the shared library ---
try:
    eigen_lib = ctypes.CDLL(os.path.abspath(lib_name))
except OSError as e:
    print(f"Error loading shared library: {e}")
    exit()

# --- Step 3: Define the function signature ---
# The modified C function signature is:
# void find_2x2_eigenvalues(double, double, double, double, double*, double*, double*, double*)
find_2x2_c = eigen_lib.find_2x2_eigenvalues
find_2x2_c.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
]
find_2x2_c.restype = None

# --- Step 4: Prepare data and call the C function ---
# The matrix from the image is:
# [[0, -1],
#  [1,  0]]
matrix = np.array([[0, -1], [1, 0]])
a, b = float(matrix[0, 0]), float(matrix[0, 1])
c, d = float(matrix[1, 0]), float(matrix[1, 1])

# Create C-compatible double variables to hold the real and imaginary parts
eig1_real, eig1_imag = ctypes.c_double(), ctypes.c_double()
eig2_real, eig2_imag = ctypes.c_double(), ctypes.c_double()

print(f"Calling C function to find eigenvalues of the matrix:\n{matrix}\n")

# Call the C function, passing pointers to the result variables
find_2x2_c(a, b, c, d,
           ctypes.byref(eig1_real), ctypes.byref(eig1_imag),
           ctypes.byref(eig2_real), ctypes.byref(eig2_imag))

# --- Step 5: Retrieve the results and combine them into complex numbers ---
eigenvalue1 = complex(eig1_real.value, eig1_imag.value)
eigenvalue2 = complex(eig2_real.value, eig2_imag.value)

print(f"Eigenvalues from C function are: {eigenvalue1} and {eigenvalue2}")
