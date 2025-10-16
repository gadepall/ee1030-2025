import ctypes
import os

# Define the name of the shared library based on the operating system
if os.name == 'nt': # Windows
    lib_name = 'solver.dll'
else: # Linux, macOS, etc.
    lib_name = 'solver.so'

# Construct the full path to the library file in the current directory
lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), lib_name)

try:
    # 1. Load the shared library
    solver_lib = ctypes.CDLL(lib_path)
except OSError as e:
    print(f"Error: Could not load the shared library '{lib_name}'.")
    print("Please make sure you have compiled the C code first.")
    print(f"Details: {e}")
    exit()

# 2. Define the function signature to match the C code
#    Specify the argument types (argtypes)
solver_lib.solve_determinant_2x2.argtypes = [ctypes.c_double, ctypes.c_double]
#    Specify the return type (restype)
solver_lib.solve_determinant_2x2.restype = ctypes.c_double

# 3. Define the input values from the problem
trace_A = 3.0
trace_A3 = -18.0

# 4. Call the C function from Python
#    Python floats will be automatically converted to ctypes.c_double
determinant = solver_lib.solve_determinant_2x2(trace_A, trace_A3)

# 5. Print the result
print("--- Calling C function from Python using ctypes ---")
print(f"Given tr(A) = {trace_A}")
print(f"Given tr(A^3) = {trace_A3}")
print("-" * 25)
print(f"The calculated determinant of A is: {determinant}")

